from sort_py.sort_base import sort

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
            if self.SortCmp(NumberList[idxL], NumberList[idxR])<0:
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