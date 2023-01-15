import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora jalleriana')  # mudar o titulo da aplicacao
        self.setFixedSize(400, 600)  # deixa o tamanho fixo da janela
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 2)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
