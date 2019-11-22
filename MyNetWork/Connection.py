'''
每个连接对象都要记录该连接的权重。
'''
from random import random
from Cell import Cell


class Connection(object):
    def __init__(self, fr_cell, to_cell, weight=random()):
        self.weight = weight
        self.fr_cell = fr_cell
        self.to_cell = to_cell
