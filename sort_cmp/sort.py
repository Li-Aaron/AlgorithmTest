# -*- coding: utf-8 -*-
'''
各类sort对比
@Author: AC
2017-11-8
'''
__author__ = 'AC'

##############################################
#------------------import--------------------#
############################################## 
import random
import copy, time

##############################################
#------------------常量定义------------------#
##############################################
if __name__ == '__main__':
    # 生成100个随机数
    NumNumbers = 300
    RandomNumbers = [random.uniform(0,10) for x in range(0,NumNumbers,1)]

##############################################
#------------------函数定义------------------#
##############################################

###################################
# PrintNumList
# 打印长数组
###################################
def PrintNumList(NumberList, len = 5):
    for num in NumberList[0:len]:
        print "%4.3f, " % num,
    print "..., ",
    for num in NumberList[-len:]:
        print "%4.3f, " % num,
    print "(min = %4.3f, max = %4.3f)" % (min(NumberList), max(NumberList))

###################################
# SortTestAll
# 排序测试
###################################
def SortTestAll(cSort, NumberList, PrintFlag = True):
    NumberListCopy = copy.copy(NumberList)
    startTime = time.time()
    result = cSort().SortTest(NumberListCopy)
    stopTime = time.time()
    result["Time"] = stopTime - startTime
    if PrintFlag:
        print "%s:\t" % cSort.__name__,
        print "SwapCount = %10d ,\tSearchCount = %10d,\tTime Used: %6.3fs" \
              % (result["Swap"], result["Search"],result["Time"])
        PrintNumList(NumberListCopy, len=2)
        print ""

    return result


##############################################
#------------------类定义--------------------#
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
    # BubbleSort
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
    # Sort
    # 排序函数(内部实现)(Python自带排序)
    ###################################         
    def Sort(self, NumberList):
        NumberList.sort()
        return NumberList

###################################
# class BubbleSort (基类sort)
# 冒泡排序，相邻两数，A>B则交换
################################### 
class BubbleSort(sort):
    """冒泡排序，相邻两数，A>B则交换"""

    ###################################
    # Sort
    # 排序函数(内部实现)
    ###################################         
    def Sort(self, NumberList):
        for i in range(0,len(NumberList)):
            for j in range(0,len(NumberList)-1):
                self.AddSearchCount()
                if NumberList[j]>NumberList[j+1]:
                    self.Swap(NumberList,j,j+1)
        return NumberList

###################################
# class SelectSort (基类sort)
# 选择排序，依次找到最小值并交换
################################### 
class SelectSort(sort):
    """选择排序，依次找到最小值并交换"""

    ###################################
    # Sort
    # 排序函数(内部实现)
    ###################################         
    def Sort(self, NumberList):
        for i in range(0,len(NumberList)-1):
            minIdx = i
            for j in range(i+1,len(NumberList)):
                self.AddSearchCount()
                if NumberList[j]<NumberList[minIdx]:
                    minIdx = j
            if minIdx != i:
                self.Swap(NumberList,minIdx,i)
        return NumberList

###################################
# class InsertSort (基类sort)
# 插入排序，从第二个开始找啊到的第一个比自己小的值插在后面
################################### 
class InsertSort(sort):
    """插入排序，从第二个开始找啊到的第一个比自己小的值插在后面"""

    ###################################
    # Sort
    # 排序函数(内部实现)
    ###################################         
    def Sort(self, NumberList):
        for i in range(1,len(NumberList)):
            target = NumberList[i]
            j = i
            while (j > 0 and target < NumberList[j-1]):
                self.AddSearchCount()
                NumberList[j] = NumberList[j-1]
                j -= 1
            else:
                # 没有进入循环也检索了一次
                self.AddSearchCount()
            NumberList[j] = target
        return NumberList

###################################
# class QuickSort (基类sort)
# 快速排序（二分分治，将一个数组按照一个基准数分割，比基准数大的放基准数的右边，小的放左边。）
################################### 
class QuickSort(sort):
    """快速排序（二分分治，将一个数组按照一个基准数分割，比基准数大的放基准数的右边，小的放左边。）"""

    ###################################
    # Sort
    # 排序函数(内部实现)
    ################################### 
    def Sort(self, NumberList):
        self.__Sort(NumberList, 0, len(NumberList)-1)
        return NumberList

    ###################################
    # __Sort
    # 排序函数（递归）
    ###################################         
    def __Sort(self, NumberList, left, right):
        if (left >= right):
            # 递归的终止条件
            return NumberList
        pivotIndex = self.__SortPartition(NumberList, left, right) # first time ( pivotIndex位置数字确定不再排序 )
        self.__Sort(NumberList, left, pivotIndex-1) # ( 左右分别再次排序 )
        self.__Sort(NumberList, pivotIndex+1, right)
        return NumberList

    def __SortPartition(self, NumberList, left, right):
        # pivot: 中心点
        pivot = NumberList[left]
        pivotIndex = left

        while (left < right):
            while (left < right and NumberList[right] >= pivot):
                self.AddSearchCount()
                right -= 1
            # self.Swap(NumberList, left, right)
            while (left < right and NumberList[left] <= pivot):
                self.AddSearchCount()
                left += 1
            self.Swap(NumberList, left, right)            
        self.Swap(NumberList, pivotIndex, left) # improve
        return left

