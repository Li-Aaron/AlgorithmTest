#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
sudoku gen with numpy
@Author: AC
2018-4-23

submat(→x ↓y)
 |012|345|678
-+---+---+----
0|   |   |
1| 0 | 1 | 2
2|   |   |
-+---+---+----
3|   |   |
4| 3 | 4 | 5
5|   |   |
-+---+---+----
6|   |   |
7| 6 | 7 | 8
8|   |   |
'''

__author__ = 'AC'

import random
import numpy as np
from sudoku import Sudoku

MAX_NUM = 9
MAX_POS = MAX_NUM * MAX_NUM

class Sudoku2(Sudoku):
    def __init__(self):
        # 这里应该还可以优化
        self.matPos = np.array([[self.getMatrixPos(x,y) for y in range(MAX_NUM)] for x in range(MAX_NUM)]) # submatrix pos in mat
        self.matList = np.array([[None for y in range(MAX_NUM)] for x in range(MAX_NUM)]) # value in mat
        self.matList[0,0] = random.randint(1,MAX_NUM)

    def PositionIsValid(self, x, y):
        '''find out if position is valid'''
        ret =  self.GroupIsValid(self.matList[x, :]) # x
        ret &= self.GroupIsValid(self.matList[:, y]) # y
        ret &= self.GroupIsValid(self.matList[self.matPos == self.matPos[x,y]]) # submatrix
        return ret

    def FindValidVal(self, x, y):
        non_valid_val = self.matList[x, :]
        non_valid_val = np.append(non_valid_val, self.matList[:, y])
        non_valid_val = np.append(non_valid_val, self.matList[self.matPos == self.matPos[x,y]])
        valid_val = list(set(x for x in non_valid_val if x) ^ set(range(1,MAX_NUM+1)))
        random.shuffle(valid_val)
        return valid_val

    def _genPos(self, loc):
        '''recursion function cal each position'''
        # exit
        if loc >= MAX_POS:
            return 'end'

        # cal valid value for position (x, y)
        x, y = loc//9, loc%9
        validVal = self.FindValidVal(x, y)

        for val in validVal:
            self.matList[x,y] = val
            if self.PositionIsValid(x, y):
                flag = self._genPos(loc + 1)
                if flag == 'end':
                    return 'end'
        # all value not valid then erase
        self.matList[x,y] = None
        return

    def _removePos(self, rest = MAX_POS):
        if rest > 81 or rest < 1:
            raise ValueError('rest must in {1,81}')
        # 扣掉的数字个数
        remove_loc = set()
        while len(remove_loc) < MAX_POS - rest:
            remove_loc.add(random.randint(0, MAX_POS - 1))

        for loc in remove_loc:
            x = self.xyList[loc][0]
            y = self.xyList[loc][1]
            self.matList[x, y] = None

    def Display(self):
        display = ''
        for y in range(MAX_NUM):
            for x in range(MAX_NUM):
                val = self.matList[x,y]
                display += str(val) if val else ' '
                display += '|' if x in [2,5] else ' '
            display += '\n-----+-----+-----\n' if y in [2,5] else '\n'
        print display

if __name__ == '__main__':
    s = Sudoku()
    s.Gen(random.randint(40,60))
    s.Display()

