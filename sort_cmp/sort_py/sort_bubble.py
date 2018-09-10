from sort_py.sort_base import sort

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
                if self.SortCmp(NumberList[j],NumberList[j+1])>0:
                    self.Swap(NumberList,j,j+1)
        return NumberList