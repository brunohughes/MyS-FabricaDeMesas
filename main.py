#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib.pyplot as plt
from Variable import Variable
from window import Ui_MainWindow
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
    
class Formulario(QMainWindow):


    #Constructor de la clase
    def __init__(self):
        #Inicio el objeto QMainwindow
        QMainWindow.__init__(self)
        self.formulario = Ui_MainWindow()
        self.formulario.setupUi(self)

        #seteamos las variables iniciales
        self.iniciarVariables()
        
        #seteamos los eventos        
        self.formulario.btnSimulacion.clicked.connect(self.simular)
        self.formulario.btnGraficoDePuntos.clicked.connect(self.armarGraficoPuntos)
        self.formulario.btnGraficoDeBarras.clicked.connect(self.armarGraficoBarras)

    def iniciarVariables(self):
        self.formulario.lineEditExp.setValue(1)
        self.formulario.lineEditDias.setValue(20)
        self.formulario.lineEditIncrementoM4.setValue(50)
        self.formulario.lineEditIncrementoM6.setValue(30)
        self.formulario.lineEditVelOperM4.setValue(5)
        self.formulario.lineEditVelOperM6.setValue(10)
        self.formulario.lineEditDiasProd.setValue(10)

    def calcularPorcentajes(self, solicitudesAtendidas, solicitudesSinAtender):
        total = solicitudesAtendidas + solicitudesSinAtender
        porcAtendidas = ( solicitudesAtendidas * 100 ) / total
        porcSinAtender = ( solicitudesSinAtender * 100) / total
        return porcAtendidas, porcSinAtender

    def calcularMejora(self,porc1, porc2):
        return abs(porc1 - porc2)    

    def simular(self):
        print('---------------------------------------------------------------')
        promSolicitudesAtendidas, promSolicitudesSinAtender = self.procesar()        
        porcAtendidas, porcSinAtender = self.calcularPorcentajes(promSolicitudesAtendidas, promSolicitudesSinAtender)        
        listaPorcAtendidas.append(porcAtendidas)                      
        cantEjecuciones = len(listaPorcAtendidas)
        print('Promedio Solicitudes atendidas: {} ({:.2f}%) '.format(str(promSolicitudesAtendidas), porcAtendidas))
        print('Promedio Solicitudes NO atendidas: {} ({:.2f}%)'.format(str(promSolicitudesSinAtender), porcSinAtender ))        

        if cantEjecuciones > 1:
            print('Ejecuciones:' + str(cantEjecuciones))
            mejora=self.calcularMejora(listaPorcAtendidas[cantEjecuciones -2], listaPorcAtendidas[cantEjecuciones -1])
            print('Mejora: {:.2f}%'.format(mejora))

            self.formulario.lineEditMejora.setText('{:.2f}%'.format(mejora))            
            if mejora > 15:                
                self.formulario.lineEditMejora.setStyleSheet('QLineEdit { background-color: #7CFC00}')
            else:
                self.formulario.lineEditMejora.setStyleSheet('QLineEdit { background-color: #B22222}')

        self.armarGrafico(cantEjecuciones,porcAtendidas,porcSinAtender)
        
    def armarGrafico(self,nroEjecucion, porcAtendidas, porcSinAtender):

        labels = ['Prom. Solicitudes atendidas', 'Prom. Solicitudes NO atendidas']
        porcAtendidasI=int(porcAtendidas)
        porcSinAtenderI = int(porcSinAtender)
        sizes = [porcAtendidasI, porcSinAtenderI]        
        colors = ['yellowgreen', 'lightcoral']
        explode = (0.1, 0)
        plt.figure()
        plt.pie(sizes, explode=explode, colors=colors, autopct='%.2f%%', shadow=True, startangle=90)
        plt.legend(labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.gcf().canvas.set_window_title('Ejecucion nro {0}'.format(nroEjecucion))        
        plt.show()

    def armarGraficoPuntos(self):
        plt.figure()
        plt.ylabel('Porcentaje Solicitudes Atendidas')
        plt.xlabel('Ejecucion Nro')
        plt.gcf().canvas.set_window_title('Solicitudes atendidas en cada ejecucion')        

        cantEjec= len(listaPorcAtendidas) + 1
        indiceEjec = np.arange(1,cantEjec) 

        plt.axis([0, cantEjec + 2, 0, 100])
        plt.plot(indiceEjec, listaPorcAtendidas,'ro')        
        plt.show()

    def armarGraficoBarras(self):

        fig, ax = plt.subplots()
        index = np.arange(len(listaPorcAtendidas))        
        bar_width = 0.35
        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        ax.bar(index, listaPorcAtendidas, bar_width,
                alpha=opacity, color='b',
                yerr=index, error_kw=error_config,
                label='Solicitudes atendidas')
        
        ax.set_xlabel('Ejecuciones')
        ax.set_ylabel('Porcentaje')
        ax.set_title('Solicitudes atendidas en cada ejecucion')
        ax.set_xticklabels((''))
        ax.legend()

        fig.tight_layout()
        plt.show()

    def generarPedidos(self,pedidos):
        cantPedidosM4 = np.random.poisson(30)
        cantPedidosM6 = np.random.poisson(25)

        #Armo una lista con elemntos M4 y M6
        for _ in range(cantPedidosM4):
            pedidos.append('M4')
        for _ in range(cantPedidosM6):    
            pedidos.append('M6')

        #Desordeno lista para no atender siempre las M4 primero
        np.random.shuffle(pedidos)    
 
    def procesarPedido(self,dia,item,var,noAtendidos):
        tiempoEspera = 0
        if (item == 'M4'):                
            if (var.stockM4 > 0):
                var.stockM4 -= 1
                #Esperar tiempo de Operador. se resta al tiempo disponible                    
                tiempoEspera = np.random.exponential(scale=var.velOperM4)         
                var.mesasConstruidasM4[dia] += 1 
                var.solicitudesAtendidas += 1
            else:
                noAtendidos.append(item)    

        if (item == 'M6'):                
            if (var.stockM6 > 0):
                var.stockM6 -= 1
                #Esperar tiempo de Operador. se resta al tiempo disponible                    
                tiempoEspera = np.random.exponential(scale=var.velOperM6)                                
                var.mesasConstruidasM6[dia] += 1 
                var.solicitudesAtendidas += 1
            else:
                noAtendidos.append(item)  

        var.minutosRestantes -= tiempoEspera

    
    def obtenerParametros(self):
        variable = Variable()
        variable.MES = int(self.formulario.lineEditExp.text())
        variable.DIAS = int(self.formulario.lineEditDias.text())
        variable.incrementoStockM4 = int(self.formulario.lineEditIncrementoM4.text())
        variable.incrementoStockM6 = int(self.formulario.lineEditIncrementoM6.text())
        variable.velOperM4 = int(self.formulario.lineEditVelOperM4.text())
        variable.velOperM6 = int(self.formulario.lineEditVelOperM6.text())
        variable.cantDiasProduccion = int(self.formulario.lineEditDiasProd.text())
        return variable

        
    def procesar(self):
        pedidos = []                    
        noAtendidos = []                

        var = self.obtenerParametros()  

        for mes in range(var.MES):            
            var.solicitudesAtendidas=0            

            for dia in range(var.DIAS):
                noAtendidos = []                
                var.minutosRestantes = var.minutosXdia
                var.mesasConstruidasM4.append(0)
                var.mesasConstruidasM6.append(0)

                #Incremento el stock los promeros N dia de cada mes
                if (dia < var.cantDiasProduccion):
                    var.stockM4 += var.incrementoStockM4
                    var.stockM6 += var.incrementoStockM6

                self.generarPedidos(pedidos)

                #Recorro la lista de solicitudes
                for item in pedidos:   
                    if (var.minutosRestantes > 0):
                        self.procesarPedido(dia,item,var,noAtendidos)
                    else:
                        noAtendidos.append(item)    

                pedidos = noAtendidos
                
            var.solicitudesSinAtender= len(pedidos)
            var.solicitudesAtendidasXMes.append(var.solicitudesAtendidas)
            var.solicitudesSinAtenderXMes.append(var.solicitudesSinAtender)

        promedioSolicitudesAtendidas = int(np.mean(var.solicitudesAtendidasXMes))
        promedioSolicitudesSinAtender = int(np.mean(var.solicitudesSinAtenderXMes))
        
        return promedioSolicitudesAtendidas, promedioSolicitudesSinAtender                


        
def main():
    
    global listaPorcAtendidas
    listaPorcAtendidas = []
    
    app = QApplication(sys.argv)  
    formulario = Formulario()  
    formulario.show()  
    app.exec_()     

if __name__ == '__main__':  
    main()  
