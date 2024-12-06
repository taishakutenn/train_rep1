import sys
import random

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.circles = []

    def initUI(self):
        self.setWindowTitle("Случайные круги")
        self.resize(900, 900)
        self.draw_circle = QPushButton("Click", self)
        self.draw_circle.clicked.connect(self.draw_circle_met)

    def draw_circle_met(self):
        x = random.randint(0, 900 - 50)
        y = random.randint(0, 900 - 50)
        radius = random.randint(10, 50)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        self.circles.append((x, y, radius, QColor(r, g, b)))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)

        for (x, y, radius, color) in self.circles:
            qp.setBrush(color)
            qp.drawEllipse(x, y, radius * 2, radius * 2)

        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
