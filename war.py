import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QMainWindow):
   def __init__(self):
      super().__init__()

      self.setWindow()
      self.setNextCardButton()
      
   def setWindow(self):
      self.setWindowTitle("War")
      self.setFixedSize(QSize(900, 400))
   
   def setNextCardButton(self):
      nextCardButton = QPushButton("Next card", self)
      nextCardButton.setGeometry(375, 300, 150, 50)
      #startButton.clicked.connect(self.showNextCard)
      

stylesheet = """
    MainWindow {
        background-image: url("bg.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""
    
def openWindow():
   app = QApplication([])
   app.setStyleSheet(stylesheet)
   window = Window()
   window.show()
   app.exec()
   
if __name__ == '__main__':
   openWindow()
   
