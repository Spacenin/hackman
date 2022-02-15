import PyQt6.QtWidgets as qtw 
import window
import getWord

word = getWord.getWord()
print(word)

def start(app):
    #Start up main window
    hackGame = window.window(word)

    app.exec()

def checkLetter(guessedSoFar, letter):
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