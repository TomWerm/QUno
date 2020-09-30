import sys
import abc
from abc import ABC

from qiskit import circuit
from quno.output import *
from quno.card import *
from quno.execution import *
from quno.player import Player
from qiskit.quantum_info import *


class Game(ABC):

    qibit_count = 3

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
    def initializeGame(): 
        while True :
            mode = input('Please enter the game mode (easy, normal or hard): ')
            playercount = eval(input('Please enter the number of players: '))
            players = []
            for index in range (0, playercount):
                name = input('Please enter a name for player ' + str(index) + ': ')
                goal_vector = Game.randomValue()
                output('Player ' + name + ' has the goal vector ' + str(goal_vector))
                players.append(Player(goal_vector, name, None))
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

class NormalGame(Game):
    Game
    def getGameMode(self):
        return "normal"

class HardGame(Game):
    Game
    def getGameMode(self):
        return "hard"



game = Game.initializeGame()
print('Game mode set to ' + game.getGameMode())
print(game.printPlayers())
print(game.drawCircuit())
