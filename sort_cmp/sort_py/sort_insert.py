from sort_py.sort_base import sort

###################################
# class InsertSort (基类sort)
# 插入排序，从第二个开始找到的第一个比自己小的值插在后面（其他依次后移）
################################### 
class InsertSort(sort):
    """插入排序，从第二个开始找到的第一个比自己小的值插在后面"""

    ###################################
    # Sort
    # 排序函数(内部实现)
    ###################################         
    def Sort(self, NumberList):
        for i in range(1,len(NumberList)):
            target = NumberList[i]
            j = i
            while (j > 0 and self.SortCmp(target, NumberList[j-1])<0):
                self.AddSearchCount()
                NumberList[j] = NumberList[j-1]
                j -= 1
            else:
                # 没有进入循环也检索了一次
                self.AddSearchCount()
            NumberList[j] = target
        return NumberList