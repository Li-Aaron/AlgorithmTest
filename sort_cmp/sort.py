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
from sort_c import *
import random, time

##############################################
#---------------  CONSTANT  -----------------#
############################################## 
NumNumbers = 1000
RandomNumbers = [random.uniform(0,10) for x in range(0,NumNumbers,1)]
SortFunc = [BubbleSort,SelectSort,InsertSort,QuickSort,ShellSort,MergeSort,HeapSort]

##############################################
#----------------  FUNCTION  ----------------#
##############################################
@duration
def SortStd(NumberList):
    return sort().Sort(NumberList)

def SortTest(cSort, NumberList, StdList = None, PrintFlag = True):
    # For Python Sort Code Testing
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
        print("[Class %12s]: Time Duration: %6.6fs, Check: %s" % (cSort.__name__, result["Time"], result["Chk"]), end = ' ')
        print("SwapCount = %10d, SearchCount = %10d" \
              % (result["Swap"], result["Search"]))
        # PrintNumList(RandList)
    return result


def SortTestC(fSort, NumberList, StdList = None, PrintFlag = True):
    # For C Sort Code Testing
    result = dict()
    RandList = copy.copy(NumberList)
    startTime = time.time()
    result["Res"] = SortCaller(fSort, RandList)
    stopTime = time.time()
    result["Time"] = stopTime - startTime
    # detect weather need result check
    if not StdList:
        result["Chk"] = True
    else:
        result["Chk"] = (result["Res"] == StdList)
    if PrintFlag:
        print("[Func %13s]: Time Duration: %6.6fs, Check: %s" % (fSort.__name__, result["Time"], result["Chk"]))
        # PrintNumList(result["Res"])
    return result

##############################################
#------------------  MAIN  ------------------#
##############################################
if __name__ == '__main__':
    RandList = copy.copy(RandomNumbers)
    StdList = SortStd(RandList)
    
    print("Python Sort Test")
    RandList = copy.copy(RandomNumbers)
    for cSort in SortFunc:
        SortTest(cSort, RandList, StdList)

    print("C Sort Test")
    for fSort in SortFuncC:
        SortTestC(fSort, RandList, StdList)
        
    
