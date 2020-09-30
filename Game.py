import sys
import abc
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
    def placeCard(self):
        pass

    def mainLoop(self):
        activePlayerIndex = 0
        while self.players[activePlayerIndex].hasCards():
            activePlayer = self.players[activePlayerIndex]
            output('Turn of ' + activePlayer.getInfo())
            output(activePlayer.getCards())
            self.placeCard()
            activePlayerIndex = activePlayerIndex + 1 % len(self.players)-1
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
        return Statevector([ 0-1j, -1+0j, 1-0j],
            dims=(Game.qibit_count,))

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
            mode = getInput('Please enter the game mode (easy, normal or hard): ')
            playercount = eval(getInput('Please enter the number of players: '))
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

    

class EasyGame(Game):
    Game
    def getGameMode(self):
        return "easy"

    def placeCard(self):
        addGateToCircuit(self.circuit, Gate.h, [0])
        pass

class NormalGame(Game):
    Game
    def getGameMode(self):
        return "normal"

    def placeCard(self):
        pass

class HardGame(Game):
    Game
    def getGameMode(self):
        return "hard"

    def placeCard(self):
        pass



game = Game.initializeGame()
print('Game mode set to ' + game.getGameMode())
print(game.printPlayers())
print(game.drawCircuit())
game.mainLoop()
