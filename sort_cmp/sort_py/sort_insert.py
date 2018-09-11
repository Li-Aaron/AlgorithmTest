from sort_py.sort_base import sort

class InsertSort(sort):
    """插入排序，从第二个开始找到的第一个比自己小的值插在后面"""

    def Sort(self, NumberList):
        '''
        Sort Function, Main Function
        :param NumberList:  Random Number List (IN/OUT)
        :return:            Sorted Number List (OUT)
        '''
        return self._SortInsert(NumberList, 0, len(NumberList))

    def _SortInsert(self, NumberList, left, right):
        '''
        Inner Insert Sort
        :param NumberList:  Random Number List (IN/OUT)
        :param left:        List Left Margin Index
        :param right:       List Right Margin Index
        :return:            Sorted Number List (OUT)
        '''
        for i in range(left+1, right):
            target = NumberList[i]
            j = i
            while (j > 0 and self.SortCmp(target, NumberList[j-1])<0):
                self.AddSearchCount()
                NumberList[j] = NumberList[j-1]
                j -= 1
            else:
                # Searched once even if not in the loop
                self.AddSearchCount()
            NumberList[j] = target
        return NumberList