###################################
# class ShellSort (基类sort)
# 希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
###################################
class ShellSort(sort):
    """ -- 以下内容出自百度文库
    希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
    希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。
    希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
    随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
    """

    ###################################
    # Sort
    # 排序函数(内部实现)
    ###################################
    def Sort(self, NumberList):
        NumLen = len(NumberList)
        step = NumLen # 间距初始值
        while (step >= 1):
            step = step // 2
            for i in range(0, step):
                # 分组
                grp = range(i, NumLen, step)
                # 以下同插入排序
                for idx1 in range(1, len(grp)):
                    target = NumberList[grp[idx1]]
                    idx2 = idx1
                    while(idx2 > 0 and target < NumberList[grp[idx2 - 1]]):
                        self.AddSearchCount()
                        NumberList[grp[idx2]] = NumberList[grp[idx2 - 1]]
                        idx2 -= 1
                    else:
                        # 没有进入循环也检索了一次
                        self.AddSearchCount()
                    NumberList[grp[idx2]] = target
        return NumberList

###################################
# class MergeSort (基类sort)
# 归并排序（Merge Sort）是建立在归并操作上的一种有效的排序算法，该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
###################################
class MergeSort(sort):
    """ -- 以下内容出自百度文库
    归并排序（MERGE-SORT）是建立在归并操作上的一种有效的排序算法，
    该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
    将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，
    再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。
    """

    ###################################
    # Sort
    # 排序函数(内部实现)
    ###################################
    def Sort(self, NumberList):
        self.__Sort(NumberList, 0, len(NumberList))
        return NumberList

    ###################################
    # __Sort
    # 排序函数（递归）
    ###################################
    def __Sort(self, NumberList, left, right):
        if (right - left <= 1):
            # 递归的终止条件
            return NumberList
        middle = (left + right) // 2
        self.__Sort(NumberList, left, middle)
        self.__Sort(NumberList, middle, right)
        self.__Merge(NumberList, left, middle, right)

    def __Merge(self, NumberList, left, middle, right):
        '''数组的两部分Merge
        [left:middle] 与 [middle:right] merge
        '''
        NumberListMerged = []
        idxL, idxR = left, middle
        while(idxL < middle and idxR < right):
            self.AddSearchCount()
            if (NumberList[idxL] < NumberList[idxR]):
                NumberListMerged.append(NumberList[idxL])
                idxL += 1
            else:
                NumberListMerged.append(NumberList[idxR])
                idxR += 1
        self.AddSearchCount()
        # 剩余部分
        if(idxL < middle):
            NumberListMerged += NumberList[idxL:middle]
        else:
            NumberListMerged += NumberList[idxR:right]
        NumberList[left:right] = NumberListMerged
        return NumberList

###################################
# class HeapSort (基类sort)
# 堆排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法，它是选择排序的一种。
###################################
class HeapSort(sort):
    """ -- 以下内容出自百度文库
    排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法，它是选择排序的一种。
    可以利用数组的特点快速定位指定索引的元素。堆分为大根堆和小根堆，是完全二叉树。
    大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。
    在数组的非降序排序中，需要使用的就是大根堆，因为根据大根堆的要求可知，最大的值一定在堆顶。
    CHILD = {2*PARENT+1, 2*PARENT+2}
    """

    ###################################
    # Sort
    # 排序函数(内部实现)
    ###################################
    def Sort(self, NumberList):
        NumLen = len(NumberList)
        for Stop in range(NumLen-1, 0, -1):
            self.__BuildHeap(NumberList, 0, Stop)
            self.Swap(NumberList, 0, Stop)
        return NumberList

    def __BuildHeap(self, NumberList, Start, Stop):
        '''建立大根堆，让最大的浮上来'''
        for Parent in range(Stop//2, Start-1, -1):
            self.__ShiftDown(NumberList, Parent, Stop)

    def __ShiftDown(self, NumberList, Parent, Boundary):
        '''节点比较'''
        Child1 = Parent * 2 + 1
        Child2 = Parent * 2 + 2
        if (Child2 <= Boundary):
            self.AddSearchCount()
            if (NumberList[Parent]<NumberList[Child1] or NumberList[Parent]<NumberList[Child2]):
                self.AddSearchCount()
                if (NumberList[Child1]<NumberList[Child2]):
                    self.Swap(NumberList, Parent, Child2)
                else:
                    self.Swap(NumberList, Parent, Child1)
        elif (Child1 <= Boundary):
            self.AddSearchCount()
            if (NumberList[Parent]<NumberList[Child1]):
                self.Swap(NumberList, Parent, Child1)
        return NumberList

##############################################
#------------------脚本开始------------------#
##############################################
if __name__ == '__main__':
    # 主线程
    PrintNumList(RandomNumbers)
    SortList = [BubbleSort,SelectSort,InsertSort,QuickSort,ShellSort,MergeSort,HeapSort]
    for cSort in SortList:
        SortTestAll(cSort, RandomNumbers, PrintFlag=True)
