from PyQt5.QtWidgets import QWidget, QMainWindow, \
    QGridLayout, QVBoxLayout, QHBoxLayout, \
        QLabel, QPushButton, QSpacerItem, QTextEdit, QGroupBox, \
            QSizePolicy, QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QColor, QPixmap
from PyQt5.QtCore import Qt, QSize

from vars import *



class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QIcon(WINDOW_ICON))
        self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setStyleSheet(WINDOW_STYLE)

        self.win_lo = QHBoxLayout()
        self.win = QWidget()

        self.win.setLayout(self.win_lo)
        self.win_lo.setSpacing(0)
        self.win_lo.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(self.win)
        self.create_GUI()

    def create_GUI(self):
        self.create_sidebar()
        self.create_container()
        self.create_download()
        self.create_update()
        self.create_vspacer()
        self.create_boxes()

    def create_sidebar(self):
        self.sidebar = QWidget()
        self.sidebar.setStyleSheet(SIDEBAR_STYLE)
        self.sidebar.setMaximumWidth(100)
        self.sidebar_lo = QVBoxLayout()
        self.sidebar_lo.setContentsMargins(10, 10, 10, 10)
        self.sidebar_lo.setSpacing(20)
        self.sidebar.setLayout(self.sidebar_lo)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(5)
        shadow.setBlurRadius(10)
        self.sidebar.setGraphicsEffect(shadow)
        self.win_lo.addWidget(self.sidebar)

    def create_download(self):
        self.download_btn = QPushButton()
        self.download_btn.setStyleSheet(BTN_STYLE)
        self.download_btn.setFixedHeight(80)
        self.download_btn.setIcon(QIcon(DOWNLOAD_ICON))
        self.download_btn.setIconSize(QSize(50, 50))
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.download_btn.setGraphicsEffect(shadow)
        self.sidebar_lo.addWidget(self.download_btn)

    def create_update(self):
        self.update_btn = QPushButton()
        self.update_btn.setStyleSheet(BTN_STYLE)
        self.update_btn.setFixedHeight(80)
        self.update_btn.setIcon(QIcon(UPDATE_ICON))
        self.update_btn.setIconSize(QSize(50, 50))
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.update_btn.setGraphicsEffect(shadow)
        self.sidebar_lo.addWidget(self.update_btn)

    def create_vspacer(self):
        self.vspacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.sidebar_lo.addSpacerItem(self.vspacer)

    def create_container(self):
        self.container = QWidget()
        self.container.setStyleSheet(CONTAINER_STYLE)
        self.container_lo = QGridLayout()
        self.container_lo.setSpacing(10)
        self.container.setLayout(self.container_lo)
        self.win_lo.addWidget(self.container)

    def create_boxes(self):

        self.boxes = [QWidget() for i in range(6)]

        for box in self.boxes:
            box.setStyleSheet(BOX_STYLE)
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor('#111'))
            shadow.setOffset(2)
            shadow.setBlurRadius(10)
            box.setGraphicsEffect(shadow)

        self.container_lo.addWidget(self.boxes[0], 0, 0, 1, 1)
        self.container_lo.addWidget(self.boxes[1], 0, 1, 1, 1)
        self.container_lo.addWidget(self.boxes[2], 0, 2, 1, 2)
        self.container_lo.addWidget(self.boxes[3], 1, 0, 1, 4)
        self.container_lo.addWidget(self.boxes[4], 2, 0, 1, 3)
        self.container_lo.addWidget(self.boxes[5], 2, 3, 1, 1)


