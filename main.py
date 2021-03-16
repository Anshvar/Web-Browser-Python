import sys
from PyQt5.QtWidgets import*
from PyQt5.QtWebEngineWidgets import*
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back' , self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        refresh_btn = QAction('Refresh' , self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        forward_btn = QAction('Forward' , self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        Home_btn = QAction('Home' , self)
        Home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(Home_btn)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.urlbar)

        self.browser.urlChanged.connect(self.update_url)


    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))
    def navigate_url(self):
        url = self.urlbar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self, q):
        self.urlbar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('My Own Browser')
window = MainWindow()
app.exec_()
