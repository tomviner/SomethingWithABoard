import random
import os
import time

import board
from colorama import Fore, Back, Style

from generate import generate_board
from ising import new_spin

map = generate_board(20)


class DrawingBoard(board.Board):
    filler = ["+", "-", "|", " "]
    fixes = {
        '-1': Fore.BLUE + '💧',
        '1 ': Fore.GREEN + '📗',
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
            print(''.join(chs), end='')
            print(Style.RESET_ALL)


class View:
    def __init__(self, board, width, height, x=0, y=0):
        board.__class__ = DrawingBoard
        self.board = board
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def view(self):
        return self.board[self.x:self.x+self.width, self.y:self.y+self.height]

    def draw(self):
        self.view.draw()

    def move(self, x, y):
        self.x = max(self.x + x, 0)
        self.y = max(self.y + y, 0)

key_map = {
    'w': (0, -1),
    'a': (-1, 0),
    's': (0, 1),
    'd': (1, 0),
}

from nonblock_input import getch

kgen = getch(0.1)

os.system('clear')
v = View(map, 50, 10)
v.draw()
while True:
    key = next(kgen)
    if not key:
        continue
    # key = input('move?')
    move = key_map[key]
    v.move(*move)
    view = v.view
    for local_coord in iter(view):
        coord = view._to_global(local_coord)
        data = v.board[coord]
        if not data:
            ns = v.board.neighbours(coord)
            vals = [v.board[coord] for coord in ns]
            ones = len([v for v in vals if v==1])
            minus_ones = len([v for v in vals if v==-1])
            v.board[coord] = new_spin((ones, minus_ones))
    os.system('clear')
    v.draw()
    time.sleep(0.01)




