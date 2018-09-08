# use python3
'''
sort_odd_even 的 clib 与 python function 对比
[Sort_odd_even] 排序，奇数在前偶数在后 (C lib)
@Author: AC
2018-9-8
'''
__author__ = 'AC'
from ctypes import CDLL, c_int
import os, time, copy
import random
from functools import cmp_to_key

path1 = os.getcwd()
mylib = CDLL('./Lib/sort.dll')
# mylib = CDLL(os.path.join(path1,'Lib\\CPyTcl.dll'))

sort_func = [
  mylib.sort_odd_even,
  mylib.sort_odd_even_insert,
  mylib.sort_odd_even_fast,
]
NumNumbers = 100000
RandomNumbers = [random.randint(0,NumNumbers) for x in range(0,NumNumbers,1)]

def list2array(a_list):
  # generate an array for c code
  # @param a_list: list
  # @param return: c based INPUT
  assert(isinstance(a_list, list))
  INPUT = c_int * len(a_list)
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


def sort_odd_even_py(a_list):
  # a python based sort function
  def _compare(a, b):
    if a < b:
      return -1
    if a == b:
      return 0
    else:
      return 1

  def compare(a, b):
    # a copy of compare from c code
    if ((a & 1) == (b & 1)):
      return _compare(a, b) # same parity, little first
    else:
      return _compare((b & 1), (a & 1) ) # different parity, odd first
  return sorted(a_list, key=cmp_to_key(compare))


if __name__ == '__main__':
  # run python code
  py_alist = copy.copy(RandomNumbers)
  startTime = time.time()
  standard_result = sort_odd_even_py(py_alist)
  stopTime = time.time()
  print('[Function Py] Time Duration:%2.6f'%((stopTime - startTime)))

  # run c code
  for i in range(len(sort_func)):
    c_array = list2array(RandomNumbers)
    n = len(RandomNumbers)
    # Test time passed
    startTime = time.time()
    sort_func[i](c_array, n)
    stopTime = time.time()
    py_list = array2list(c_array)
    # check result:
    res = (py_list == standard_result)
    print('[Function C_%s] Time Duration:%2.6f, check:%s'%(i,(stopTime - startTime),res))




