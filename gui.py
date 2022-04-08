from PyQt5.QtWidgets import QWidget, QMainWindow, \
    QGridLayout, QVBoxLayout, QHBoxLayout, \
        QLabel, QPushButton, QSpacerItem, QTextEdit, QGroupBox, QLineEdit, QFileDialog, \
            QSizePolicy, QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QColor, QPixmap
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtTest import QTest

from plotly.graph_objects import Figure, Scatter, Layout, Bar, Pie
import plotly

from os.path import exists
from classes.database import Database

import smtplib, ssl

from validate_email_address import validate_email


from vars import *
from classes.appdata import *
from classes.user import *
 
global img1, img2, img3, win2

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
        self.create_now()
        self.create_nod()
        self.create_tod()
        self.create_viw()
        self.create_wv()
        self.create_mvw()

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
        self.download_btn.clicked.connect(self.click_download)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.download_btn.setGraphicsEffect(shadow)
        self.sidebar_lo.addWidget(self.download_btn)

    def click_download(self):
        folder = QFileDialog.getExistingDirectory(self)
        img1.write_image(f'{folder}/visits_in_week.png')
        img2.write_image(f'{folder}/website_visits.png')
        img3.write_image(f'{folder}/most_visited_websites.png')

    def create_update(self):
        self.update_btn = QPushButton()
        self.update_btn.setStyleSheet(BTN_STYLE)
        self.update_btn.setFixedHeight(80)
        self.update_btn.setIcon(QIcon(UPDATE_ICON))
        self.update_btn.setIconSize(QSize(50, 50))
        self.update_btn.clicked.connect(self.click_update)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.update_btn.setGraphicsEffect(shadow)
        self.sidebar_lo.addWidget(self.update_btn)

    def click_update(self):
        for layout in self.boxes_lo:
            for i in reversed(range(layout.count())): 
                layout.itemAt(i).widget().deleteLater()
        self.create_now()
        self.create_nod()
        self.create_tod()
        self.create_viw()
        self.create_wv()
        self.create_mvw()

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
        self.boxes_lo = [QVBoxLayout(), QVBoxLayout(), QGridLayout(), QVBoxLayout(), QVBoxLayout(), QVBoxLayout()]

        for i, box in enumerate(self.boxes):
            box.setStyleSheet(BOX_STYLE)
            box.setLayout(self.boxes_lo[i])
            self.boxes_lo[i].setSpacing(0)
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor('#111'))
            shadow.setOffset(2)
            shadow.setBlurRadius(10)
            box.setGraphicsEffect(shadow)
            if i < 3:
                box.setFixedHeight(180)

        self.container_lo.addWidget(self.boxes[0], 0, 0, 1, 1)
        self.container_lo.addWidget(self.boxes[1], 0, 1, 1, 1)
        self.container_lo.addWidget(self.boxes[2], 0, 2, 1, 2)
        self.container_lo.addWidget(self.boxes[3], 1, 0, 1, 4)
        self.container_lo.addWidget(self.boxes[4], 2, 0, 1, 3)
        self.container_lo.addWidget(self.boxes[5], 2, 3, 1, 1)

    def create_now(self):
        username = ''
        with open('user.txt') as user:
            username = user.readline().strip()
        now = NoOfWebsites(username)
        self.b0_lbl0 = QLabel(str(now.get_data()))
        self.b0_lbl0.setStyleSheet(b0_lbl0_STYLE)
        self.b0_lbl0.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        self.boxes_lo[0].addWidget(self.b0_lbl0)
        self.b0_lbl1 = QLabel('Websites Visited')
        self.b0_lbl1.setStyleSheet(b0_lbl1_STYLE)
        self.b0_lbl1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.boxes_lo[0].addWidget(self.b0_lbl1)

    def create_nod(self):
        username = ''
        with open('user.txt') as user:
            username = user.readline().strip()
        nod = NoOfDownloads(username)
        self.b1_lbl0 = QLabel(str(nod.get_data()))
        self.b1_lbl0.setStyleSheet(b0_lbl0_STYLE)
        self.b1_lbl0.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        self.boxes_lo[1].addWidget(self.b1_lbl0)
        self.b1_lbl1 = QLabel('Downloads')
        self.b1_lbl1.setStyleSheet(b0_lbl1_STYLE)
        self.b1_lbl1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.boxes_lo[1].addWidget(self.b1_lbl1)

    def create_tod(self):
        username = ''
        with open('user.txt') as user:
            username = user.readline().strip()
        tod = TermsOfDay(username)
        self.b2_lbls = [QLabel(tod.get_data()[i]) for i in range(len(tod.get_data()))]
        for i in range(len(tod.get_data())):
            self.b2_lbls[i].setStyleSheet(b2_lbl_STYLE)
            self.boxes_lo[2].addWidget(self.b2_lbls[i], i % 5, i // 5, 1, 1)

    def create_viw(self):
        username = ''
        with open('user.txt') as user:
            username = user.readline().strip()
        viw = VisitsInWeek(username)
        x = ['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'Today']
        y = viw.get_data()
        fig = Figure(data=Scatter(x=x, y=y, line=dict(color='#DF5865')), layout = Layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            ))
        fig.update_layout(
            xaxis = dict(
                tickfont = dict(size=10, color='#888')
                )
            )
        fig.update_xaxes(showline=True, linewidth=1, linecolor='#534f82', gridcolor='#353354')
        fig.update_yaxes(showline=True, linewidth=1, linecolor='#534f82', gridcolor='#353354')
        global img1 
        img1 = fig

        html = '<html><body style="background:#24233A;">'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.resize(600, 200)
        plot_widget.setHtml(html)
        self.boxes_lo[3].addWidget(plot_widget)

    def create_wv(self):
        username = ''
        with open('user.txt') as user:
            username = user.readline().strip()
        wv = WebsiteVisits(username)
        x = list(wv.get_data().keys())
        y = list(wv.get_data().values())
        fig = Figure(data=Bar(x=x, y=y, marker_color='#86C38F'), layout = Layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
            ))
        fig.update_layout(
            xaxis = dict(
                tickfont = dict(size=10, color='#888')
                )
            )
        fig.update_xaxes(showline=True, linewidth=1, linecolor='#534f82', gridcolor='#353354')
        fig.update_yaxes(showline=True, linewidth=1, linecolor='#534f82', gridcolor='#353354')
        global img2 
        img2 = fig

        html = '<html><body style="background:#24233A;">'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.resize(200, 200)
        plot_widget.setHtml(html)
        self.boxes_lo[4].addWidget(plot_widget)


    def create_mvw(self):
        username = ''
        with open('user.txt') as user:
            username = user.readline().strip()
        mvw = MostVisitedWebsites(username)
        x = list(mvw.get_data().keys())[:5]
        y = list(mvw.get_data().values())[:5]

        fig = Figure(data=Pie(labels=x, values=y), layout = Layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            ))
        fig.update_layout(
            legend = dict(font = dict(size = 10))
            )
        fig.update_xaxes(showline=True, linewidth=1, linecolor='#534f82', gridcolor='#353354')
        fig.update_yaxes(showline=True, linewidth=1, linecolor='#534f82', gridcolor='#353354')
        global img3
        img3 = fig
        
        html = '<html><body style="background:#24233A;">'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.resize(600, 200)
        plot_widget.setHtml(html)
        self.boxes_lo[5].addWidget(plot_widget)


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
        self.username.setToolTip('Please choose the same name\nas that of your system')
        self.email_lbl = QLabel('Email')
        self.email_lbl.setStyleSheet(LABEL_STYLE)
        self.email = QTextEdit()
        self.email.setFixedHeight(30)
        self.email.setStyleSheet(TEXTEDIT_STYLE)
        self.email.setToolTip('Please choose an email\nwhich is not linked with Chrome')
        self.password_lbl = QLabel('Password')
        self.password_lbl.setStyleSheet(LABEL_STYLE)
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFixedHeight(30)
        self.password.setStyleSheet(TEXTEDIT_STYLE)
        self.password.setToolTip('Please Choose a strong password')
        self.confirm_password_lbl = QLabel('Confirm Password')
        self.confirm_password_lbl.setStyleSheet(LABEL_STYLE)
        self.confirm_password = QLineEdit()
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.confirm_password.setFixedHeight(30)
        self.confirm_password.setStyleSheet(TEXTEDIT_STYLE)
        self.confirm_password.setToolTip('Please rewrite the password')

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
        self.signup_btn.clicked.connect(self.click_signup)
        self.win_lo.addWidget(self.signup_btn, alignment=Qt.AlignCenter)

    def click_signup(self):
        username = self.username.toPlainText()
        email = self.email.toPlainText()
        password = self.password.text()
        confirm_password = self.confirm_password.text()

        global win2
        if not exists(f'C:\\Users\\{username}'):
            self.username_lbl.setText('Username does not exist')
        elif not validate_email(email):
            invalidemail = InvalidEmail()
            invalidemail.show()
            win2 = invalidemail
        elif password != confirm_password:
            self.confirm_password_lbl.setText('Passwords did not match')
        else:
            self.username_lbl.setText('Username')
            self.confirm_password_lbl.setText('Confirm Password')
            user = User(username, password, email, True, True)
            user.store()
            self.close()
            if not exists(f'C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'):
                nodb = NoDB()
                nodb.show()
                win2 = nodb
            else:
                main = Window()
                main.showMaximized()
                win2 = main
            

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
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFixedHeight(30)
        self.password.setStyleSheet(TEXTEDIT_STYLE)
        self.forgot = QPushButton('forgot password ?')
        self.forgot.setStyleSheet(FORGOT_STYLE)
        self.forgot.setFixedWidth(100)
        self.forgot.clicked.connect(self.click_forgot)
        
        self.win_lo.addWidget(self.username_lbl)
        self.win_lo.addWidget(self.username)
        self.win_lo.addWidget(self.password_lbl)
        self.win_lo.addWidget(self.password)
        self.win_lo.addWidget(self.forgot)

    def click_forgot(self):
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "youremail"
        receiver_email = ""
        message = 'Subject: Password\n\n'
        with open('user.txt', 'r') as user:
            user.readline()
            receiver_email = user.readline()
            message += user.readline()
        password = 'yourpwd'
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.ehlo()
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            self.forgot.setText('Check the mail')
            QTest.qWait(5000)
            self.forgot.setText('Forgot Password ?')

    def create_signin(self):
        self.signin_btn = QPushButton('SIGN IN')
        self.signin_btn.setStyleSheet(LONG_BTN_STYLE)
        self.signin_btn.setFixedSize(200, 50)
        self.signin_btn.clicked.connect(self.click_signin)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.signin_btn.setGraphicsEffect(shadow)
        self.win_lo.addWidget(self.signin_btn, alignment=Qt.AlignCenter)

    def click_signin(self):
        username = self.username.toPlainText()
        password = self.password.text()

        global win2
        with open('user.txt') as user:
            user_username = user.readline().strip()
            user.readline()
            user_password = user.readline().strip()
            if user_username == username and str(password) == user_password:
                self.username_lbl.setText('Username')
                self.password_lbl.setText('Password')
                self.close()
                if not exists(f'C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'):
                    nodb = NoDB()
                    nodb.show()
                    win2 = nodb
                else:
                    main = Window()
                    main.showMaximized()
                    win2 = main
            elif user_username != username and str(password) == user_password:
                self.username_lbl.setText('Invalid Username')
                self.password_lbl.setText('Password')
            elif user_username == username and str(password) != user_password:
                self.username_lbl.setText('Username')
                self.password_lbl.setText('Invalid Password')
            else:
                self.username_lbl.setText('Invalid Username')
                self.password_lbl.setText('Invalid Password')


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
        self.path_btn.clicked.connect(self.click_path_btn)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.path_btn.setGraphicsEffect(shadow)

        self.inputbox_lo.addWidget(self.path_txt)
        self.inputbox_lo.addWidget(self.path_btn)

        self.win_lo.addWidget(self.inputbox)

    def click_path_btn(self):
        file, _ = QFileDialog.getOpenFileName(self)
        self.path_txt.setText(file)

    def create_ok(self):
        self.ok_btn = QPushButton('OK')
        self.ok_btn.setStyleSheet(LONG_BTN_STYLE)
        self.ok_btn.setFixedSize(200, 50)
        self.ok_btn.clicked.connect(self.click_ok)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.ok_btn.setGraphicsEffect(shadow)
        self.win_lo.addWidget(self.ok_btn, alignment=Qt.AlignCenter)

    def click_ok(self):
        file = self.path_txt.toPlainText()
        print(file)
        Database.set_path(file)
        self.close
        global win2
        main = Window()
        main.showMaximized()
        win2 = main

    
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
        self.ok_btn.clicked.connect(self.click_ok)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.ok_btn.setGraphicsEffect(shadow)
        self.win_lo.addWidget(self.ok_btn, alignment=Qt.AlignCenter)

    def click_ok(self):
        self.close()


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
        self.ok_btn.clicked.connect(self.click_ok)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor('#111'))
        shadow.setOffset(2)
        shadow.setBlurRadius(10)
        self.ok_btn.setGraphicsEffect(shadow)
        self.win_lo.addWidget(self.ok_btn, alignment=Qt.AlignCenter)

    def click_ok(self):
        self.close()
