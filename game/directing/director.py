from game.scripting.board import Board
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
        # self._draw_board()
        
        while self._is_playing == True:
            self._draw_board()
            self._get_inputs()
            
    def _draw_board(self):
        # Prints the board w/ numbers
        os.system('cls' if os.name == 'nt' else 'clear')
        
        self._board.tic_board()
        
        # self._board._squares[1] = "X"
        # print("Second Draw: ")
        # print(self._board.tic_board())
        
        

    
    def _get_inputs(self):
        # self._board.check_turn()
        # self._board.make_move()
        # Reset the screen
        turn = 0
        if self._is_playing:
            # self._board.tic_board()
            # Gets input from Player
            choice = self._terminal_service.read_text("Player " + str((turn % 2) +1 ) + "'s turn: Pick your spot or press q to quit: ")
            # self._board._squares[int(choice)] = int(choice)
            if choice == 'q':
                self._is_playing = False
                #  Check if the player gave a number from 1-9

            elif str.isdigit(choice) and int(choice) in self._board._squares:
                # Check if the spot has already been taken
                if not self._board._squares[int(choice)] in {"X", "O"}:
                    # Valid input, update the board
                    turn += 1
                    self._board._squares[int(choice)] = self._board.check_turn(turn)
            
            
            # player = self._board._squares
            # move = self._board.check_turn() 
            # player[int(choice)] = move(turn)
            
            # self._board._squares[int(choice)] = choice
            # print(self._board.tic_board())
        
        

        # pass
    
