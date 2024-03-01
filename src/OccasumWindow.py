from Vasak.VSKWindow import VSKWindow
from Vasak.system.VSKConfigManager import VSKConfigManager
from src.OccasumBinding import OccasumBinding
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

class OccasumWindow(VSKWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.shareObject = OccasumBinding(self, app)
        self.channel.registerObject("vsk", self.shareObject)
        self.configManager = VSKConfigManager()
        self.load_html("ui/dist/index.html") # Cargar un HTML en el WebView
        self.set_position()
    
    def set_position(self):
        self.setWindowFlags(
            self.windowFlags() | Qt.WindowType.FramelessWindowHint 
        )
        self.resize(800, 600)
    
    def send_Javascript(self, message):
        self.webview.page().runJavaScript(message)
    
    def load_ui_config(self):
        self.configManager.reload()
        darkMode = self.configManager.get('STYLE', 'darkmode')
        radius = self.configManager.get('STYLE', 'radius')
        color = self.configManager.get('STYLE', 'color')

        self.send_Javascript(f'document.body.style.setProperty("--system-rounded", "{radius}px")')
        self.send_Javascript(f'document.body.style.setProperty("--system-accent-color", "{color}")')
        if darkMode == 'true':
            self.send_Javascript('document.body.classList.add("dark")')
        else:
            self.send_Javascript('document.body.classList.remove("dark")')