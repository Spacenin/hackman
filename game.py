import PyQt6.QtWidgets as qtw 
import window
import getWord

class game:
    word = ""

    def start(self, app):
        #Start up main window and get word
        self.word = getWord.getWord()
        #print(self.word)
        hackGame = window.window(self.word)

        return(app.exec())

    def checkLetter(guessedSoFar, letter, word):
        #Create list from guessed letters
        listed = list(guessedSoFar)

        #Check if the letter is in the word
        for i in range(len(word)):
            if word[i] == letter:
                listed[i] = letter

        guessedSoFar = ""

        #Return as string
        for i in range(len(listed)):
            guessedSoFar += listed[i]

        return(guessedSoFar)