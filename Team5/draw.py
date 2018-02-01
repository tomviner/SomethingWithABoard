import random
import os
import time

import board

from generate import map


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

    def draw(self):
        view = self.board[self.x:self.x+self.width, self.y:self.y+self.height]
        view.draw()

    def move(self, x, y):
        self.x += x
        self.y += y

key_map = {
    'w': (0, -1),
    'a': (-1, 0),
    's': (0, 1),
    'd': (1, 0),
}

v = View(map)
v.draw()
for i in range(1000):
    key = input('move?')
    move = key_map[key]
    v.move(*move)
    os.system('clear')
    v.draw()
    # time.sleep(0.5)




