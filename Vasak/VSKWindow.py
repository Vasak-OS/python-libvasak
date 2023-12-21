import os
from Vasak.application.VSKJavaScript import VSKJavaScript
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWebChannel import QWebChannel
from PyQt6.QtWebEngineWidgets import QWebEngineView


class VSKWindow(QMainWindow):
    def __init__(self, screen_num=0):
        super().__init__()
        self.channel = QWebChannel()
        self.webview = QWebEngineView(self)
        self.setCentralWidget(self.webview)
        self.__set_basic_attributes()  # Establecer atributos de la ventana
        self.__set_webview_properties()

    # Establecer atributos de la ventana
    def __set_basic_attributes(self):
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)  # Fondo transparente
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)  # No dibujar el fondo del sistema

    # Cargar un HTML en el WebView
    def load_html(self, html):
        file_path = os.path.abspath(html)
        self.webview.webContent = file_path
        self.webview.load(QUrl.fromLocalFile(file_path))
        page = self.webview.page()
        page.setBackgroundColor(Qt.GlobalColor.transparent)
        page.setWebChannel(self.channel)
        self.javaScript = VSKJavaScript(page)

    def __set_webview_properties(self):
        self.webview.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        settings = self.webview.settings()
        settings.setAttribute(settings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(settings.WebAttribute.LocalContentCanAccessFileUrls, True)
        settings.setAttribute(settings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(settings.WebAttribute.AllowWindowActivationFromJavaScript, True)
        settings.setAttribute(settings.WebAttribute.ShowScrollBars, False)
