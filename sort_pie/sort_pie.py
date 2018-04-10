#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
微软的烙饼排序
@Author: AC
2018-4-8
'''
__author__ = 'AC'

##############################################
#------------------import--------------------#
############################################## 
import random
import copy

##############################################
#------------------类定义--------------------#
##############################################
class PieSorting(object):

    n_search = 0
    n_exceed = 0
    n_sorted = 0

    def __init__(self, PieCnt = None, PieArray = None):
        if PieArray:
            self.PieCnt = len(PieArray)
            self.PieArray = PieArray
        elif PieCnt:
            self.PieCnt = PieCnt
            self.PieArray = range(0,PieCnt)
            random.shuffle(self.PieArray)
        else:
            raise ValueError('PieCnt and PieArray must exist once.')
        self.MaxSwap = self.PieCnt*2
        # self.MinSwap = self._calMinSwap(self.PieArray)
        self.PieArraySorted = copy.deepcopy(self.PieArray)
        self.PieArraySorted.sort()
        self.SwapSteps = []
        self.SwapStepsLoc = []
        self.SwapStepsTmp = [[] for x in range(self.PieCnt*2)]
        self.SwapStepsLocTmp = [[] for x in range(self.PieCnt*2)]

    def _calMinSwap(self, NewPieArray):
        '''
        计算下限
        如果有两个相邻的Pie就判定最小交换次数少一次
        '''
        temp = []
        for i in range(1, len(NewPieArray)):
            temp.append(NewPieArray[i] - NewPieArray[i-1])
        return self.PieCnt - 1 - temp.count(-1) - temp.count(1)

    def _isSorted(self, NewPieArray):
        return self.PieArraySorted == NewPieArray

    def _reverse(self, NewPieArray, start, end):
        '''reverse elements in NewPieArray from start to end'''
        assert start <= end
        temp = NewPieArray[start:end+1]
        temp.reverse()
        NewPieArray[start:end+1] = temp

    def Sort(self, NewPieArray, step):
        '''
        recursion function for traverse each condition of sorting pie
        :param NewPieArray: a copy of PieArray
        :param step: swap step
        :return:
        '''

        self.n_search += 1

        # step exceed max swap
        if step + self._calMinSwap(NewPieArray) >= self.MaxSwap:
        # if step + 0 >= self.MaxSwap:
            self.n_exceed += 1
            return

        # sort complete
        if self._isSorted(NewPieArray):
            if step <= self.MaxSwap:
                self.MaxSwap = step
                self.SwapSteps = copy.deepcopy(self.SwapStepsTmp[0:step])
                self.SwapStepsLoc = copy.deepcopy(self.SwapStepsLocTmp[0:step])
            self.n_sorted += 1
            return

        # recursion
        for i in range(1, self.PieCnt):
            self._reverse(NewPieArray, 0, i)
            self.SwapStepsTmp[step] = copy.deepcopy(NewPieArray)
            self.SwapStepsLocTmp[step] = i
            self.Sort(NewPieArray, step + 1)
            self._reverse(NewPieArray, 0, i)

    def OutputStatus(self):
        print('Origin Array: %s'%self.PieArray)
        print('Sorted Array: %s'%self.PieArraySorted)
        for idx in range(len(self.SwapStepsLoc)):
            print('%d : %s'%(self.SwapStepsLoc[idx],self.SwapSteps[idx]))
        print('Search Times = %d'%self.n_search)
        print('Exceed Times = %d'%self.n_exceed)
        print('Sorted Times = %d'%self.n_sorted)

    def RunSort(self):
        NewPieArray = copy.deepcopy(self.PieArray)
        self.Sort(NewPieArray, step=0)
        self.OutputStatus()


##############################################
#------------------脚本开始------------------#
##############################################
if __name__ == '__main__':
    # 主线程
    psort = PieSorting(PieCnt=8)
    psort.RunSort()





