import numpy as np
import random

#create an empty board
#print to screen

board = np.array([['','',''], ['','',''], ['','','']])
print(board)

#initialize a boolean variable until someone wins
repeat = True

while repeat == True:
    r = input("row number: ")
    c = input("col number: ")
    #place r,c on board 'X'
    print(board)
    #get x's by row and col
    count_row = np.count_nonzero(board == 'X', axis = 1)
    count_col = np.count_nonzero(board == 'X', axis = 0)
    if any count_row in board == 3 or count_col in board == 3:
        #then user wins
        print('You Win!')
        repeat = False
    #get comp row, col randomly
    while board[r,c] == 'X' or 'O':
        get row and col again randomly
    #place it on board 'O'
    print board
    #get o's by row and col
    comp_row = np.count_nonzero(board == 'O', axis = 1)
    comp_col = np.count_nonzero(board == 'O', axis = 0)
    if any comp_row in board == 3 or comp_col in board == 3:
        #then comp wins
        print('You Lose.')
        repeat = False
'''
Ex: 1,1
[[ , , ],
[ ,x, ],
[ , , ]]

use count non-zeros function

count_row = np.count_nonzero(myarray == 'X')

count_row = np.count_nonzero(myarray == 'X', axis = 1)
count_col = np.count_nonzero(myarray == 'X', axis = 0)
print(count_row)
print(count_col)
if any is equal to 3, then user wins
'''