#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib.pyplot as plt
from Variable import Variable
from window import Ui_MainWindow
from reporte import Ui_MainWindow as Ui_MainWindow1
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
    
class Reporte(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.reporte = Ui_MainWindow1()
        self.reporte.setupUi(self)
    
    def setearTexto(self,texto):
    	self.reporte.plainTextEditReporte.setPlainText(texto)    	

class Formulario(QMainWindow):

    #Constructor de la clase
    def __init__(self):
        #Inicio el objeto QMainwindow
        QMainWindow.__init__(self)
        self.formulario = Ui_MainWindow()
        self.formulario.setupUi(self)

        self.iniciarVariables()
        self.vaciarLog()

        self.reporte = Reporte()

        #seteamos los eventos        
        self.formulario.btnSimulacion.clicked.connect(self.simular)
        self.formulario.btnGraficoDePuntos.clicked.connect(self.armarGraficoPuntos)
        self.formulario.btnGraficoDeBarras.clicked.connect(self.armarGraficoBarras)
        self.formulario.btnReporte.clicked.connect(self.armarReporte)



    def armarReporte(self):
        file = open("log.txt", "r")
        self.reporte.setearTexto( file.read() )
        self.reporte.show()


    def iniciarVariables(self):
        self.formulario.lineEditExp.setValue(1)
        self.formulario.lineEditDias.setValue(20)
        self.formulario.lineEditIncrementoM4.setValue(50)
        self.formulario.lineEditIncrementoM6.setValue(30)
        self.formulario.lineEditVelOperM4.setValue(5)
        self.formulario.lineEditVelOperM6.setValue(10)
        self.formulario.lineEditDiasProd.setValue(10)
        self.formulario.lineEditCantidadM4.setValue(30)
        self.formulario.lineEditCantidadM6.setValue(25)



    def calcularPorcentajes(self, solicitudesAtendidas, solicitudesSinAtender):
        total = solicitudesAtendidas + solicitudesSinAtender
        porcAtendidas = ( solicitudesAtendidas * 100 ) / total
        porcSinAtender = ( solicitudesSinAtender * 100) / total
        return porcAtendidas, porcSinAtender
    
    def vaciarLog(self):
        open("log.txt", "w").close()

    def grabarLog(self,cantEjecuciones,var,promSolicitudesAtendidas, promSolicitudesSinAtender,diferencia):
        text_file = open("log.txt", "a")

        text = """
--- Reporte de simulación N° {} ---
        Parámetros utilizados:
        Meses: {}
        Días: {}
        Días de producción: {}
        Producción fija mensual M4: {}
        Producción fija mensual M6: {}
        Velocidad de atención M4 (min.): {}
        Velocidad de atención M6 (min.): {}
        Cantidad de pedidos M4: XXX
        Cantidad de pedidos M6: XXX
        ---
        Total de solicitudes: XXX
        Promedio de solicitudes atendidas x mes: {}
        Promedio de solicitudes sin atender x mes: {}
        Diferencia observada: {:.2f} %        
        """.format(cantEjecuciones,var.MES,var.DIAS,var.cantDiasProduccion,var.incrementoStockM4,var.incrementoStockM6,
        	var.velOperM4, var.velOperM6,promSolicitudesAtendidas, promSolicitudesSinAtender,diferencia)
        text_file.write(text)
        text_file.close()

    def simular(self):
        
        promSolicitudesAtendidas, promSolicitudesSinAtender, var = self.procesar()        
        porcAtendidas, porcSinAtender = self.calcularPorcentajes(promSolicitudesAtendidas, promSolicitudesSinAtender)        
        listaPorcAtendidas.append(porcAtendidas)                      
        cantEjecuciones = len(listaPorcAtendidas)
        diferencia=0
        print('---------------------------------------------------------------')
        print('Promedio Solicitudes atendidas: {} ({:.2f}%) '.format(str(promSolicitudesAtendidas), porcAtendidas))
        print('Promedio Solicitudes NO atendidas: {} ({:.2f}%)'.format(str(promSolicitudesSinAtender), porcSinAtender ))        

        if cantEjecuciones > 1:
            print('Ejecuciones:' + str(cantEjecuciones))
            diferencia = listaPorcAtendidas[cantEjecuciones -1] - listaPorcAtendidas[cantEjecuciones -2]
            print('Diferencia: {:.2f}%'.format(diferencia))

            self.formulario.lineEditDiferencia.setText('{:.2f}%'.format(diferencia))            
            if diferencia > 0:                
                self.formulario.lineEditDiferencia.setStyleSheet('QLineEdit { background-color: #7CFC00}')
            else:
                self.formulario.lineEditDiferencia.setStyleSheet('QLineEdit { background-color: #B22222}')


        self.grabarLog(cantEjecuciones,var,promSolicitudesAtendidas, promSolicitudesSinAtender,diferencia)
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

        labels = np.arange(1, len(listaPorcAtendidas) + 1) 
        index = np.arange(len(listaPorcAtendidas))        
        bar_width = 0.35
        opacity = 0.4
        error_config = {'ecolor': '0.3'}
        fig, ax = plt.subplots()

        rects= ax.bar(index, listaPorcAtendidas, bar_width,
                alpha=opacity, color='b',
                yerr=index, error_kw=error_config,
                label='Solicitudes atendidas')
        
        ax.set_xlabel('Ejecuciones')
        ax.set_ylabel('Porcentaje')
        ax.set_title('Solicitudes atendidas en cada ejecucion')
        ax.set_xticks(index)
        ax.set_xticklabels(labels)                
        ax.legend()

        i=0 
        for x in listaPorcAtendidas:
            ax.text(i - 0.15, x - 5, '{:.2f}%'.format(x), fontsize=10)
            i +=1

        fig.tight_layout()
        plt.show()


    def generarPedidos(self,pedidos,var):
        cantPedidosM4 = np.random.poisson(var.cantidadM4)
        cantPedidosM6 = np.random.poisson(var.cantidadM6)

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
        variable.cantidadM4 = int(self.formulario.lineEditCantidadM4.text())
        variable.cantidadM6 = int(self.formulario.lineEditCantidadM6.text())

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

                self.generarPedidos(pedidos,var)

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
        
        return promedioSolicitudesAtendidas, promedioSolicitudesSinAtender, var                


        
def main():
    
    global listaPorcAtendidas
    listaPorcAtendidas = []
    
    app = QApplication(sys.argv)  
    formulario = Formulario()  
    formulario.show()  
    app.exec_()     

if __name__ == '__main__':  
    main()  
