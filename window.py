# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 489)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 631, 501))
        self.toolBox.setObjectName("toolBox")
        self.toolBoxPage1 = QtWidgets.QWidget()
        self.toolBoxPage1.setGeometry(QtCore.QRect(0, 0, 631, 447))
        self.toolBoxPage1.setObjectName("toolBoxPage1")
        self.groupBox = QtWidgets.QGroupBox(self.toolBoxPage1)
        self.groupBox.setGeometry(QtCore.QRect(20, 0, 601, 441))
        self.groupBox.setObjectName("groupBox")
        self.label_0 = QtWidgets.QLabel(self.groupBox)
        self.label_0.setGeometry(QtCore.QRect(10, 40, 279, 17))
        self.label_0.setObjectName("label_0")
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(10, 80, 251, 17))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 191, 17))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 311, 17))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 331, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 311, 17))
        self.label_4.setObjectName("label_4")
        self.line_1 = QtWidgets.QFrame(self.groupBox)
        self.line_1.setGeometry(QtCore.QRect(0, 20, 531, 20))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(0, 60, 531, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 260, 311, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 140, 301, 17))
        self.label_7.setObjectName("label_7")
        self.lineEditExp = QtWidgets.QSpinBox(self.groupBox)
        self.lineEditExp.setGeometry(QtCore.QRect(410, 80, 111, 26))
        self.lineEditExp.setObjectName("lineEditExp")
        self.lineEditDias = QtWidgets.QSpinBox(self.groupBox)
        self.lineEditDias.setGeometry(QtCore.QRect(410, 110, 111, 26))
        self.lineEditDias.setObjectName("lineEditDias")
        self.lineEditIncrementoM4 = QtWidgets.QSpinBox(self.groupBox)
        self.lineEditIncrementoM4.setGeometry(QtCore.QRect(410, 170, 111, 26))
        self.lineEditIncrementoM4.setObjectName("lineEditIncrementoM4")
        self.lineEditIncrementoM6 = QtWidgets.QSpinBox(self.groupBox)
        self.lineEditIncrementoM6.setGeometry(QtCore.QRect(410, 200, 111, 26))
        self.lineEditIncrementoM6.setObjectName("lineEditIncrementoM6")
        self.lineEditVelOperM4 = QtWidgets.QSpinBox(self.groupBox)
        self.lineEditVelOperM4.setGeometry(QtCore.QRect(410, 230, 111, 26))
        self.lineEditVelOperM4.setObjectName("lineEditVelOperM4")
        self.lineEditVelOperM6 = QtWidgets.QSpinBox(self.groupBox)
        self.lineEditVelOperM6.setGeometry(QtCore.QRect(410, 260, 111, 26))
        self.lineEditVelOperM6.setObjectName("lineEditVelOperM6")
        self.lineEditDiasProd = QtWidgets.QSpinBox(self.groupBox)
        self.lineEditDiasProd.setGeometry(QtCore.QRect(410, 140, 111, 26))
        self.lineEditDiasProd.setObjectName("lineEditDiasProd")
        self.btnSimulacion = QtWidgets.QPushButton(self.groupBox)
        self.btnSimulacion.setGeometry(QtCore.QRect(10, 320, 261, 31))
        self.btnSimulacion.setObjectName("btnSimulacion")
        self.lineEditDiferencia = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditDiferencia.setEnabled(True)
        self.lineEditDiferencia.setGeometry(QtCore.QRect(410, 320, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditDiferencia.setFont(font)
        self.lineEditDiferencia.setAcceptDrops(True)
        self.lineEditDiferencia.setReadOnly(True)
        self.lineEditDiferencia.setObjectName("lineEditDiferencia")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(290, 326, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btnGraficoDePuntos = QtWidgets.QPushButton(self.groupBox)
        self.btnGraficoDePuntos.setGeometry(QtCore.QRect(10, 360, 261, 31))
        self.btnGraficoDePuntos.setObjectName("btnGraficoDePuntos")
        self.btnGraficoDeBarras = QtWidgets.QPushButton(self.groupBox)
        self.btnGraficoDeBarras.setGeometry(QtCore.QRect(10, 400, 261, 31))
        self.btnGraficoDeBarras.setObjectName("btnGraficoDeBarras")
        self.btnReporte = QtWidgets.QPushButton(self.groupBox)
        self.btnReporte.setGeometry(QtCore.QRect(290, 400, 231, 31))
        self.btnReporte.setObjectName("btnReporte")
        self.line_3 = QtWidgets.QFrame(self.toolBoxPage1)
        self.line_3.setGeometry(QtCore.QRect(30, 300, 521, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.toolBox.addItem(self.toolBoxPage1, "")
        self.toolBoxPage2 = QtWidgets.QWidget()
        self.toolBoxPage2.setGeometry(QtCore.QRect(0, 0, 631, 447))
        self.toolBoxPage2.setObjectName("toolBoxPage2")
        self.toolBox.addItem(self.toolBoxPage2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tp Final Modelos y Simulación"))
        self.groupBox.setTitle(_translate("MainWindow", "Parámetros de simulación"))
        self.label_0.setText(_translate("MainWindow", "Ingrese los siguientes datos para simular:"))
        self.label_1.setText(_translate("MainWindow", "Cantidad de meses a simular:"))
        self.label_2.setText(_translate("MainWindow", "Días x mes:"))
        self.label_5.setText(_translate("MainWindow", "Vel. atención operario M4 (minutos):"))
        self.label_3.setText(_translate("MainWindow", "Incremento de stock M4 (cantidad de partes):"))
        self.label_4.setText(_translate("MainWindow", "Incremento de stock M6 (cantidad de partes):"))
        self.label_6.setText(_translate("MainWindow", "Vel. atención operario M6 (minutos):"))
        self.label_7.setText(_translate("MainWindow", "Cantidad de días de producción por mes:"))
        self.btnSimulacion.setText(_translate("MainWindow", "Simular"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">DIFERENCIA:</span></p></body></html>"))
        self.btnGraficoDePuntos.setText(_translate("MainWindow", "Gráfico de Puntos"))
        self.btnGraficoDeBarras.setText(_translate("MainWindow", "Gráfico de Barras"))
        self.btnReporte.setText(_translate("MainWindow", "Ver Reporte"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

