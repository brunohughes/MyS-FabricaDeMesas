#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import simulacion
import Pedido
from window import Ui_MainWindow
<<<<<<< HEAD
#from PyQt5 import QtGui
#from PyQt5.QtWidgets import QApplication, QMainWindow
#from PyQt5 import uic
#from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
#from PyQt5.QtCore import pyqtSlot

#Clase heredada de QDialog
class Formulario(QtWidgets.QMainWindow):
    #Constructor de la clase
    def __init__(self):
        #Inicio el objeto QDialog
        QtWidgets.QMainWindow.__init__(self)
=======
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
>>>>>>> 9c3ab7f8fdb70e0b68431d268e4622e433d41b3c
        self.formulario = Ui_MainWindow()
        self.formulario.setupUi(self)

        #seteamos las variables iniciales
        self.iniciarVariables()
        #self.formulario.btnSimulacion.clicked.connect(self.iniciarVariables)
        #seteamos los eventos        
        self.formulario.btnSimulacion.clicked.connect(self.simular)

    def iniciarVariables(self):
        exp = self.formulario.lineEdit_exp.setText("1")
        dias = self.formulario.lineEdit_dias.setText("20")
        incM4 = self.formulario.lineEdit_incrementoM4.setText("50")
        incM6 = self.formulario.lineEdit_incrementoM6.setText("30")
        velM4 = self.formulario.lineEdit_velOperM4.setText("5")
        velM6 = self.formulario.lineEdit_velOperM6.setText("10")
        
       # sim=simulacion()
        #sim.exp=exp
       # sim.dias=dias
       # sim.incM4 =incM4
       # sim.incM6=incM6
       # sim.velM4=velM4
       # sim.velM6=velM6
        
        #mje= "dentro de iniciar variables1"
       # simulacion.procesar(self,exp,dias, incM4,incM6,velM4,velM6)
        #mje= "dentro de iniciar variables2"

    def simular(self):
        mje = "Iniciando simulacion..."
        try:
            mje="entré al try"
            simulacion.procesar(exp, dias, incM4, incM6, velM4, velM6)
        except:
            mje="entre a except"
            #QMessageBox.critical(self, 'Error','Lo sentimos. Surgio un error inesperado \n %s', QMessageBox.Ok)
            self.formulario.btnSimulacion.setEnabled(True)
        print(mje)
        
def main():
    app = QtWidgets.QApplication(sys.argv)  
    formulario = Formulario()  
    formulario.show()  
    app.exec_()     

if __name__ == '__main__':  
    main()
