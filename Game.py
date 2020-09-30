import sys
import abc
from abc import ABC
from quno.output import *
from quno.card import *
from quno.execution import *
from quno.player import Player


class Game(ABC):
    def __init__(self, playercount, players):
        """
        docstring
        """
        self.playercount = playercount
        self.players = players
        pass
    

    @abc.abstractmethod
    def getGameMode(self):
        return ""

    @staticmethod
    def initializeGame():   
        initialized = False
        while not initialized :
            mode = input('Please enter the game mode (easy, normal or hard): ')
            playercount = eval(input('Please enter the number of players: '))
            players = []
            for index in range (0, playercount):
                name = input('Please enter a name for player ' + str(index) + ': ')
                players.append(Player(None, name, None))
            initialized = True
            if mode == 'easy': 
                return EasyGame(playercount, players)
            elif mode == 'normal':
                return NormalGame(playercount, players)
            elif mode == 'hard':
                return HardGame(playercount, players)
            else:
                initialized = False


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
