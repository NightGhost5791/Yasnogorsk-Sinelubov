import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Главное меню.ui', self)
        self.playbtn.clicked.connect(self.play)
        self.closebtn.clicked.connect(self.close)
        self.leadersbtn.clicked.connect(self.leaders)
        self.razrabibtn.clicked.connect(self.razrabi)

    def play(self):
        pass
    #Начало игры

    def close(self):
        self.close()

    def leaders(self):
        pass
    # Датабаза с лучшими игроками

    def razrabi(self):
        self.label.setText('by NightGhost5791')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())