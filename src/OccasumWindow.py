from Vasak.VSKWindow import VSKWindow
from src.OccasumBinding import OccasumBinding

class OccasumWindow(VSKWindow):
    def __init__(self):
        super().__init__()
        self.shareObject = OccasumBinding(self)
        self.channel.registerObject("vsk", self.shareObject)
        self.load_html("ui/dist/index.html") # Cargar un HTML en el WebView
