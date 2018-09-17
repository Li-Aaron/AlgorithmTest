from sort_py.sort_base import sort

class MergeSort(sort):
    """ -- 以下内容出自百度文库
    归并排序（MERGE-SORT）是建立在归并操作上的一种有效的排序算法，
    该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
    将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，
    再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。
    """

    def Sort(self, NumberList):
        '''
        Sort Function, Main Function
        :param NumberList:  Random Number List (IN/OUT)
        :return:            Sorted Number List (OUT)
        '''
        self._Sort(NumberList, 0, len(NumberList))
        return NumberList

    def _Sort(self, NumberList, left, right):
        '''
        Recursive inner sort function
        :param NumberList:  Number List (IN/OUT)
        :param left:        List Left Margin Index
        :param right:       List Right Margin Index
        :return:            Number List (OUT)
        '''
        if (right - left <= 1):
            # Terminate Condition
            # if right - left <= 0, when right - left = 1, the
            # middle will always be left
            return NumberList
        middle = (left + right) // 2
        self._Sort(NumberList, left, middle)
        self._Sort(NumberList, middle, right)
        self._Merge(NumberList, left, middle, right)

    def _Merge(self, NumberList, left, middle, right):
        '''
        Merge NumberList[left:middle] and NumberList [middle:right]
        :param NumberList:      Number List (IN/OUT)
        :param left:            Left Index
        :param middle:          Middle Index
        :param right:           Right Index
        :return:                Number List (OUT)
        '''
        NumberListMerged = []
        idxL, idxR = left, middle
        while(idxL < middle and idxR < right):
            self.AddSearchCount()
            # left < right then append left
            # right < left then append right
            if self.SortCmp(NumberList[idxL], NumberList[idxR])<0:
                NumberListMerged.append(NumberList[idxL])
                idxL += 1
            else:
                NumberListMerged.append(NumberList[idxR])
                idxR += 1
        self.AddSearchCount()
        # rest part of left/right
        if(idxL < middle):
            NumberListMerged += NumberList[idxL:middle]
        else:
            NumberListMerged += NumberList[idxR:right]
        NumberList[left:right] = NumberListMerged
        return NumberList