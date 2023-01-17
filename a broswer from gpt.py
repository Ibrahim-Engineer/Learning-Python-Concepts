import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QToolBar, QAction, QMenu
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineScript

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Web Browser")
        self.setGeometry(100, 100, 800, 600)

        # Initialize history list
        self.history = []

        self.web_view = QWebEngineView()
        self.web_view.load(QUrl("https://www.google.com"))
        self.web_view.urlChanged.connect(self.add_to_history)

        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)

        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.go_back)

        self.forward_button = QPushButton(">")
        self.forward_button.clicked.connect(self.go_forward)

        self.layout = QVBoxLayout()
        self.nav_bar = QHBoxLayout()
        self.nav_bar.addWidget(self.back_button)
        self.nav_bar.addWidget(self.forward_button)
        self.nav_bar.addWidget(self.address_bar)

        self.layout.addLayout(self.nav_bar)
        self.layout.addWidget(self.web_view)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.create_toolbar()
        
        # Enable ad-blocking
        profile = self.web_view.page().profile()
        script = QWebEngineScript()
        script.setName("adblock")
        script.setWorldId(QWebEngineScript.ApplicationWorld)
        script.setSourceCode("""
            var adElements = document.getElementsByClassName("ad");
            for (var i = 0; i < adElements.length; i++) {
                adElements[i].remove();
            }
        """)
        script.setInjectionPoint(QWebEngineScript.DocumentReady)
        script.setRunsOnSubFrames(True)
        profile.scripts().insert(script)

    def add_to_history(self, url):
        self.history.append(url)

    def go_back(self):
        if self.history:
            self.history.pop()
            if self.history:
                self.web_view.load(self.history.pop())
    def go_forward(self):
        if self.history:
            self.web_view.load(self.history.pop())

    def load_url(self):
        url = self.address_bar.text()
        self.web_view.load(QUrl(url))

    def create_toolbar(self):
        self.toolbar = self.addToolBar("Navigation")

        # History button
        self.history_button = QAction("History", self)
        self.history_button.setMenu(self.create_history_menu())
        self.toolbar.addAction(self.history_button)

        # Adblock button
        self.adblock_button = QAction("Adblock", self)
        self.adblock_button.setCheckable(True)
        self.adblock_button.setChecked(True)
        self.adblock_button.toggled.connect(self.toggle_adblock)
        self.toolbar.addAction(self.adblock_button)

    def create_history_menu(self):
        menu = QMenu()
        for url in self.history:
            action = QAction(url, self)
            action.triggered.connect(lambda: self.web_view.load(QUrl(url)))
            menu.addAction(action)
        return menu

    def toggle_adblock(self, enabled):
        if enabled:
            # Enable ad-blocking
            profile = self.web_view.page().profile()
            script = QWebEngineScript()
            script.setName("adblock")
            script.setWorldId(QWebEngineScript.ApplicationWorld)
            script.setSourceCode("""
                var adElements = document.getElementsByClassName("ad");
                for (var i = 0; i < adElements.length; i++) {
                    adElements[i].remove();
                }
            """)
            script.setInjectionPoint(QWebEngineScript.DocumentReady)
            script.setRunsOnSubFrames(True)
            profile.scripts().insert(script)
        else:
            # Disable ad-blocking
            profile = self.web_view.page().profile()
            profile.scripts().remove("adblock")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())


           


