import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from random import *

class Card:
   symbol = ''
   value = 0
   def __init__(self, symbol, value):
      self.symbol = symbol
      self.value = value
   
   def getSymbol(self):
      return self.symbol
   
   def getValue(self):
      return self.value
   
   def printCard(self):
      print("Symbol:", self.getSymbol(), ", Value:", self.getValue())
      
class Jucator:
   cards = list()
   
   def __init__(self, cards):
      self.cards = cards
   
   def getCards(self):
      return self.cards
   
   def addCard(self, card):
      self.cards.append(card)
   
   def addCards(self, cards):
      self.cards = self.cards + cards
   
   def removeFirstCard(self):
      self.cards.pop(0)
      
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

def createDeck():
   deck = list()
   symbols = ['club', 'diamond', 'heart', 'spade']
   for a in symbols:
      for i in range(2, 11):
         deck.append(Card(a, i))
      for i in range(12, 15):
         deck.append(Card(a, i))
      deck.append(Card(a, 100))
   return deck

def shuffleDeck(deck):
   shuffledDeck = list()
   for i in range(1, 53):
      randomNr = randint(1, 53-i)
      shuffledDeck.append(deck[randomNr - 1])
      deck.pop(randomNr - 1)
   return shuffledDeck

if __name__ == '__main__':
   #openWindow()
   deck = shuffleDeck(createDeck())
   for a in deck:
      print(a.printCard())
   
