import sys
from os.path import exists

from PyQt5.QtWidgets import QApplication

import gui


app = QApplication(sys.argv)
signup = gui.SignUp()
signin = gui.SignIn()
nochrome = gui.NoChrome()

def chrome() -> bool:
        '''To check if Chrome is installed on the system'''
        return exists("C:\Program Files\Google\Chrome\Application\chrome.exe")


if __name__ == "__main__":

    if not chrome():
        nochrome.show()
    elif exists('user.txt'):
        signin.show()
    else:
        signup.show()


    app.exec()