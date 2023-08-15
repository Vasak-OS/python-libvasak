import os
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView


class VSKWindow(QMainWindow):
    def __init__(self, screen_num=0):
        super().__init__()
        self.webview = None
        self.set_attributes()  # Establecer atributos de la ventana
        self.move_to_screen(screen_num)  # Mover la ventana a una pantalla específica
        self.set_widget()  # Establecer el widget central. Y el WebView.
        self.set_webview_poprties()

    # Mover la ventana a una pantalla específica
    def move_to_screen(self, screen_num):
        #desktop = QApplication.desktop()
        #available_rect = desktop.availableGeometry(screen_num)
        #self.move(available_rect.topLeft())
        pass

    # Establecer atributos de la ventana
    def set_attributes(self):
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)  # Fondo transparente
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)  # No dibujar el fondo del sistema

    # Cargar un HTML en el WebView
    def load_html(self, html):
        file_path = os.path.abspath(html)
        self.webview.webContent = file_path
        self.webview.load(QUrl.fromLocalFile(file_path))
        page = self.webview.page()
        page.setBackgroundColor(Qt.ColorScheme.transparent)

    def set_webview_poprties(self):
        self.webview.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        settings = self.webview.settings()
        settings.setAttribute(settings.JavascriptEnabled, True)
        settings.setAttribute(settings.AllowWindowActivationFromJavaScript, True)
        settings.setAttribute(settings.ShowScrollBars, False)

    # Establecer el widget central. Y el WebView.
    def set_widget(self):
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
