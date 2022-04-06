import sys

from PyQt5.QtWidgets import QApplication

import gui


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # window = gui.Window()
    # window.showMaximized()
    
    # window = gui.SignUp()
    # window.show()

    # window = gui.SignIn()
    # window.show()

    # window = gui.NoDB()
    # window.show()

    # window = gui.NoChrome()
    # window.show()

    # window = gui.InvalidEmail()
    # window.show()

    app.exec()