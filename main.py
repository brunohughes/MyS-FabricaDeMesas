#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import simulacion
import Pedido
import numpy as np
import matplotlib.pyplot as plt
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
        self.formulario.lineEdit_velOperM4.setText("5")
        self.formulario.lineEdit_velOperM6.setText("10")
        self.formulario.lineEdit_diasProd.setText("10")
    
    def calcular_porcentajes(self, solicitudesAtendidas, solicitudesSinAtender):
        total = solicitudesAtendidas + solicitudesSinAtender
        porc_atendidas = ( solicitudesAtendidas * 100 ) / total
        porc_sin_atender = ( solicitudesSinAtender * 100) / total
        return porc_atendidas, porc_sin_atender

    def calcular_mejora(porc_1, porc_2):
        return abs(porc_1 - porc_2)    

    def simular(self):
        solicitudesAtendidas, solicitudesSinAtender = self.procesar()

        porc_atendidas_5030, porc_sin_atender = self.calcular_porcentajes(solicitudesAtendidas, solicitudesSinAtender)
        #print('PARAMETRO Minutos totales de trabajo diario: ' + str(minutosXdia))
        print('Solicitudes atendidas: {} ({:.2f}%) '.format(str(solicitudesAtendidas), porc_atendidas_5030))
        print('Solicitudes NO atendidas: {} ({:.2f}%)'.format(str(solicitudesSinAtender), porc_sin_atender ))
                

    def procesar(self):
        pedidos = []
        stockM4=0
        stockM6=0
        pedidosAtendidos=0
        pedidosNOatendidos=0
        minutosRestantes=0 #Contador de minutos restantes en un dia 
        minutosXdia = 60*8
        cantDiasProduccion = 10
        solicitudesSinAtender=0
        solicitudesAtendidas=0
        mesasConstruidasM4=[]
        mesasConstruidasM6=[]
        tiemposOperarios=[]

        EXP = int(self.formulario.lineEdit_exp.text())
        DIAS = int(self.formulario.lineEdit_dias.text())
        incrementoStockM4 = int(self.formulario.lineEdit_incrementoM4.text())
        incrementoStockM6 = int(self.formulario.lineEdit_incrementoM6.text())
        velOperM4 = int(self.formulario.lineEdit_velOperM4.text())
        velOperM6 = int(self.formulario.lineEdit_velOperM6.text())
        diasProd = int(self.formulario.lineEdit_diasProd.text())
      
        for i in range(EXP):
            for dia in range(DIAS):
                minutosRestantes = minutosXdia
                mesasConstruidasM4.append(0)
                mesasConstruidasM6.append(0)
                tiemposOperarios.append(0)

                #Incremento el stock los promeros N dias
                if (dia <= cantDiasProduccion):
                    stockM4 +=incrementoStockM4
                    stockM6 +=incrementoStockM6

                cantPedidosM4 = np.random.poisson(8)
                cantPedidosM6 = np.random.poisson(4)

                #Armo una lista con elemntos M4 y M6
                for _ in range(cantPedidosM4):
                    pedidos.append('M4')
                for _ in range(cantPedidosM6):    
                    pedidos.append('M6')


                #Desordeno lista para no atender siempre las M4 primero
                np.random.shuffle(pedidos)    


                #Recorro la lista de solicitudes
                for item in pedidos:   
                    if (minutosRestantes > 0):
                        if (item == 'M4'):                
                            if (stockM4 > 0):
                                #Decrementar stock M4
                                stockM4 -= 1

                                #Esperar tiempo de Operador. se resta al tiempo disponible                    
                                tiempoEspera = np.random.exponential(scale=velOperM4)
                                minutosRestantes -= tiempoEspera

                                #Contabilizar tiempo de Operarios (espera)
                                tiemposOperarios[dia] += tiempoEspera

                                #contabilizar solicitudes atendidas (por dia)
                                solicitudesAtendidas += 1

                                #Incrementamos contador de mesas contruidas M4                
                                mesasConstruidasM4[dia] += 1 

                                #Resto al tiempo restante la velocidad de extraccion M4
                                #minutosRestantes -= item.velocidad

                            else:                        
                                solicitudesSinAtender +=1

                        if (item == 'M6'):                
                            if (stockM6 > 0):
                                #Decrementar stock M4
                                stockM6 -= 1

                                #Esperar tiempo de Operador. se resta al tiempo disponible                    
                                tiempoEspera = np.random.exponential(scale=velOperM6)
                                minutosRestantes -= tiempoEspera

                                #Contabilizar tiempo de Operarios (espera)
                                tiemposOperarios[dia] += tiempoEspera

                                #contabilizar solicitudes atendidas (por dia)
                                solicitudesAtendidas += 1

                                #Incrementamos contador de mesas contruidas M6                
                                mesasConstruidasM6[dia] += 1 

                                #Resto al tiempo restante la velocidad de extraccion M6
                                #minutosRestantes -= item.velocidad

                            else:                        
                                solicitudesSinAtender +=1


                    else: 
                        #Se terminaron los minutos del dia
                        #contabilizar solicitudes NO atendidas (por dia)
                        solicitudesSinAtender +=1
        return solicitudesAtendidas, solicitudesSinAtender

def main():
    app = QApplication(sys.argv)  
    formulario = Formulario()  
    formulario.show()  
    app.exec_()     

if __name__ == '__main__':  
    main()
