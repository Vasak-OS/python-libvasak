import os
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtWebEngineWidgets import QWebEngineView


class VSKWindow(QMainWindow):
    def __init__(self, screen_num=0):
        super().__init__()
        self.webview = None
        self.__set_basic_attributes()  # Establecer atributos de la ventana
        self.__set_webengine_widget()  # Establecer el widget central. Y el WebView.
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
        page.setBackgroundColor(Qt.ColorScheme.transparent)

    def __set_webview_properties(self):
        self.webview.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        settings = self.webview.settings()
        settings.setAttribute(settings.JavascriptEnabled, True)
        settings.setAttribute(settings.AllowWindowActivationFromJavaScript, True)
        settings.setAttribute(settings.ShowScrollBars, False)

    # Establecer el widget central. Y el WebView.
    def __set_webengine_widget(self):
        self.webview = QWebEngineView(self)
        self.setCentralWidget(self.webview)

    def set_as_dock(self):
        self.setAttribute(Qt.WidgetAttribute.WA_X11NetWmWindowTypeDock, True)  # Seteo tipo dock x11
        self.setAttribute(Qt.WidgetAttribute.WA_AlwaysStackOnTop, True)  # Mantener la ventana por encima de las demás
        self.setWindowFlags(
            self.windowFlags() | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )  # Establecer atributos de la ventana (sin bordes, sin barra de título, etc.)

    def set_as_desktop(self):
        self.setAttribute(Qt.WidgetAttribute.WA_X11NetWmWindowTypeDesktop, True)  # Seteo tipo desktop x11
        self.setAttribute(Qt.WidgetAttribute.WA_WA_AlwaysStackOnTop, False)
        self.setWindowFlags(
            self.windowFlags() | Qt.WindowType.FramelessWindowHint | Qt.WindowType.Desktop
        )
