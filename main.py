import PyQt6.QtWidgets as qtw
import getWord
import game
import window

def main():
    #Exit code constant that allows user to restart program
    EXIT_CODE_REBOOT = 618491
    exitCodeCurrent = EXIT_CODE_REBOOT

    while (exitCodeCurrent == EXIT_CODE_REBOOT):
        app = qtw.QApplication([])
        #Start up game window within application
        exitCodeCurrent = game.game().start(app)

        app = None

if __name__ == "__main__":
    main()