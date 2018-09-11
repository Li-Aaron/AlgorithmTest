from sort_py.sort_base import sort
from sort_py.sort_insert import InsertSort

class QuickSort(sort):
    """快速排序（二分分治，将一个数组按照一个基准数分割，比基准数大的放基准数的右边，小的放左边。）"""

    def Sort(self, NumberList):
        '''
        Sort Function, Main Function
        :param NumberList:  Random Number List (IN/OUT)
        :return:            Sorted Number List (OUT)
        '''
        self._Sort(NumberList, 0, len(NumberList)-1)
        return NumberList

    def _Sort(self, NumberList, left, right):
        '''
        Recursive inner sort function
        :param NumberList:  Number List (IN/OUT)
        :param left:        List Left Margin Index
        :param right:       List Right Margin Index
        :return:            Number List (OUT)
        '''
        if (left >= right):
            # Terminate Condition
            return NumberList
        # first time ( pivotIndex is fixed and no need to sort )
        pivotIndex = self._SortPartition(NumberList, left, right)
        self._Sort(NumberList, left, pivotIndex-1) # sort left part
        self._Sort(NumberList, pivotIndex+1, right) # sort right part
        return NumberList

    def _SortPartition(self, NumberList, left, right):
        '''
        Make First Value Pivot and do sort like [Smaller|Pivot|Larger]
        :param NumberList:  Random Number List (IN/OUT)
        :param left:        Left Index
        :param right:       Right Index
        :return:            Pivot Index
        '''
        # pivot: 中心点
        pivot = NumberList[left]
        pivotIndex = left

        while (left < right):
            # find next R < Pivot
            while (left < right and self.SortCmp(NumberList[right], pivot)>=0):
                self.AddSearchCount()
                right -= 1
            # find next L > Pivot
            while (left < right and self.SortCmp(NumberList[left], pivot)<=0):
                self.AddSearchCount()
                left += 1
            self.Swap(NumberList, left, right)            
        self.Swap(NumberList, pivotIndex, left) # improve
        return left


class QuickSort2(QuickSort, InsertSort):
    """快速排序+插入排序"""

    def Sort(self, NumberList):
        '''
        Sort Function, Main Function
        :param NumberList:  Random Number List (IN/OUT)
        :return:            Sorted Number List (OUT)
        '''
        self._Sort(NumberList, 0, len(NumberList)-1)
        return NumberList

    def _Sort(self, NumberList, left, right):
        '''
        Recursive inner sort function
        :param NumberList:  Number List (IN/OUT)
        :param left:        List Left Margin Index
        :param right:       List Right Margin Index
        :return:            Number List (OUT)
        '''
        if (right - left < 10):
            # Terminate Condition
            self._SortInsert(NumberList, left, right+1)
            return NumberList
        # first time ( pivotIndex is fixed and no need to sort )
        pivotIndex = self._SortPartition(NumberList, left, right)
        self._Sort(NumberList, left, pivotIndex-1) # sort left part
        self._Sort(NumberList, pivotIndex+1, right) # sort right part
        return NumberList

