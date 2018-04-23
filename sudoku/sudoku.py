#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
sudoku gen
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

import re
import random

MAX_NUM = 9
MAX_POS = MAX_NUM * MAX_NUM

class MatList(list):
    '''
    element = {'x':int,'y':int,'mat':int,'val':int/None}
    x, y : unique
    '''
    def getListFromKey(self, key, value):
        return [mat['val'] for mat in self if mat[key] == value]

    def getVal(self, x, y):
        for mat in self:
            if mat['x'] == x and mat['y'] == y:
                return mat['val']

    def updateVal(self, x, y, value):
        for mat in self:
            if mat['x'] == x and mat['y'] == y:
                mat['val'] = value

class Sudoku(object):
    def __init__(self):
        # 这里应该还可以优化
        self.matList = MatList({'x':x,'y':y,'mat':self.getMatrixPos(x,y),'val':None} for x in range(MAX_NUM) for y in range(MAX_NUM))
        self.matList.updateVal(0, 0, random.randint(1, MAX_NUM))
        self.xyList = [[x,y] for x in range(MAX_NUM) for y in range(MAX_NUM)] # 计算对应与matList的x,y值

    def getMatrixPos(self, x, y):
        '''find (x, y) in which submat'''
        x_to_mat = {'012':'036', '345':'147', '678':'258'}
        y_to_mat = {'012':'012', '345':'345', '678':'678'}
        x_mat = [x_to_mat[x_key] for x_key in x_to_mat.keys() if re.search(str(x),x_key)][0]
        y_mat = [y_to_mat[y_key] for y_key in y_to_mat.keys() if re.search(str(y),y_key)][0]
        MatPos = int([loc for loc in x_mat if loc in y_mat][0]) # 求交集
        return MatPos

    def GroupIsValid(self, result):
        '''find out if result list is valid'''
        grp = [x for x in result if x] # remove None
        return len(grp) == len(set(grp)) # 查重

    def PositionIsValid(self, x, y):
        '''find out if position is valid'''
        ret =  self.GroupIsValid(self.matList.getListFromKey('x',x))
        ret &= self.GroupIsValid(self.matList.getListFromKey('y',y))
        ret &= self.GroupIsValid(self.matList.getListFromKey('mat',self.getMatrixPos(x,y)))
        return ret

    def FindValidVal(self, x, y):
        non_valid_val =  self.matList.getListFromKey('x',x)
        non_valid_val += self.matList.getListFromKey('y',y)
        non_valid_val += self.matList.getListFromKey('mat',self.getMatrixPos(x,y))
        valid_val = list(set(x for x in non_valid_val if x) ^ set(range(1,MAX_NUM+1)))
        random.shuffle(valid_val)
        return valid_val

    def Gen(self, rest = MAX_POS):
        self._genPos(1)
        self._removePos(rest)

    def _genPos(self, loc):
        '''recursion function cal each position'''
        # exit
        if loc >= MAX_POS:
            return 'end'

        # cal valid value for position (x, y)
        x = self.xyList[loc][0]
        y = self.xyList[loc][1]
        validVal = self.FindValidVal(x, y)

        for val in validVal:
            self.matList.updateVal(x, y, val)
            if self.PositionIsValid(x, y):
                flag = self._genPos(loc + 1)
                if flag == 'end':
                    return 'end'
        # all value not valid then erase
        self.matList.updateVal(x, y, None)
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
            self.matList.updateVal(x, y, None)

    def Display(self):
        display = ''
        for y in range(MAX_NUM):
            for x in range(MAX_NUM):
                val = self.matList.getVal(x, y)
                display += str(val) if val else ' '
                display += '|' if x in [2,5] else ' '
            display += '\n-----+-----+-----\n' if y in [2,5] else '\n'
        print display

if __name__ == '__main__':
    s = Sudoku()
    s.Gen(random.randint(40,60))
    s.Display()

