from sort_py.sort_base import sort

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
                    while(idx2 > 0 and self.SortCmp(target, NumberList[grp[idx2 - 1]])<0):
                        self.AddSearchCount()
                        NumberList[grp[idx2]] = NumberList[grp[idx2 - 1]]
                        idx2 -= 1
                    else:
                        # 没有进入循环也检索了一次
                        self.AddSearchCount()
                    NumberList[grp[idx2]] = target
        return NumberList