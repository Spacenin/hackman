import PyQt6.QtWidgets as qtw
import getWord
import game

def main():
    print("Working!")

    #Set up qt application
    app = qtw.QApplication([])

    #Start up game window within application
    myGame = game.game()
    app.exec()

if __name__ == "__main__":
    main()