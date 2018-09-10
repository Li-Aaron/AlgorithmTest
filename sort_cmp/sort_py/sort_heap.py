from sort_py.sort_base import sort

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
        cmp = self.SortCmp
        Child1 = Parent * 2 + 1
        Child2 = Parent * 2 + 2
        if (Child2 <= Boundary):
            self.AddSearchCount()
            if (cmp(NumberList[Parent],NumberList[Child1])<0 or cmp(NumberList[Parent],NumberList[Child2])<0):
                self.AddSearchCount()
                if cmp(NumberList[Child1],NumberList[Child2])<0:
                    self.Swap(NumberList, Parent, Child2)
                else:
                    self.Swap(NumberList, Parent, Child1)
        elif (Child1 <= Boundary):
            self.AddSearchCount()
            if cmp(NumberList[Parent],NumberList[Child1])<0:
                self.Swap(NumberList, Parent, Child1)
        return NumberList