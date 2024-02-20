import sys
import signal
from src.OccasumWindow import OccasumWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon


app = QApplication(sys.argv)

if __name__ == "__main__":
    app.setApplicationName("Occasum")
    app.setApplicationVersion("0.0.1")
    app.setOrganizationName("Vasak Group")
    app.setApplicationDisplayName("Occasum")
    app.setWindowIcon(QIcon.fromTheme("configurator"))
    window = OccasumWindow(app)
    window.show()
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Habilitar Ctrl+C
    sys.exit(app.exec())
