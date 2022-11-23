import sys
from random import *
import tkinter as tk


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
      
class Player:
   cards = list()
   score = 0
   name = ''
   def __init__(self, cards, name):
      self.cards = cards
      self.name = name
      
   def getCards(self):
      return self.cards
   
   def addCard(self, card):
      self.cards.append(card)
   
   def addCards(self, cards):
      self.cards = self.cards + cards
   
   def getCards(self):
      return self.cards
   
   def removeFirstCard(self):
      self.cards.pop(0)
      
   def increaseScore(self):
      self.score = self.score + 1
   
   def getScore(self):
      return self.score
   
   def getName(self):
      return self.name
   
   def getCurrentStatusInGame(self):
      return self.getName() + " Cards: " + str(len(self.getCards())) + " Score: " + str(self.getScore())
   
class Game:
   player1 = Player([], '')
   player2 = Player([], '')
   window = tk.Tk()
   def __init__(self, player1, player2):
      self.player1 = player1
      self.player2 = player2
      self.start()
   
   def start(self):
      
      self.setPlayerLabel()
      self.setComputerLabel()
      self.window.mainloop()
   
   def setPlayerLabel(self):
      frame = tk.Frame(master=self.window, width=200, height=150)
      frame.pack()
      
      label1 = tk.Label(master=frame, text=player1.getCurrentStatusInGame(), bg="white")
      label1.place(x=30, y=30)
      
   def setComputerLabel(self):
      frame2 = tk.Frame(master=self.window, width=200, height=150)
      frame2.pack()

      label2 = tk.Label(master=frame2, text=player2.getCurrentStatusInGame(), bg="white")
      label2.place(x=30, y=300)
      print("a")
      
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

def startGame(player1, player2):
   game = Game(player1, player2)
   
if __name__ == '__main__':
   deck = shuffleDeck(createDeck())
   cardsForPlayer1 = list()
   cardsForPlayer2 = list()
   for i in range(0, 26):
      cardsForPlayer1.append(deck[i])
      cardsForPlayer2.append(deck[51 - i])
   
   player1 = Player(cardsForPlayer1, "Player")
   player2 = Player(cardsForPlayer2, "Computer")
   startGame(player1, player2)
   
      
   
   
