from game.scripting.board import Board
from game.scripting.terminal_service import TerminalService

import os
    
class Director():
    def __init__(self):
        self._board = Board()
        self._is_playing, self.complete = True, False
        self._terminal_service = TerminalService()
        self.turn = 0
        self.prev_turn = -1
        
        
        
        
    
    def start_game(self):
        # self._draw_board()
        
        while self._is_playing == True:
            self._draw_board()
            self._get_inputs()
            self._get_winner()
            
    def _draw_board(self):
        # Reset the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Prints the board w/ numbers
        self._board.tic_board()
        
        # Force changes square
        # self._board._squares[1] = "X"
        # print("Second Draw: ")
        # print(self._board.tic_board())
        
        

    
    def _get_inputs(self):

        if self.prev_turn == self.turn:
            print("Invalid spot selected, please pick another.")
        
        self.prev_turn = self.turn
        
        if self._is_playing:
            # self._board.tic_board()
            # Gets input from Player
            choice = self._terminal_service.read_text("Player " + str((self.turn % 2) +1 ) + "'s turn: Pick your spot or press q to quit: ")
            # self._board._squares[int(choice)] = int(choice)
            if choice == 'q':
                self._is_playing = False
                #  Check if the player gave a number from 1-9

            elif str.isdigit(choice) and int(choice) in self._board._squares:
                # Check if the spot has already been taken
                if not self._board._squares[int(choice)] in {"X", "O"}:
                    # Valid input, update the board
                    self.turn += 1
                    self._board._squares[int(choice)] = self._board.check_turn(self.turn)

        
        

    def _get_winner(self):
        if self._board.check_for_win():
            self._is_playing, self.complete = False, True
        if self.turn > 8: self._is_playing = False
        os.system('cls' if os.name == 'nt' else 'clear')
        self._board.tic_board()
        if self.complete:
            if self._board.check_turn(self.turn) == 'X': print("Player 1 Wins!")
            else: print("Player 2 Wins!")
        print("Thanks for playing!")
        
    
