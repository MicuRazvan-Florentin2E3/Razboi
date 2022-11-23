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
   
   def setFirstCard(self, card):
      self.cards[0] = card


class Game:
   player1 = Player([], '')
   player2 = Player([], '')
   window = tk.Tk()
   nextCardButton = tk.Button('')
   def __init__(self, player1, player2):
      self.player1 = player1
      self.player2 = player2
      self.start()
   
   def start(self):
      self.setWindowSettings()
      self.setLables()
      self.setNextCardButton()
      self.window.mainloop()
   
   def setWindowSettings(self):
      self.window.geometry('900x400')
      self.window.title("War")
      
   def setLables(self):
      
      label1 = tk.Label(self.window, 
                     text = self.player1.getCurrentStatusInGame(),
                     bd = '1', relief = 'sunken')
      label1.place(x = 20, y = 50)
      
      label2 = tk.Label(self.window, 
                     text = self.player2.getCurrentStatusInGame(),
                     bd = '1', relief = 'sunken')
      label2.place(x = 725, y = 50)
   
   def setNextCardButton(self):
      self.nextCardButton = tk.Button(self.window, text="Next Card", width = 20, command = self.giveNextCard)
      self.nextCardButton.place(x = 400, y = 300)
      
   def giveNextCard(self):
      player1Card = self.player1.getCards()[0]
      player2Card = self.player2.getCards()[0]
      player1.removeFirstCard()
      player2.removeFirstCard()
      
      cardsForWinner = [player1Card, player2Card]

      player1Card.printCard()
      player2Card.printCard()
      if player1Card.getValue() > player2Card.getValue():
         self.player1.addCards(cardsForWinner)
      elif player1Card.getValue() < player2Card.getValue():
         self.player2.addCards(cardsForWinner)
      else:
         print("Razboi")
         if player1Card.getValue() != 100:
            nrDeCartiDeDat = min(player1Card.getValue(), min(len(player1.getCards()), len(player2.getCards())))
         else:
            nrDeCartiDeDat = min(11, min(len(player1.getCards()), len(player2.getCards())))
         
         if(nrDeCartiDeDat == 0):
            print("Total draw")
         else:
            self.warCase(cardsForWinner, nrDeCartiDeDat)
         
   
   def warCase(self, cardsForWinner, nrDeCartiDeDat):
      for i in range(1, nrDeCartiDeDat + 1):
         self.player1.getCards()[0].printCard()
         self.player2.getCards()[0].printCard()
         lastCardPlayer1 = self.player1.getCards()[0]
         lastCardPlayer2 = self.player2.getCards()[0]
         cardsForWinner.append(lastCardPlayer1)
         cardsForWinner.append(lastCardPlayer2)
         player1.removeFirstCard()
         player2.removeFirstCard()
         
      if lastCardPlayer1.getValue() > lastCardPlayer2.getValue():
         player1.addCards(cardsForWinner)
      elif lastCardPlayer1.getValue() < lastCardPlayer2.getValue():
         player2.addCards(cardsForWinner)
      else:
         print("Razboi:")
         nrDeCartiDeDat = 0
         if lastCardPlayer1.getValue() != 100:
            nrDeCartiDeDat = min(lastCardPlayer1.getValue(), min(len(player1.getCards()), len(player2.getCards())))
         else:
            nrDeCartiDeDat = min(11, min(len(player1.getCards()), len(player2.getCards())))
            
         if(nrDeCartiDeDat == 0):
            print("Total draw")
         else:
            self.warCase(cardsForWinner, nrDeCartiDeDat)
            
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

def caseDoubleWar(player1, player2):
   cardsForPlayer1[0] = Card('diamond', 2)
   cardsForPlayer2[0] = Card('heart', 2)
   
   cardsForPlayer1[2] = Card('diamond', 4)
   cardsForPlayer2[2] = Card('heart', 4)
   
   return [player1, player2]

def startGame(player1, player2):
   #player1 = caseDoubleWar(player1, player2)[0]
   #player2 = caseDoubleWar(player1, player2)[1]
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
   

   
   
