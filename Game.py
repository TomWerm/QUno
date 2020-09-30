import sys
import abc
import os
from abc import ABC
from random import choice

from quno.output import *
from quno.card import *
from quno.execution import *
from quno.player import Player
from quno.input import getInput
from qiskit import circuit


class Game(ABC):

    qibit_count = 3
    card_count = 5

    def __init__(self, playercount, players, circuit):
        """
        docstring
        """
        self.playercount = playercount
        self.players = players
        self.circuit = circuit
        pass
    

    @abc.abstractmethod
    def getGameMode(self):
        return ""

    @abc.abstractmethod
    def placeCard(self, activePlayer):
        pass

    def mainLoop(self):
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
        output(calculateResult(self.circuit))

    def printPlayers(self):
        """
        docstring
        """
        result = ""
        for player in self.players:
            result += player.getInfo()
        return result

    def drawCircuit(self):
        return str(self.circuit.draw())

    @staticmethod
    def randomValue():
        return Statevector([ 0-1j, -1+0j, 1-0j],dims=(Game.qibit_count,))

    @staticmethod
    def randomCard():
        return Card(choice(list(Gate)))

    @staticmethod
    def randomCardHand():
        cards = []
        for index in range (0, Game.card_count):
            cards.append(Game.randomCard())
        return cards

    @staticmethod
    def initializeGame(): 
        while True :
            # mode = getInput('Please enter the game mode (easy, normal or hard): ')
            mode = 'easy'
            # playercount = int(getInput('Please enter the number of players: '))
            playercount = 2
            players = []
            for index in range (0, playercount):
                name = getInput('Please enter a name for player ' + str(index) + ': ')
                goal_vector = Game.randomValue()
                output('Player ' + name + ' has the goal vector ' + str(goal_vector))
                players.append(Player(goal_vector, name, Game.randomCardHand()))
            circuit = QuantumCircuit(Game.qibit_count)
            if mode == 'easy': 
                return EasyGame(playercount, players, circuit)
            elif mode == 'normal':
                return NormalGame(playercount, players, circuit)
            elif mode == 'hard':
                return HardGame(playercount, players, circuit)

    def getCardParametersAndPlaceCard(self, activePlayer):
        cardIndex = int(getInput('Choose a card index(0..5): '))
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
        output(getProbabilityOutput(self.circuit))
        confirmed = False
        while not confirmed:
            cardIndex = self.getCardParametersAndPlaceCard(activePlayer)
            output(getProbabilityOutput(self.circuit))
            if getInput('Please confirm your choice with \'Yes\'') == 'Yes':
                activePlayer.removeCard(cardIndex)
                confirmed = True
            else:
                self.circuit.data.pop(0)
            

class NormalGame(Game):
    Game
    def getGameMode(self):
        return "normal"

    def placeCard(self, activePlayer):
        output(getProbabilityOutput(self.circuit))
        activePlayer.removeCard(self.getCardParametersAndPlaceCard(activePlayer))

class HardGame(Game):
    Game
    def getGameMode(self):
        return "hard"

    def placeCard(self, activePlayer):
        activePlayer.removeCard(self.getCardParametersAndPlaceCard(activePlayer))


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def printSeparation():
        output('-------------------------------------------------------------')



game = Game.initializeGame()
print('Game mode set to ' + game.getGameMode())
print(game.printPlayers())
print(game.drawCircuit())
game.mainLoop()
