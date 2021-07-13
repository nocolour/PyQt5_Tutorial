import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    f = QFont()
    f.setFamily("Arial")
    f.setPointSize(16)
    b.setText("Hello World")
    w.setGeometry(100, 100, 200, 50)
    b.setFont(f)
    b.move(50, 20)
    w.setWindowTitle("PyQt5 Tutorial")
    w.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    window()
