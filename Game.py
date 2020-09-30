# -- coding: utf-8 --
"""
Created on Wed Sep 30 2020

@author: Julia Butte, Sebastian Weber, Thomas Weber
"""

import abc
import os
from abc import ABC
from random import choice
from numpy.core.fromnumeric import sort
from qiskit import circuit


from quno.output import *
from quno.card import *
from quno.execution import *
from quno.player import Player
from quno.input import getInput


""" This class represents a game of quno. The game has three difficulties 
    as seen in the subclasses of Game."""
class Game(ABC):
    """The number of Qbits used"""
    qibit_count = 3
    """The default number of cards per player"""
    card_count = 1
    """Possible combinations for the three qbits"""
    targets = ["[1, 1, 1]", "[1, 1, 0]", "[1, 0, 1]", "[1, 0, 0]", "[0, 1, 1]", "[0, 1, 0]", "[0, 0, 1]", "[0, 0, 0]"]

    def __init__(self, playercount, players, circuit):
        """
        the number of players, the player list and the circuit object
        """
        self.playercount = playercount
        self.players = players
        self.circuit = circuit
        pass
    

    @abc.abstractmethod
    def getGameMode(self):
        """
        returns a string representation for the game mode
        """
        pass

    @abc.abstractmethod
    def placeCard(self, activePlayer):
        """
        the difficulty specific behaviour
        """
        pass

    def mainLoop(self):
        """
        the main loop of the program, contains inputs and the execution of placeCard 
        """
        activePlayerIndex = 0
        while self.players[activePlayerIndex].hasCards():
            cls()
            activePlayer = self.players[activePlayerIndex]
            output('Turn of ' + activePlayer.getInfo())
            printSeparation()
            output(self.circuit.draw())
            printSeparation()
            output(activePlayer.getCards())
            printSeparation()
            self.placeCard(activePlayer)
            activePlayerIndex = (activePlayerIndex + 1) % len(self.players)
        self.printResults()
        

    def printResults(self) :
        """
        prints the result of the game to the output specified in output 
        """
        cls()
        result = calculateResult(self.circuit)
        results = []
        for player in self.players:
            results.append((hamming(result, player.endconfig), player.name))
        reversed(sort(results))
        _,y = results[0]
        output('Player ' + str(y) + ' wins!\n' + str(results))
        printSeparation()
        output(self.circuit.draw())

    def drawCircuit(self):
        """
        string representation of the circuit 
        """
        return str(self.circuit.draw())

    @staticmethod
    def randomTargetVector():
        """
        returns one of the possible 3 bit target vectors 
        """
        chosenTarget = choice(Game.targets)
        Game.targets.remove(chosenTarget)
        return chosenTarget

    @staticmethod
    def randomCard():
        """
        returns a card with a random gate on it
        """
        return Card(choice(list(Gate)))

    @staticmethod
    def randomCardHand():
        """
        returns a full hand of random cards
        """
        cards = []
        for index in range (0, Game.card_count):
            cards.append(Game.randomCard())
        return cards

    @staticmethod
    def initializeGame(): 
        """
        initializes the game by collecting user input on the game parameters
        """
        while True :
            mode = getInput('Please enter the game mode (easy, normal or hard): ')
            playercount = int(getInput('Please enter the number of players: '))
            Game.card_count = int(getInput('Please enter the number of cards per player: '))
            players = []
            # initialize a player with a hand of cards and a random goal vector
            for index in range (0, playercount):
                name = getInput('Please enter a name for player ' + str(index) + ': ')
                goal_vector = Game.randomTargetVector()
                output('Player ' + name + ' has the goal vector ' + str(goal_vector))
                players.append(Player(goal_vector, name, Game.randomCardHand()))
            circuit = QuantumCircuit(Game.qibit_count, Game.qibit_count)
            # set the game mode based on the user input
            if mode == 'easy': 
                return EasyGame(playercount, players, circuit)
            elif mode == 'normal':
                return NormalGame(playercount, players, circuit)
            elif mode == 'hard':
                return HardGame(playercount, players, circuit)

    def getCardParametersAndPlaceCard(self, activePlayer):
        """
        choose the card to play and get the required parameters to place the card and 
        place the card afterwards 
        """
        cardIndex = int(getInput('Choose a card index(0..' + str(activePlayer.lenCards()-1) + '): '))
        card = activePlayer.getCard(cardIndex)
        numberParams = card.gate.getParamCount()
        params = []
        for param in range (0, numberParams):
            params.append(int(getInput('Choose parameter ' + str(param) + ' out of ' + str(numberParams) + ' for gate ' + card.gate.get() + ': ')))
        addGateToCircuit(self.circuit, card.gate, params)
        return cardIndex

class EasyGame(Game):
    Game
    def getGameMode(self):
        return "easy"

    def placeCard(self, activePlayer):
        """
        easy mode with probabilities and the option to withdraw a card
        after knowing its effect
        """
        output(getProbabilityOutput(self.circuit))
        confirmed = False
        while not confirmed:
            cardIndex = self.getCardParametersAndPlaceCard(activePlayer)
            output(getProbabilityOutput(self.circuit))
            if getInput('Please confirm your choice with \'Y\' ') == 'Y':
                activePlayer.removeCard(cardIndex)
                confirmed = True
            else:
                self.circuit.data.pop(0)
            

class NormalGame(Game):
    Game
    def getGameMode(self):
        return "normal"

    def placeCard(self, activePlayer):
        """
        normal mode with probabilities
        """
        output(getProbabilityOutput(self.circuit))
        activePlayer.removeCard(self.getCardParametersAndPlaceCard(activePlayer))

class HardGame(Game):
    Game
    def getGameMode(self):
        return "hard"

    def placeCard(self, activePlayer):
        """
        hard mode without any aid
        """
        activePlayer.removeCard(self.getCardParametersAndPlaceCard(activePlayer))

def hamming(first, second):
    """
    hamming distance between two strings
    """
    return len(list(filter(lambda x : ord(x[0])^ord(x[1]), zip(first, second))))

def cls():
    """
    clears the command line for a cleaner game flow
    """
    os.system('cls' if os.name=='nt' else 'clear')

def printSeparation():
    """
    prints a visual separation
    """
    output('-------------------------------------------------------------')


# initialize the game with user input
game = Game.initializeGame()
# enter the game loop and play the game
game.mainLoop()
