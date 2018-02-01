import board
import ising

from board import Infinity


def generate_board(size):

    map = board.Board((Infinity,Infinity))

    numpy_board = ising.ising_board((size,size))

    for i in range(size):
        for j in range(size):
            map[i,j] = numpy_board[i,j]

    return map

if __name__ == '__main__':
    b = generate_board(20)
    b[:10, :10].draw()
    # print(map[:size,:size].draw())
