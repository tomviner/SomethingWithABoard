import random
import os
import time

import board

from generate import generate_board
from ising import new_spin

map = generate_board(12)


class DrawingBoard(board.Board):
    filler = ["+", "-", "|", " "]
    fixes = {
        '-1': 'S',
        '1 ': 'L',
    }

    def draw(self):
        for line in self.drawn():
            chs = []
            for ch in line.split('|'):
                for val, new in self.fixes.items():
                    ch = ch.replace(val, new)
                for f in self.filler:
                    ch = ch.replace(f, '')
                chs.append(ch)
            print(''.join(chs))



# b1 = VisualInfinityBoard((board.Infinity, board.Infinity))

# for i in range(20):
#     for j in range(20):
#         b1[(i, j)] = random.choice(['Sea', 'Land'])

# b2 = b1[:10, :10]

# b2.draw()

class View:
    def __init__(self, board, x=0, y=0):
        board.__class__ = DrawingBoard
        self.board = board
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10

    @property
    def view(self):
        return self.board[self.x:self.x+self.width, self.y:self.y+self.height]

    def draw(self):
        self.view.draw()

    def move(self, x, y):
        self.x += x
        self.y += y

key_map = {
    'w': (0, -1),
    'a': (-1, 0),
    's': (0, 1),
    'd': (1, 0),
}

os.system('clear')
v = View(map)
v.draw()
for i in range(1000):
    key = input('move?')
    os.system('clear')
    move = key_map[key]
    v.move(*move)
    view = v.view
    for coord, data in view.iterdata():
        if not data:
            ns = view.neighbours(coord)
            vals = [view[coord] for coord in ns]
            ones = len([v for v in vals if v==1])
            minus_ones = len([v for v in vals if v==-1])
            print(coords, data, (ones, minus_ones))
            view[coord] = new_spin((ones, minus_ones))
    v.draw()
    # time.sleep(0.5)




