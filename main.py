#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import simulacion
import Pedido
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

        #seteamos los eventos        
        self.formulario.btnSimulacion.clicked.connect(self.simular)

    def iniciarVariables(self):
        exp = self.formulario.lineEdit_exp.setText("1")
        dias = self.formulario.lineEdit_dias.setText("20")
        incM4 = self.formulario.lineEdit_incrementoM4.setText("50")
        incM6 = self.formulario.lineEdit_incrementoM6.setText("30")
        velM4 = self.formulario.lineEdit_velOperM4.setText("5")
        velM6 = self.formulario.lineEdit_velOperM6.setText("10")

    def simular(self):
        mje = "Iniciando simulacion..."
        try:
            simulacion.procesar(exp, dias, incM4, incM6, velM4, velM6)
        except:
            #QMessageBox.critical(self, 'Error','Lo sentimos. Surgio un error inesperado \n %s', QMessageBox.Ok)
            self.formulario.btnSimulacion.setEnabled(True)
        print(mje)
        
def main():
    app = QApplication(sys.argv)  
    formulario = Formulario()  
    formulario.show()  
    app.exec_()  

if __name__ == '__main__':  
    main()
