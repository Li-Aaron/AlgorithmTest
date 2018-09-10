from sort_py.sort_base import sort

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
                if self.SortCmp(NumberList[j], NumberList[minIdx])<0:
                    minIdx = j
            if minIdx != i:
                self.Swap(NumberList,minIdx,i)
        return NumberList
