from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow
import sys

class VentanaPrincipal(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #seteamos las variables iniciales
        self.iniciarVariables()

        #seteamos los eventos        
        self.ui.btnSimulacion.clicked.connect(self.simular)


    def iniciarVariables(self):
        self.ui.lineEdit_exp.setText("1")
        self.ui.lineEdit_dias.setText("20")
        self.ui.lineEdit_incrementoM4.setText("50")
        self.ui.lineEdit_incrementoM6.setText("30")
        self.ui.lineEdit_velOperM4.setText("5")
        self.ui.lineEdit_velOperM6.setText("10")


    def simular(self):
        mje = "Iniciando simulación..."
        print(mje)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = VentanaPrincipal()
    MainWindow.show()
    sys.exit(app.exec_())

