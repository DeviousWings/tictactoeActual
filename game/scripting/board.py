from game.scripting.terminal_service import TerminalService



class Board():
    def __init__(self):
        self._squares = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}
        self._terminal_service = TerminalService()
        
        
    def tic_board(self):
        self._boards = [self._squares]
           
        for key in self._squares:
            self._boards.append(key)
        self._boards = (f"|{self._squares[1]}|{self._squares[2]}|{self._squares[3]}|\n"
                        f"|{self._squares[4]}|{self._squares[5]}|{self._squares[6]}|\n"
                        f"|{self._squares[7]}|{self._squares[8]}|{self._squares[9]}|")
        print(self._boards)
        

    
    def check_turn(self, turn):
        if turn % 2 == 0: 
            return 'O'
        else:
            return 'X'

    def check_for_win(self):
        if   (self._squares[1] == self._squares[2] == self._squares[3]) \
            or (self._squares[4] == self._squares[5] == self._squares[6]) \
            or (self._squares[7] == self._squares[8] == self._squares[9]):
            return True
        # Handle Vertical Cases
        elif   (self._squares[1] == self._squares[4] == self._squares[7]) \
            or (self._squares[2] == self._squares[5] == self._squares[8]) \
            or (self._squares[3] == self._squares[6] == self._squares[9]):
            return True
        # Diagonal Cases
        elif (self._squares[1] == self._squares[5] == self._squares[9]) \
            or (self._squares[3] == self._squares[5] == self._squares[7]):
            return True
            
        else: return False
        
    
    
    



    
    