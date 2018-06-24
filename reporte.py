# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reporte.ui'
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
        self.plainTextEditReporte = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEditReporte.setGeometry(QtCore.QRect(20, 30, 561, 391))
        self.plainTextEditReporte.setObjectName("plainTextEditReporte")
        self.toolBox.addItem(self.toolBoxPage1, "")
        self.toolBoxPage2 = QtWidgets.QWidget()
        self.toolBoxPage2.setGeometry(QtCore.QRect(0, 0, 100, 30))
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
        self.groupBox.setTitle(_translate("MainWindow", "Reporte"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