class SignUp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(SIGNUP_TITLE)
        self.setWindowIcon(QIcon(WINDOW_ICON))
        self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setStyleSheet(WINDOW_STYLE)

        self.win_lo = QVBoxLayout()
        self.win = QWidget()

        self.win.setLayout(self.win_lo)
        self.win_lo.setSpacing(10)
        self.win_lo.setContentsMargins(20, 20, 20, 20)
        self.win.setFixedSize(400, 500)
        self.win_lo.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.win)

        self.create_GUI()

    def create_GUI(self):
        self.create_logo()
        self.create_inputs()
        self.create_signup()

    def create_logo(self):
        self.logo_container = QLabel()
        self.logo = QPixmap(LOGO)
        self.logo = self.logo.scaledToHeight(50)
        self.logo_container.setPixmap(self.logo)
        self.logo_container.setAlignment(Qt.AlignCenter)
        self.win_lo.addWidget(self.logo_container)

    def create_inputs(self):
        self.username_lbl = QLabel('Username')
        self.username_lbl.setStyleSheet(LABEL_STYLE)
        self.username = QTextEdit()
        self.username.setFixedHeight(30)
        self.username.setStyleSheet(TEXTEDIT_STYLE)
        self.email_lbl = QLabel('Email')
        self.email_lbl.setStyleSheet(LABEL_STYLE)
        self.email = QTextEdit()
        self.email.setFixedHeight(30)
        self.email.setStyleSheet(TEXTEDIT_STYLE)
        self.password_lbl = QLabel('Password')
        self.password_lbl.setStyleSheet(LABEL_STYLE)
        self.password = QTextEdit()
        self.password.setFixedHeight(30)
        self.password.setStyleSheet(TEXTEDIT_STYLE)
        self.confirm_password_lbl = QLabel('Confirm Password')
        self.confirm_password_lbl.setStyleSheet(LABEL_STYLE)
        self.confirm_password = QTextEdit()
        self.confirm_password.setFixedHeight(30)
        self.confirm_password.setStyleSheet(TEXTEDIT_STYLE)

        self.win_lo.addWidget(self.username_lbl)
        self.win_lo.addWidget(self.username)
        self.win_lo.addWidget(self.email_lbl)
        self.win_lo.addWidget(self.email)
        self.win_lo.addWidget(self.password_lbl)
        self.win_lo.addWidget(self.password)
        self.win_lo.addWidget(self.confirm_password_lbl)
        self.win_lo.addWidget(self.confirm_password)

    def create_signup(self):
        self.signup_btn = QPushButton('SIGN UP')
        self.signup_btn.setStyleSheet(LONG_BTN_STYLE)
        self.signup_btn.setFixedSize(200, 50)
        self.win_lo.addWidget(self.signup_btn, alignment=Qt.AlignCenter)


class SignIn(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(SIGNIN_TITLE)
        self.setWindowIcon(QIcon(WINDOW_ICON))
        self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setStyleSheet(WINDOW_STYLE)

        self.win_lo = QVBoxLayout()
        self.win = QWidget()

        self.win.setLayout(self.win_lo)
        self.win_lo.setSpacing(10)
        self.win_lo.setContentsMargins(20, 20, 20, 20)
        self.win.setFixedSize(400, 300)
        self.win_lo.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.win)

        self.create_GUI()

    def create_GUI(self):
        self.create_logo()
        self.create_inputs()
        self.create_signin()

    def create_logo(self):
        self.logo_container = QLabel()
        self.logo = QPixmap(LOGO)
        self.logo = self.logo.scaledToHeight(50)
        self.logo_container.setPixmap(self.logo)
        self.logo_container.setAlignment(Qt.AlignCenter)
        self.win_lo.addWidget(self.logo_container)

    def create_inputs(self):
        self.username_lbl = QLabel('Username')
        self.username_lbl.setStyleSheet(LABEL_STYLE)
        self.username = QTextEdit()
        self.username.setFixedHeight(30)
        self.username.setStyleSheet(TEXTEDIT_STYLE)
        self.password_lbl = QLabel('Password')
        self.password_lbl.setStyleSheet(LABEL_STYLE)
        self.password = QTextEdit()
        self.password.setFixedHeight(30)
        self.password.setStyleSheet(TEXTEDIT_STYLE)
        
        self.win_lo.addWidget(self.username_lbl)
        self.win_lo.addWidget(self.username)
        self.win_lo.addWidget(self.password_lbl)
        self.win_lo.addWidget(self.password)

    def create_signin(self):
        self.signin_btn = QPushButton('SIGN IN')
        self.signin_btn.setStyleSheet(LONG_BTN_STYLE)
        self.signin_btn.setFixedSize(200, 50)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.signin_btn.setGraphicsEffect(shadow)
        self.win_lo.addWidget(self.signin_btn, alignment=Qt.AlignCenter)


class NoDB(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(NODB_TITLE)
        self.setWindowIcon(QIcon(WINDOW_ICON))
        self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setStyleSheet(WINDOW_STYLE)

        self.win_lo = QVBoxLayout()
        self.win = QWidget()

        self.win.setLayout(self.win_lo)
        self.win_lo.setSpacing(10)
        self.win_lo.setContentsMargins(20, 20, 20, 20)
        self.win.setFixedSize(400, 350)
        self.win_lo.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.win)

        self.create_GUI()

    def create_GUI(self):
        self.create_logo()
        self.create_msg()
        self.create_inputs()
        self.create_ok()

    def create_logo(self):
        self.logo_container = QLabel()
        self.logo = QPixmap(LOGO)
        self.logo = self.logo.scaledToHeight(50)
        self.logo_container.setPixmap(self.logo)
        self.logo_container.setAlignment(Qt.AlignCenter)
        self.win_lo.addWidget(self.logo_container)

    def create_msg(self):
        self.header1 = QLabel('Oops! Database\ncould not be found')
        self.header1.setAlignment(Qt.AlignCenter)
        self.header1.setStyleSheet(H1_STYLE)
        self.win_lo.addWidget(self.header1)

        self.header2 = QLabel('Please set your database path')
        self.header2.setAlignment(Qt.AlignCenter)
        self.header2.setStyleSheet(H2_STYLE)
        self.win_lo.addWidget(self.header2)

    def create_inputs(self):
        self.inputbox = QGroupBox('Path to history')
        self.inputbox.setStyleSheet(GROUPBOX_STYLE)
        self.inputbox_lo = QHBoxLayout()
        self.inputbox.setLayout(self.inputbox_lo)
        self.path_txt = QTextEdit()
        self.path_txt.setFixedHeight(30)
        self.path_txt.setStyleSheet(TEXTEDIT_STYLE)
        self.path_btn = QPushButton()
        self.path_btn.setFixedSize(30, 30)
        self.path_btn.setStyleSheet(SMALL_BTN_STYLE)
        self.path_btn.setIcon(QIcon(PATH_ICON))
        self.path_btn.setIconSize(QSize(18, 16))
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.path_btn.setGraphicsEffect(shadow)

        self.inputbox_lo.addWidget(self.path_txt)
        self.inputbox_lo.addWidget(self.path_btn)

        self.win_lo.addWidget(self.inputbox)

    def create_ok(self):
        self.ok_btn = QPushButton('OK')
        self.ok_btn.setStyleSheet(LONG_BTN_STYLE)
        self.ok_btn.setFixedSize(200, 50)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.ok_btn.setGraphicsEffect(shadow)
        self.win_lo.addWidget(self.ok_btn, alignment=Qt.AlignCenter)

    
