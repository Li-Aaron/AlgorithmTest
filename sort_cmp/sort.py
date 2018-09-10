# -*- coding: utf-8 -*-
'''
各类sort对比运行程序
@Author: AC
2018-9-10
'''
__author__ = 'AC'

##############################################
#----------------  IMPORT  ------------------#
############################################## 
from sort_py import *
import random, time

##############################################
#---------------  CONSTANT  -----------------#
############################################## 
NumNumbers = 300
RandomNumbers = [random.uniform(0,10) for x in range(0,NumNumbers,1)]
SortFunc = [BubbleSort,SelectSort,InsertSort,QuickSort,ShellSort,MergeSort,HeapSort]

##############################################
#----------------  FUNCTION  ----------------#
##############################################
@duration
def SortStd(NumberList):
    return sort().Sort(NumberList)

def SortTest(cSort, NumberList, StdList = None, PrintFlag = True):
    RandList = copy.copy(NumberList)
    startTime = time.time()
    result = cSort().SortTest(RandList)
    stopTime = time.time()
    result["Time"] = stopTime - startTime
    # detect weather need result check
    if not StdList:
        result["Chk"] = True
    else:
        result["Chk"] = (RandList == StdList)
    if PrintFlag:
        print("[Class %12s]: Time Duration: %6.3fs, Check: %s" % (cSort.__name__, result["Time"], result["Chk"]), end = ' ')
        print("SwapCount = %10d, SearchCount = %10d" \
              % (result["Swap"], result["Search"]))
        # PrintNumList(RandList)
    return result

##############################################
#------------------  MAIN  ------------------#
##############################################
if __name__ == '__main__':
    RandList = copy.copy(RandomNumbers)
    StdList = SortStd(RandList)
    
    RandList = copy.copy(RandomNumbers)
    for cSort in SortFunc:
        SortTest(cSort, RandList, StdList)
        
