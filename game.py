import PyQt6.QtWidgets as qtw
import PyQt6.QtGui as qtg

#Game window class 
class game(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #Set size, title, and other properties
        self.setGeometry(0, 0, 500, 600)
        self.setWindowTitle("Hackman!")
        self.setWindowIcon(qtg.QIcon("assets/letter-h.png"))
        self.setLayout(qtw.QGridLayout())
        self.setStyleSheet("background-color: black;")

        self.show()

    