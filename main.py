import PyQt6.QtWidgets as qtw
import getWord
import game
import window

def main():
    app = qtw.QApplication([])
    #Start up game window within application
    game.start(app)

if __name__ == "__main__":
    main()