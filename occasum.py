import sys
import signal
from src.OccasumWindow import OccasumWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt


app = QApplication(sys.argv)

if __name__ == "__main__":
    app.setApplicationName("Occasum")
    app.setApplicationVersion("0.0.1")
    app.setOrganizationName("Vasak Group")
    window = OccasumWindow(app)
    window.show()
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Habilitar Ctrl+C
    sys.exit(app.exec())
