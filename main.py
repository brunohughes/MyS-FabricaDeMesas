#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
#import tratamiento
from window import Ui_MainWindow
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot

#Clase heredada de QDialog
class Formulario(QMainWindow):
    #Constructor de la clase
    def __init__(self):
        #Inicio el objeto QDialog
        QMainWindow.__init__(self)
        self.formulario = Ui_MainWindow()
        self.formulario.setupUi(self)
        #self.input1 = self.formulario.dato1.text()
        self.formulario.btnSimulacion.clicked.connect(self.preparar)
        #self.formulario.btnSimulacion()
        #QPushButton('PyQt5 button', self)
        #button.setToolTip('This is an example button')
        #button.clicked.connect(self.on_click)
        #self.formulario.btnSimulacion.clicked.connect(self)

        @pyqtSlot()
        def on_click(self):
            print('PyQt5 button click')
               
        def preparar(self):
            pass
        #    print(self.input1)
"""         self.input2 = self.formulario.dato2.text()
            self.input3 = self.formulario.dato3.text()
            self.input4 = self.formulario.dato4.text()
            self.input5 = self.formulario.dato5.text()
            self.input6 = self.formulario.dato6.text()
        

        vecindad = 0
        cant_vecinos = 0    
        ruta = self.directorio_imagen
        if self.formulario.btn1.isChecked():
            vecindad = 0
        elif self.formulario.btn2.isChecked():
            vecindad = 1
        if self.formulario.btn3.isChecked():
            cant_vecinos = 2
        elif self.formulario.btn4.isChecked():
            cant_vecinos = 4
        elif self.formulario.btn5.isChecked():
            cant_vecinos = 8
        try:
            self.imagen = tratamiento.Tratamiento(ruta)
        except:
            QtGui.QMessageBox.warning(self, 'Error','No te olvides de elegir una imagen \n %s', QtGui.QMessageBox.Ok)
        try:
            self.imagen.procesar(vecindad, cant_vecinos)
        except:
            QtGui.QMessageBox.critical(self, 'Error','Lo siento. Hay un error con los filtros \n %s', QtGui.QMessageBox.Ok)
        QtGui.QMessageBox.information(self,'Fin', 'Suavizado finalizado!', QtGui.QMessageBox.Ok)
        self.formulario.btnSuavizar.setEnabled(False)
        self.formulario.imagenResultado.setScaledContents(True)
        self.formulario.imagenResultado.setPixmap(QtGui.QPixmap(self.imagen.devolver_directorio()))
    

        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)
        self.formulario.btnImagen.clicked.connect(self.elegir_imagen)
        self.formulario.btnSimulacion.clicked.connect(self.preparar)
        self.formulario.btnImagen.setEnabled(True)
        self.formulario.btnSuavizar.setEnabled(False)
            
    def elegir_imagen(self):
        file_path = QFileDialog.getOpenFileName(self, 'Buscar imagen', '/', "Image file(*.png *.jpeg *.jpg)")
        self.formulario.imagenOriginal.setScaledContents(True)
        self.formulario.imagenOriginal.setPixmap(QtGui.QPixmap(file_path))
        self.directorio_imagen = file_path
        self.formulario.btnSuavizar.setEnabled(True)
"""
        
def main():
    app = QApplication(sys.argv)  
    formulario = Formulario()  
    formulario.show()  
    app.exec_()  

if __name__ == '__main__':  
    main()
