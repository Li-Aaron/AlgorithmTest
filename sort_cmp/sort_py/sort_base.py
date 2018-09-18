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
import time
import functools
from functools import cmp_to_key

##############################################
#---------------  DECORATORS  ---------------#
##############################################
def duration(func):
  '''
  a decorator for time duration test
  :param func:  target function
  :return:      target function return
  '''
  @functools.wraps(func)
  def wrapper(*args, **kw):
    startTime = time.time()
    ret = func(*args, **kw)
    stopTime = time.time()
    print('[Function %s] Time Duration:%6.6fs'%(func.__name__,(stopTime - startTime)))
    return ret
  return wrapper

def res_chk(std_res):
  '''
  a decorator for result check test
  :param std_res:  standard result
  :return:         target function return
  '''
  def decorator(func):
    # a decorator for time duration test
    @functools.wraps(func)
    def wrapper(*args, **kw):
      startTime = time.time()
      ret = func(*args, **kw)
      stopTime = time.time()
      res = (ret == std_res)
      print('[Function %s] Time Duration:%6.6f, check:%s'%(func.__name__,(stopTime - startTime),res))
      return ret
    return wrapper
  return decorator

##############################################
#----------------  FUNCTION  ----------------#
##############################################
def PrintNumList(NumberList, len = 5):
  '''
  Print a long numberlist with selected Header/Footer length
  :param NumberList:  Number List
  :param len:         Header/Footer length
  :return:
  '''
  for num in NumberList[0:len]:
    print("%4.3f, " % num, end=' ')
  print("..., ", end=' ')
  for num in NumberList[-len:]:
    print("%4.3f, " % num, end=' ')
  print("(min = %4.3f, max = %4.3f)" % (min(NumberList), max(NumberList)))


##############################################
#-----------------  CLASS  ------------------#
##############################################
class sort:
  """General Sort Basis"""

  __swapCount = 0
  __searchCount = 0

  def Swap(self, NumberList, i, j):
    '''
    Swap two numbers in list
    :param NumberList:  Number List (IN/OUT)
    :param i:           index i
    :param j:           index j
    :return:            Number List
    '''
    tmp = NumberList[i]
    NumberList[i] = NumberList[j]
    NumberList[j] = tmp
    self.__swapCount += 1
    return NumberList

  def ClearCount(self):
    '''
    Clear the Static Counts
    :return: void
    '''
    self.__swapCount = 0
    self.__searchCount = 0

  def GetCount(self):
    '''
    Get the Static Counts for Print
    :return: Static Count dict
    '''
    # print "SwapCount = %10d ,\tSearchCount = %10d" % (self.__swapCount, self.__searchCount),
    return {"Swap":self.__swapCount, "Search":self.__searchCount}

  def AddSearchCount(self):
    '''
    Search Count Plus One
    '''
    self.__searchCount += 1

  def SortTest(self, NumberList):
    '''
    Test Function of Sort Method
    :param NumberList:  Random Number List
    :return:            Static Count dict
    '''
    self.ClearCount()
    self.Sort(NumberList)
    return self.GetCount()

  @staticmethod
  def SortCmp(a, b):
    '''
    Compare Method, using for setting the rule of compare
    :param a:   value a
    :param b:   value b
    :return:    -1/0/1
    '''
    if a < b:
      return -1
    if a == b:
      return 0
    else:
      return 1

  def Sort(self, NumberList):
    '''
    Sort Function, Main Function
    :param NumberList:  Random Number List (IN/OUT)
    :return:            Sorted Number List (OUT)
    '''
    NumberList = sorted(NumberList, key=cmp_to_key(self.SortCmp))
    return NumberList
