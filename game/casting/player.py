import random

from game.scripting.board import Board


class Player():
    
    def __init__(self):
       self.turn = 0
       self._board = Board()
       
    def _move(self):
        self.turn += 1
        self._board.tic_board()
