from sort_py.sort_base import sort

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
            while (left < right and self.SortCmp(NumberList[right], pivot)>=0):
                self.AddSearchCount()
                right -= 1
            # self.Swap(NumberList, left, right)
            while (left < right and self.SortCmp(NumberList[left], pivot)<=0):
                self.AddSearchCount()
                left += 1
            self.Swap(NumberList, left, right)            
        self.Swap(NumberList, pivotIndex, left) # improve
        return left