class NoChrome(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(NOChrome_TITLE)
        self.setWindowIcon(QIcon(WINDOW_ICON))
        self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setStyleSheet(WINDOW_STYLE)

        self.win_lo = QVBoxLayout()
        self.win = QWidget()

        self.win.setLayout(self.win_lo)
        self.win_lo.setSpacing(10)
        self.win_lo.setContentsMargins(20, 20, 20, 20)
        self.win.setFixedSize(400, 300)
        self.win_lo.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.win)

        self.create_GUI()

    def create_GUI(self):
        self.create_logo()
        self.create_msg()
        self.create_ok()

    def create_logo(self):
        self.logo_container = QLabel()
        self.logo = QPixmap(LOGO)
        self.logo = self.logo.scaledToHeight(50)
        self.logo_container.setPixmap(self.logo)
        self.logo_container.setAlignment(Qt.AlignCenter)
        self.win_lo.addWidget(self.logo_container)

    def create_msg(self):
        self.header1 = QLabel('looks like\nChrome is not installed\non your system')
        self.header1.setAlignment(Qt.AlignCenter)
        self.header1.setStyleSheet(H1_STYLE)
        self.win_lo.addWidget(self.header1)

        self.header2 = QLabel('Please install Chrome to proceed')
        self.header2.setAlignment(Qt.AlignCenter)
        self.header2.setStyleSheet(H2_STYLE)
        self.win_lo.addWidget(self.header2)

    def create_ok(self):
        self.ok_btn = QPushButton('OK')
        self.ok_btn.setStyleSheet(LONG_BTN_STYLE)
        self.ok_btn.setFixedSize(200, 50)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.ok_btn.setGraphicsEffect(shadow)
        self.win_lo.addWidget(self.ok_btn, alignment=Qt.AlignCenter)


class InvalidEmail(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(INVALID_EMAIL_TITLE)
        self.setWindowIcon(QIcon(WINDOW_ICON))
        self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setStyleSheet(WINDOW_STYLE)

        self.win_lo = QVBoxLayout()
        self.win = QWidget()

        self.win.setLayout(self.win_lo)
        self.win_lo.setSpacing(10)
        self.win_lo.setContentsMargins(20, 20, 20, 20)
        self.win.setFixedSize(400, 300)
        self.win_lo.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.win)

        self.create_GUI()

    def create_GUI(self):
        self.create_logo()
        self.create_msg()
        self.create_ok()

    def create_logo(self):
        self.logo_container = QLabel()
        self.logo = QPixmap(LOGO)
        self.logo = self.logo.scaledToHeight(50)
        self.logo_container.setPixmap(self.logo)
        self.logo_container.setAlignment(Qt.AlignCenter)
        self.win_lo.addWidget(self.logo_container)

    def create_msg(self):
        self.header1 = QLabel('looks like\nthe email which you have entered\nis invalid')
        self.header1.setAlignment(Qt.AlignCenter)
        self.header1.setStyleSheet(H1_STYLE)
        self.win_lo.addWidget(self.header1)

        self.header2 = QLabel('Please enter a valid email')
        self.header2.setAlignment(Qt.AlignCenter)
        self.header2.setStyleSheet(H2_STYLE)
        self.win_lo.addWidget(self.header2)

    def create_ok(self):
        self.ok_btn = QPushButton('OK')
        self.ok_btn.setStyleSheet(LONG_BTN_STYLE)
        self.ok_btn.setFixedSize(200, 50)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.ok_btn.setGraphicsEffect(shadow)
        self.win_lo.addWidget(self.ok_btn, alignment=Qt.AlignCenter)