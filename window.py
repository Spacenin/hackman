from socketserver import ThreadingUDPServer
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
import time
import numpy
import game

class window(qtw.QWidget):
    def __init__(self, word):
        self.word = word
        self.score = 0
        self.status = 0
        self.wordBonus = False
        super().__init__()

        #Setup fonts
        font = qtg.QFont()
        font.setFamilies(["MS Sans Serif"])
        font.setPointSize(9)
        fontBig = qtg.QFont()
        fontBig.setFamilies(["MS Sans Serif"])
        fontBig.setPointSize(10)
        fontSmaller = qtg.QFont()
        fontSmaller.setFamilies(["MS Sans Serif"])
        fontSmaller.setPointSize(5)
        fontBigger = qtg.QFont()
        fontBigger.setFamilies(["MS Sans Serif"])
        fontBigger.setPointSize(12)

        #Setup window
        self.setGeometry(0, 0, 439, 397)
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.setWindowTitle("hackman")
        self.setWindowIcon(qtg.QIcon("assets/letter-h.png"))

        #Hangman image
        self.imageSeen = qtw.QLabel(self)
        self.imageSeen.setGeometry(qtc.QRect(50, -50, 401, 361))
        self.imageSeen.setAutoFillBackground(False)
        self.imageSeen.setPixmap(qtg.QPixmap("assets/base.png"))
        self.imageSeen.setScaledContents(True)

        #Enter button
        self.wordButton = qtw.QPushButton("Guess full word", self)
        self.wordButton.clicked.connect(self.changeTextWord)
        self.wordButton.setGeometry(qtc.QRect(170, 350, 131, 24))
        self.wordButton.setFont(font)
        self.wordButton.setAutoFillBackground(False)
        self.wordButton.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                        "border: 2px solid white;\n"
                                        "border-radius: 5px;")

        #Text box to enter in
        self.enterLetter = qtw.QLineEdit(self)
        self.enterLetter.setPlaceholderText("Enter letter here")
        self.enterLetter.setEnabled(True)
        self.enterLetter.returnPressed.connect(self.checkLetter)
        self.enterLetter.setMaxLength(1)
        self.enterLetter.setGeometry(qtc.QRect(140, 290, 191, 41))
        self.enterLetter.setFont(fontBigger)
        self.enterLetter.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        self.enterLetter.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                        "border: 2px solid white;\n"
                                        "border-radius: 5px;\n"
                                        "")

        #Word label
        self.guessedLabel = qtw.QLabel("_" * len(word), self)
        self.guessedLabel.setGeometry(qtc.QRect(40, 240, 161, 31))
        self.guessedLabel.setFont(font)
        self.guessedLabel.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        self.guessedLabel.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                         "border: 2px solid white;\n"
                                         "border-radius: 5px;")
        
        #Word count label
        self.wordNumberLabel = qtw.QLabel("--" + str(len(word)) + " letter word--", self)
        self.wordNumberLabel.setGeometry(qtc.QRect(55, 210, 130, 20))
        self.wordNumberLabel.setFont(fontSmaller)
        self.wordNumberLabel.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        self.wordNumberLabel.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                            "border: 2px solid white;\n"
                                            "border-radius: 5px;")

        #Incorrect letters
        self.badLettersLabel = qtw.QLabel("Incorrect guesses:\n", self)
        self.badLettersLabel.setGeometry(qtc.QRect(290, 200, 121, 71))
        self.badLettersLabel.setFont(fontBig)
        self.badLettersLabel.setAlignment(qtc.Qt.AlignmentFlag.AlignLeading|qtc.Qt.AlignmentFlag.AlignLeft|qtc.Qt.AlignmentFlag.AlignTop)
        self.badLettersLabel.setWordWrap(True)
        self.badLettersLabel.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                            "border: 2px solid white;\n"
                                            "border-radius: 5px;")

        self.start = time.time()

        self.show()
    
    #Check letter entered
    def checkLetter(self):
        #Get letter entered
        letter = self.enterLetter.text()

        if letter == "":
            return

        guessed = self.guessedLabel.text()

        #Reset text box
        self.enterLetter.setText("")
        self.enterLetter.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

        #Check if it is right
        guessedCheck = game.checkLetter(guessed, letter)
        
        #If the check if unchanged, add to incorrect, otherwise add to correct
        if guessedCheck == guessed:
            badLetters = self.badLettersLabel.text()
            badLetters += (letter + ", ")
            self.badLettersLabel.setText(badLetters)

            self.status += 1
        
        else:
            self.guessedLabel.setText(guessedCheck)

        self.checkImage()
        self.checkWon()
    
    #Change text box to accept full words
    def changeTextWord(self):
        self.enterLetter.setMaxLength(100)
        self.enterLetter.setPlaceholderText("Enter the word")
        self.enterLetter.returnPressed.disconnect()
        self.enterLetter.returnPressed.connect(self.checkWord)

        self.wordButton.setText("Guess letters")
        self.wordButton.clicked.disconnect()
        self.wordButton.clicked.connect(self.changeTextLetter)

    #Change text box back to letters
    def changeTextLetter(self):
        self.enterLetter.setMaxLength(1)
        self.enterLetter.setPlaceholderText("Enter letter here")
        self.enterLetter.returnPressed.disconnect()
        self.enterLetter.returnPressed.connect(self.checkLetter)

        self.wordButton.setText("Guess full word")
        self.wordButton.clicked.disconnect()
        self.wordButton.clicked.connect(self.changeTextWord)
    
    #Check if full word is right
    def checkWord(self):
        #Get word in text box
        guessed = self.enterLetter.text()

        if guessed == self.word:
            self.guessedLabel.setText(guessed)

            self.wordBonus = True

            self.checkWon()

        else:
            self.status = 5

            self.checkImage()
    
    #Check if image needs to change
    def checkImage(self):
        #Check status and set image accordingly
        if self.status == 0:
            pass
        elif self.status == 1:
            self.imageSeen.setPixmap(qtg.QPixmap("assets/one.png"))
        elif self.status == 2:
            self.imageSeen.setPixmap(qtg.QPixmap("assets/two.png"))
        elif self.status == 3:
            self.imageSeen.setPixmap(qtg.QPixmap("assets/three.png"))
        elif self.status == 4:
            self.imageSeen.setPixmap(qtg.QPixmap("assets/four.png"))
        elif self.status == 5:
            self.imageSeen.setPixmap(qtg.QPixmap("assets/five.png"))

            self.enterLetter.setReadOnly(True)

            #Display game over screen
            self.endLabel = qtw.QLabel("--GAME OVER--\nThe word was: {}".format(self.word))
            self.endLabel.setGeometry(qtc.QRect(120, 140, 221, 221))
            self.endLabel.setWindowTitle("LOSER")
            self.endLabel.setWindowIcon(qtg.QIcon("assets/letter-h.png"))
            fontBigger = qtg.QFont()
            fontBigger.setFamilies(["MS Sans Serif"])
            fontBigger.setPointSize(12)
            self.endLabel.setFont(fontBigger)
            self.endLabel.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
            self.endLabel.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                        "border: 2px solid white;\n"
                                        "border-radius: 5px;")
            self.endLabel.show()
    
    #Check the win condition
    def checkWon(self):
        guessedCheck = self.guessedLabel.text()

        #If user has guessed the word, end program
        if guessedCheck == self.word:
            self.enterLetter.setReadOnly(True)

            #Calculate score
            end = time.time()
            self.score = round(numpy.reciprocal(end - self.start) * 1000)

            if self.wordBonus:
                self.score += 100

            #Display score
            self.scoreLabel = qtw.QLabel("--YOU WON--\nYour score: {}".format(self.score))
            self.scoreLabel.setGeometry(qtc.QRect(120, 140, 221, 221))
            self.scoreLabel.setWindowTitle("WINNER")
            self.scoreLabel.setWindowIcon(qtg.QIcon("assets/letter-h.png"))
            fontBigger = qtg.QFont()
            fontBigger.setFamilies(["MS Sans Serif"])
            fontBigger.setPointSize(12)
            self.scoreLabel.setFont(fontBigger)
            self.scoreLabel.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
            self.scoreLabel.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                        "border: 2px solid white;\n"
                                        "border-radius: 5px;")
            self.scoreLabel.show()

    #Close all windows on close
    def closeEvent(self, event):
        try:
            self.scoreLabel.close()
        except AttributeError:
            pass

        try:
            self.endLabel.close()
        except AttributeError:
            pass