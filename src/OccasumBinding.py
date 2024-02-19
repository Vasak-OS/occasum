import os
import json
from PyQt6.QtCore import pyqtSlot, QObject, Qt
from Vasak.hardware.VSKInfoHard import VSKInfoHard
from Vasak.system.VSKIconManager import VSKIconManager

class OccasumBinding(QObject):
  def __init__(self, window, app):
    super().__init__()
    self.window = window
    self.app = app
    self.info = VSKInfoHard()
    self.iconManager = VSKIconManager()

  @pyqtSlot(result=str)
  def getHome(self):
      home_path = os.path.expanduser("~")

      if not os.path.isabs(home_path):
        home_path = os.path.join("/", home_path)

      return home_path
  
  @pyqtSlot()
  def startMove(self):
    self.window.windowHandle().startSystemMove()
  
  @pyqtSlot(str)
  def startResize(self, direction: str):
    
    if direction == "top":
      direction = Qt.Edge.TopEdge
    elif direction == "right":
      direction = Qt.Edge.RightEdge
    elif direction == "bottom":
      direction = Qt.Edge.BottomEdge
    elif direction == "left":
      direction = Qt.Edge.LeftEdge
    elif direction == "topright":
      direction = Qt.Edge.TopEdge | Qt.Edge.RightEdge
    elif direction == "bottomright":
      direction = Qt.Edge.BottomEdge | Qt.Edge.RightEdge
    elif direction == "bottomleft":
      direction = Qt.Edge.BottomEdge | Qt.Edge.LeftEdge
    elif direction == "topleft":
      direction = Qt.Edge.TopEdge | Qt.Edge.LeftEdge
    else:
      direction = Qt.Edge.TopEdge | Qt.Edge.LeftEdge
    
    self.window.windowHandle().startSystemResize(direction)
  
  @pyqtSlot()
  def exit(self):
    self.app.exit()

  @pyqtSlot()
  def minimize(self):
    self.window.showMinimized()
  
  @pyqtSlot()
  def toggleMaximize(self):
    if self.window.isMaximized():
      self.window.showNormal()
    else:
      self.window.showMaximized()

  @pyqtSlot(result=str)
  def getOSInfo(self):
    return json.dumps(self.info.getInfo())
  
  @pyqtSlot(str, result=str)
  def getIcon(self, name):
    return self.iconManager.get_icon(name)
