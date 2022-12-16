from game.scripting.board import Board
# from game.casting.player import Player
from game.scripting.terminal_service import TerminalService

import os
    
class Director():
    def __init__(self):
        self._board = Board()
        self._is_playing = True
        self._terminal_service = TerminalService()
        # self._players = Player()
        # self.turn = 0
        
        
        
    
    def start_game(self):
        while self._is_playing == True:
            self._draw_board()
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            
    def _draw_board(self):
        # Prints the board w/ numbers
        self._board.tic_board()
        
        
    def _get_inputs(self):
        self._board.check_turn()
        self._board.make_move()
        # Reset the screen
        # os.system('cls' if os.name == 'nt' else 'clear')
        # choices = self._terminal_service.read_text(f"Choose a square: ")
        # choice = int(choices)
        # Choosing a square
        
        
        

        
    def _do_updates(self):
        pass
        
        
        
    def _do_outputs(self):
        pass        
    #     if self._player_win == True:
    #         self._terminal_service.write_text('That letter is correct')
    #     else:
    #         self._terminal_service.write_text('Sorry that letter is not part of this word.')

    #     if self._puzzle.can_keep_guessing() == False:
    #         self._terminal_service.write_text('You got the word!')
    #         self._puzzle.draw_word_guess()
    #         self._is_playing = False
            
    #     if self._jumper.has_parachute() == False:
    #         self.is_playing = False
    #         self._terminal_service.write_text('You suck and you lost.')