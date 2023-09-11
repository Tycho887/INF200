# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 20:08:43 2023

@author: Michael
"""

import matplotlib.pyplot as plt
import numpy as np


class piece:
    def __init__(self,position,color,symbol):
        assert color in ("white","black")
        self.position = position
        self.state = color
        self.symbol = symbol
    def legal_moves(self):
        return []
    def get_lines(self):
        pass
    def get_diagonals(self):
        pass

class pawn(piece):
    def __init__(self,position,color):
        pass

class Chess_Board:
    def __init__(self):
        self.pieces = [["empty" for i in range(8)] for i in range(8)]
        self.x_axis = "a","b","c","d","e","f","g","h"
        self.y_axis = "1","2","3","4","5","6","7","8"
        self.symbols = "♔♕♗♘♙♖♚♛♝♞♟♜"

    def move(self):
        for x in self.pieces:

            print(x)
    
board = Chess_Board()

