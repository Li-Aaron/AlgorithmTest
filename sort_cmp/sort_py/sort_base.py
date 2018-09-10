# -*- coding: utf-8 -*-
'''
各类sort对比
@Author: AC
2017-11-8
'''
__author__ = 'AC'

##############################################
#----------------  IMPORT  ------------------#
############################################## 
import random
import copy, time
import functools
from functools import cmp_to_key

##############################################
#---------------  DECORATORS  ---------------#
##############################################
def duration(func):
  # a decorator for time duration test
  @functools.wraps(func)
  def wrapper(*args, **kw):
    startTime = time.time()
    ret = func(*args, **kw)
    stopTime = time.time()
    print('[Function %s] Time Duration:%6.3fs'%(func.__name__,(stopTime - startTime)))
    return ret
  return wrapper

def res_chk(std_res):
  def decorator(func):
    # a decorator for time duration test
    @functools.wraps(func)
    def wrapper(*args, **kw):
      startTime = time.time()
      ret = func(*args, **kw)
      stopTime = time.time()
      res = (ret == std_res)
      print('[Function %s] Time Duration:%2.6f, check:%s'%(func.__name__,(stopTime - startTime),res))
      return ret
    return wrapper
  return decorator

##############################################
#----------------  FUNCTION  ----------------#
##############################################
def PrintNumList(NumberList, len = 5):
    # Print a long numberlist with selected header/foot length
    for num in NumberList[0:len]:
        print("%4.3f, " % num, end=' ')
    print("..., ", end=' ')
    for num in NumberList[-len:]:
        print("%4.3f, " % num, end=' ')
    print("(min = %4.3f, max = %4.3f)" % (min(NumberList), max(NumberList)))


##############################################
#-----------------  CLASS  ------------------#
##############################################

###################################
# class sort
# sort类
################################### 
class sort:
    """通用sort基类"""
    ###################################
    # Variables
    ################################### 
    __swapCount = 0
    __searchCount = 0

    ###################################
    # Swap
    # 在List中交换两数
    ################################### 
    def Swap(self, NumberList, i, j):
        tmp = NumberList[i]
        NumberList[i] = NumberList[j]
        NumberList[j] = tmp
        self.__swapCount += 1
        return NumberList

    ###################################
    # ClearCount
    # 清除统计量
    ################################### 
    def ClearCount(self):
        self.__swapCount = 0
        self.__searchCount = 0

    ###################################
    # GetCount
    # 获取统计值（打印）
    ################################### 
    def GetCount(self):
        # print "SwapCount = %10d ,\tSearchCount = %10d" % (self.__swapCount, self.__searchCount),
        return {"Swap":self.__swapCount, "Search":self.__searchCount}

    ###################################
    # AddSearchCount
    # 检索统计值加一
    ################################### 
    def AddSearchCount(self):
        self.__searchCount += 1

    ###################################
    # SortTest
    # 排序函数
    ################################### 
    def SortTest(self, NumberList):
        self.ClearCount()
        self.Sort(NumberList)
        return self.GetCount()

    ###################################
    # SortCmp
    # 排序比较方法
    ################################### 
    @staticmethod
    def SortCmp(a, b):
        if a < b:
            return -1
        if a == b:
            return 0
        else:
            return 1

    ###################################
    # Sort
    # 排序函数(内部实现)(Python自带排序)
    ###################################         
    def Sort(self, NumberList):
        NumberList = sorted(NumberList, key=cmp_to_key(self.SortCmp))
        return NumberList
