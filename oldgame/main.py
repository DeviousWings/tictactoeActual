from helpers import draw_board
spots = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}


draw_board(spots)
        
spots[1] = "X"
spots[9] = "O"
print("Second Draw: ")
  
draw_board(spots)