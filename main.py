#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
from Variable import Variable
from window import Ui_MainWindow
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class Formulario(QMainWindow):
    #Constructor de la clase
    def __init__(self):
        #Inicio el objeto QMainwindow
        QMainWindow.__init__(self)
        self.formulario = Ui_MainWindow()
        self.formulario.setupUi(self)

        #seteamos las variables iniciales
        self.iniciarVariables()
        #self.formulario.btnSimulacion.clicked.connect(self.iniciarVariables)
        #seteamos los eventos        
        self.formulario.btnSimulacion.clicked.connect(self.simular)

    def iniciarVariables(self):
        self.formulario.lineEdit_exp.setText("1")
        self.formulario.lineEdit_dias.setText("20")
        self.formulario.lineEdit_incrementoM4.setText("50")
        self.formulario.lineEdit_incrementoM6.setText("30")
        self.formulario.lineEdit_velOperM4.setText("15")
        self.formulario.lineEdit_velOperM6.setText("20")
        self.formulario.lineEdit_diasProd.setText("10")
    
    def calcular_porcentajes(self, solicitudesAtendidas, solicitudesSinAtender):
        total = solicitudesAtendidas + solicitudesSinAtender
        porc_atendidas = ( solicitudesAtendidas * 100 ) / total
        porc_sin_atender = ( solicitudesSinAtender * 100) / total
        return porc_atendidas, porc_sin_atender

    def calcular_mejora(porc_1, porc_2):
        return abs(porc_1 - porc_2)    

    def simular(self):
        directorio_grafico = "imagenes/grafico.png"
        prom_solicitudesAtendidas, prom_solicitudesSinAtender = self.procesar()

        porc_atendidas, porc_sin_atender = self.calcular_porcentajes(prom_solicitudesAtendidas, prom_solicitudesSinAtender)        
  
        self.armar_grafico(directorio_grafico, porc_atendidas,porc_sin_atender)

        print('Promedio Solicitudes atendidas: {} ({:.2f}%) '.format(str(prom_solicitudesAtendidas), porc_atendidas))
        print('Promedio Solicitudes NO atendidas: {} ({:.2f}%)'.format(str(prom_solicitudesSinAtender), porc_sin_atender ))
        print('---------------------------------------------------------------')
    
    def armar_grafico(self,directorio_grafico, porc_atendidas, porc_sin_atender):
        labels = 'Prom. Solicitudes atendidas', 'Prom. Solicitudes NO atendidas'
        sizes = [porc_atendidas, porc_sin_atender]
        colors = ['yellowgreen', 'lightcoral']
        explode = (0.1, 0)
        patches, texts = plt.pie(sizes, explode=explode, labels=labels, colors=colors, shadow=True, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

        #return scipy.misc.imsave(directorio_imagen_final, self.imagen)

    def generarPedidos(self,pedidos):
        cantPedidosM4 = np.random.poisson(20)
        cantPedidosM6 = np.random.poisson(10)

        #Armo una lista con elemntos M4 y M6
        for _ in range(cantPedidosM4):
            pedidos.append('M4')
        for _ in range(cantPedidosM6):    
            pedidos.append('M6')

        #Desordeno lista para no atender siempre las M4 primero
        np.random.shuffle(pedidos)    
 
    def procesarPedido(self,dia,item,var,pedidos):
        tiempoEspera = 0
        if (item == 'M4'):                
            if (var.stockM4 > 0):
                var.stockM4 -= 1
                #Esperar tiempo de Operador. se resta al tiempo disponible                    
                tiempoEspera = np.random.exponential(scale=var.velOperM4)         
                var.mesasConstruidasM4[dia] += 1 
                var.solicitudesAtendidas += 1
                pedidos.remove(item);
            else:                        
                var.solicitudesSinAtender +=1

        if (item == 'M6'):                
            if (var.stockM6 > 0):
                var.stockM6 -= 1
                #Esperar tiempo de Operador. se resta al tiempo disponible                    
                tiempoEspera = np.random.exponential(scale=var.velOperM6)                                
                var.mesasConstruidasM6[dia] += 1 
                var.solicitudesAtendidas += 1
                pedidos.remove(item);
            else:                        
                var.solicitudesSinAtender +=1

        var.minutosRestantes -= tiempoEspera
        var.tiemposOperarios[dia] += tiempoEspera
    
    def obtenerParametros(self):
        variable = Variable()
        variable.MES = int(self.formulario.lineEdit_exp.text())
        variable.DIAS = int(self.formulario.lineEdit_dias.text())
        variable.incrementoStockM4 = int(self.formulario.lineEdit_incrementoM4.text())
        variable.incrementoStockM6 = int(self.formulario.lineEdit_incrementoM6.text())
        variable.velOperM4 = int(self.formulario.lineEdit_velOperM4.text())
        variable.velOperM6 = int(self.formulario.lineEdit_velOperM6.text())
        variable.cantDiasProduccion = int(self.formulario.lineEdit_diasProd.text())
        return variable
        
    def procesar(self):
        pedidos = []            
        var = self.obtenerParametros()

        for mes in range(var.MES):            
            var.solicitudesSinAtender=0
            var.solicitudesAtendidas=0

            for dia in range(var.DIAS):                
                var.minutosRestantes = var.minutosXdia
                var.mesasConstruidasM4.append(0)
                var.mesasConstruidasM6.append(0)
                var.tiemposOperarios.append(0)
            

                #Incremento el stock los promeros N dia de cada mes
                if (dia <= var.cantDiasProduccion):
                    var.stockM4 += var.incrementoStockM4
                    var.stockM6 += var.incrementoStockM6

                self.generarPedidos(pedidos)

                #Recorro la lista de solicitudes
                for item in pedidos:   
                    if (var.minutosRestantes > 0):
                        self.procesarPedido(dia,item,var,pedidos)
                    else: 
                        var.solicitudesSinAtender +=1

            var.solicitudesAtendidasXMes.append(var.solicitudesAtendidas)
            var.solicitudesSinAtenderXMes.append(var.solicitudesSinAtender)

        promedioSolicitudesAtendidas = int(np.mean(var.solicitudesAtendidasXMes))
        promedioSolicitudesSinAtender = int(np.mean(var.solicitudesSinAtenderXMes))
        
        return promedioSolicitudesAtendidas, promedioSolicitudesSinAtender                
        
def main():
    app = QApplication(sys.argv)  
    formulario = Formulario()  
    formulario.show()  
    app.exec_()     

if __name__ == '__main__':  
    main()
