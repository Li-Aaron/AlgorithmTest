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
import copy

##############################################
#----------------  FUNCTION  ----------------#
##############################################
def GenRandNum(Length = 100):
    '''
    Generate Random List
    :param Length:  List Length
    :return:        Random List
    '''
    return [random.uniform(0,10) for x in range(0,Length,1)]

@duration
def SortStd(NumberList):
    '''
    Get the Standard Result of Sort (Python Based)
    :param NumberList:  Random Number List
    :return:            Standard Number List
    '''
    return sort().Sort(NumberList)

def SortTest(cSort, NumberList, StdList = None, PrintFlag = True):
    '''
    For Python Sort Code Testing
    :param cSort:       Python based Sort Class
    :param NumberList:  Random Number List
    :param StdList:     Standard Number List
    :param PrintFlag:   Print Flag
    :return:            A dictionary of Result
    '''
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
    '''
    For C Sort Code Testing
    :param fSort:       C based Sort Function
    :param NumberList:  Random Number List
    :param StdList:     Standard Number List
    :param PrintFlag:   Print Flag
    :return:            A dictionary of Result
    '''
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
    # in order to avoid changes in original list, we use copy of list to test
    print("Python Sort Test")
    RandList = GenRandNum(1000)
    StdList = SortStd(copy.copy(RandList))
    for cSort in SortFunc:
        SortTest(cSort, copy.copy(RandList), StdList)

    print("C Sort Test")
    RandList = GenRandNum(100000)
    StdList = SortStd(copy.copy(RandList))
    for fSort in SortFuncC:
        SortTestC(fSort, copy.copy(RandList), StdList)

    print("C Sort Test EX")
    RandList = GenRandNum(10000000)
    SortFuncC_Ex = [
        sort_lib.SortShell,
        sort_lib.SortQuick,
        sort_lib.SortQuick2,
        sort_lib.SortMerge,
    ]
    for fSort in SortFuncC_Ex:
        SortTestC(fSort, copy.copy(RandList))