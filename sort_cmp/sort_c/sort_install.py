# -*- coding: utf-8 -*-
'''
导入C DLL库
@Author: AC
2018-9-10
'''
__author__ = 'AC'

##############################################
#----------------  IMPORT  ------------------#
############################################## 
from ctypes import CDLL, c_int, c_double
import functools

INT32 = c_int
FLT64 = c_double

##############################################
#----------------  C FUNC  ------------------#
############################################## 
sort_lib = CDLL('./sort_c/Lib/sort.dll')

SortFuncC = [
  sort_lib.SortBubble,
  sort_lib.SortSelect,
  sort_lib.SortInsert,
  sort_lib.SortShell,
  sort_lib.SortQuick,
  sort_lib.SortQuick2,
]


##############################################
#---------------  FUNCTION  -----------------#
############################################## 
def list2array(a_list):
  # generate an array for c code
  # @param a_list: list
  # @param return: c based INPUT
  assert(isinstance(a_list, list))
  INPUT = FLT64 * len(a_list)
  a_array = INPUT()
  i = 0
  for value in a_list:
    a_array[i] = value
    i += 1
  return a_array

def array2list(a_array):
  # generate an list from c code array
  # @param a_array: c based INPUT
  # @param return: list
  a_list = []
  for i in range(len(a_array)):
    a_list.append(a_array[i])
  return a_list

def SortCaller(func, py_list):
  # using to call a c sort function
  c_list = list2array(py_list)
  func(c_list, len(py_list))
  return array2list(c_list)


if __name__ == '__main__':
  import random
  NumNumbers = 8
  RandomNumbers = [random.uniform(0,10) for x in range(0,NumNumbers,1)]
  print(RandomNumbers)
  for func in SortFuncC:
    print("%12s"%func.__name__, end=' ')
    print(SortCaller(func, RandomNumbers))
