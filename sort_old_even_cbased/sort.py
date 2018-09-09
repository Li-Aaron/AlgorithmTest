# use python3
'''
sort_odd_even 的 clib 与 python function 对比
[Sort_odd_even] 排序，奇数在前偶数在后 (C lib)
@Author: AC
2018-9-8
'''
__author__ = 'AC'

##############################################
#-----------------  IMPORT  -----------------#
############################################## 
from ctypes import CDLL, c_int
import os, time, copy
import random
import functools
from functools import cmp_to_key

##############################################
#----------------  CONSTANT  ----------------#
##############################################
# path1 = os.getcwd()
# mylib = CDLL(os.path.join(path1,'Lib\\CPyTcl.dll'))
mylib = CDLL('./Lib/sort.dll')


sort_func = [
  mylib.sort_odd_even,
  mylib.sort_odd_even_insert,
  mylib.sort_odd_even_fast,
]
NumNumbers = 100000
RandomNumbers = [random.randint(0,NumNumbers) for x in range(0,NumNumbers,1)]


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
    print('[Function %s] Time Duration:%2.6f'%(func.__name__,(stopTime - startTime)))
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
#---------------  FUNNCTIONS  ---------------#
##############################################
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

@duration
def sort_odd_even_py(a_list):
  # a python based sort function
  # @param a_list: list
  # @param return: sorted list
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



##############################################
#------------------  MAIN  ------------------#
##############################################
if __name__ == '__main__':
  # run python code
  py_alist = copy.copy(RandomNumbers)
  standard_result = sort_odd_even_py(py_alist)

  @res_chk(standard_result)
  def sort_odd_even_c(py_alist, fun_sel):
    # warpper for c sort function
    # @param a_list: list
    # @param fun_sel: int
    # @param return: sorted list
    c_array = list2array(py_alist)
    n = len(py_alist)
    sort_func[fun_sel](c_array, n)
    print('[%s]'%(fun_sel),end='')
    return array2list(c_array)

  # run c code
  for i in range(len(sort_func)):
    sort_odd_even_c(py_alist, i)




