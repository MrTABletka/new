import sys
from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QPushButton


class RandomFlag(QWidget):
    def __init__(self, x, y):
        super().__init__()
        self.initUI()
        self.x = x
        self.y = y
        self.num = 1

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Рисование')
        self.button = QPushButton(self)
        self.button.setGeometry(20, 20, 100, 50)
        self.button.clicked.connect(self.a)


    def a(self):
        self.num, bool = QInputDialog.getInt(self, "Введите количество цветов флага", "Сколько цветов?", 3, 1, 10, 1)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        for i in range(self.num):
            qp.setBrush(QColor(randrange(1, 255, 1), randrange(1, 255, 1), randrange(1, 255, 1)))
            qp.drawRect(50, 100 + i * self.y, self.x, self.y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomFlag(100, 50)
    ex.show()
    sys.exit(app.exec())