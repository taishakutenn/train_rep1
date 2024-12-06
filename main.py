import sys
import random

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.circles = []

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.drawCircle.clicked.connect(self.draw_circle)

    def draw_circle(self):
        width = self.width()
        height = self.height()

        x = random.randint(0, width - 50)
        y = random.randint(0, height - 50)
        radius = random.randint(10, 50)

        self.circles.append((x, y, radius))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setBrush(QColor(255, 255, 51))

        for (x, y, radius) in self.circles:
            qp.drawEllipse(x, y, radius * 2, radius * 2)

        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
