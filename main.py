#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
#import tratamiento
from window import Ui_MainWindow
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
        self.formulario = Ui_MainWindow()
        self.formulario.setupUi(self)


        #seteamos las variables iniciales
        self.iniciarVariables()

        #seteamos los eventos        
        self.formulario.btnSimulacion.clicked.connect(self.simular)


    def iniciarVariables(self):
        self.formulario.lineEdit_exp.setText("1")
        self.formulario.lineEdit_dias.setText("20")
        self.formulario.lineEdit_incrementoM4.setText("50")
        self.formulario.lineEdit_incrementoM6.setText("30")
        self.formulario.lineEdit_velOperM4.setText("5")
        self.formulario.lineEdit_velOperM6.setText("10")



    def simular(self):
        mje = "Iniciando simulación..."
        print(mje)


        
def main():
    app = QtWidgets.QApplication(sys.argv)  
    formulario = Formulario()  
    formulario.show()  
    app.exec_()  

if __name__ == '__main__':  
    main()
