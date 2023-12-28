from Vasak.VSKWindow import VSKWindow
from src.OccasumBinding import OccasumBinding
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

class OccasumWindow(VSKWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.shareObject = OccasumBinding(self, app)
        self.channel.registerObject("vsk", self.shareObject)
        self.load_html("ui/dist/index.html") # Cargar un HTML en el WebView
        self.set_position()
    
    def set_position(self):
        self.setWindowFlags(
            self.windowFlags() | Qt.WindowType.FramelessWindowHint 
        )
        self.resize(800, 600)