import board
import ising

from board import Infinity

size = 20

map = board.Board((Infinity,Infinity))

numpy_board = ising.ising_board((size,size))

for i in range(size):
    for j in range(size):
        map[i,j] = numpy_board[i,j]

print(map[:size,:size].draw())
