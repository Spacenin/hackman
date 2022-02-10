import PyQt6.QtWidgets as qtw
import PyQt6.QtGui as qtg
import getWord

#Game window class 
class game(qtw.QWidget):
    def __init__(self):
        #Set up member variables
        self.status = -1
        self.word = getWord.getWord()

        super().__init__()

        #Set size, title, and other properties
        self.setGeometry(0, 0, 1000, 600)
        self.setWindowTitle("Hackman!")
        self.setWindowIcon(qtg.QIcon("assets/letter-h.png"))
        self.layout = qtw.QVBoxLayout()
        self.setStyleSheet("background-color: black;")

        self.draw()
    
    def draw(self):
        if self.status == -1:
            label = qtw.QLabel(self)
            pxmap = qtg.QPixmap("assets/base.png")
            label.setPixmap(pxmap)
            label.setMaximumHeight(pxmap.height())
            label.setMaximumWidth(pxmap.width())
            self.layout.addWidget(label)

        self.show()


    