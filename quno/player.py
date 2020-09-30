# -- coding: utf-8 --
"""
Created on Wed Sep 30 2020

@author: Julia Butte, Sebastian Weber, Thomas Weber
"""

""" This class represents a player in this game"""
class Player (object) :
    def __init__(self, endconfig, name, cards) :
        self.endconfig = endconfig
        self.name = name
        self.cards = cards

    """ Returns the player's name and aim"""
    def getInfo(self) :
        return self.name + " aiming for: " + str(self.endconfig)

    """ Returns the player's cards"""
    def getCards(self) :
        firstLine = ""
        secondLine = ""
        thirdLine = ""
        # build a 'card like' representation for the cmd output
        for card in self.cards:
            firstLine += "_" * (len(card.gate.get()) + 2) + " "
            secondLine += "|" + card.gate.get() + "| "
            thirdLine += "‾" * (len(card.gate.get()) + 2) + " "
        return firstLine + "\n" + secondLine + "\n" + thirdLine

    """ Returns the card at the specified index"""
    def getCard(self, index) :
        return self.cards[index]
    def addCard(self, card) :
        self.cards + card

    """ Removes the card at the specified index"""
    def removeCard(self, index) :
        self.cards.remove(self.cards[index])
    """ Returns if the player has more cards to place"""
    def hasCards(self):
        return len(self.cards)>0
    """ Returns the number of cards"""
    def lenCards(self):
        return len(self.cards)
