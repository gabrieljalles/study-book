"""
PyQT é um toolkit desenvolvido em C++ utilizado por vários programas para criação de aplicações GUI (interface gráfica)
Também inclui diversas funcionalidades, como: acesso ao banco de dados, threads, comunicação de rede, etc...

pip install pyqt5
"""
# criando uma janela na tela -----------------------------------
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do botão')
        self.btn.setStyleSheet('font-size: 40px;')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.btn.clicked.connect(self.acao)

        self.setCentralWidget(self.cw)

    def acao(self):
        print('Alguma coisa')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()  # instanciando uma classe
    app.show()
    qt.exec_()
# ---------------------------------------------------------------
