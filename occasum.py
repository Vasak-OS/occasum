import sys
import signal
import os
from src.OccasumWindow import OccasumWindow
from PyQt6.QtCore import QFileSystemWatcher
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon


app = QApplication(sys.argv)
files = [os.path.expanduser('~') + '/.config/vasak/vasak.conf']
watcher = QFileSystemWatcher(files)
watcher.addPaths(files)


if __name__ == "__main__":
    app.setApplicationName("Occasum")
    app.setApplicationVersion("0.0.1")
    app.setOrganizationName("Vasak Group")
    app.setApplicationDisplayName("Occasum")
    app.setWindowIcon(QIcon.fromTheme("configurator"))
    window = OccasumWindow(app)
    watcher.fileChanged.connect(window.load_ui_config)
    window.show()
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Habilitar Ctrl+C
    sys.exit(app.exec())
