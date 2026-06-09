import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import *

class ANG1Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ANG1 Browser v1.0")
        self.setGeometry(100, 100, 1200, 800)

        # Asosiy veb-oyna
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)

        # Navigatsiya paneli
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Orqaga qaytish tugmasi
        back_btn = QAction("Ortga", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # URL satri
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

app = QApplication(sys.argv)
window = ANG1Browser()
window.show()
app.exec()
