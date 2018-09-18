from sort_py.sort_base import sort

class HeapSort(sort):
  """ -- 以下内容出自百度文库
  排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法，它是选择排序的一种。
  可以利用数组的特点快速定位指定索引的元素。堆分为大根堆和小根堆，是完全二叉树。
  大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。
  在数组的非降序排序中，需要使用的就是大根堆，因为根据大根堆的要求可知，最大的值一定在堆顶。
  CHILD = {2*PARENT+1, 2*PARENT+2}
  """

  def Sort(self, NumberList):
    '''
    Sort Function, Main Function
    :param NumberList:  Random Number List (IN/OUT)
    :return:      Sorted Number List (OUT)
    '''
    NumLen = len(NumberList)
    for Stop in range(NumLen-1, 0, -1):
      # Building Big Root Heap
      self._BuildHeap(NumberList, 0, Stop)
      # Make First Node Down
      self.Swap(NumberList, 0, Stop)
    return NumberList

  def _BuildHeap(self, NumberList, Start, Stop):
    '''
    Building a Big root heap, let the biggest pop up
    :param NumberList:  Number List (IN/OUT)
    :param Start:     Start Node Index
    :param Stop:      Stop Node Index
    :return:          Number List (OUT)
    '''
    for Parent in range(Stop//2, Start-1, -1):
      self._ShiftDown(NumberList, Parent, Stop)

  def _ShiftDown(self, NumberList, Parent, Boundary):
    '''
    Compare Node and Shift down parent node if child is larger
    :param NumberList:  Number List (IN/OUT)
    :param Parent:    Parent Node Index
    :param Boundary:  List Boundary
    :return:      Number List (OUT)
    '''
    cmp = self.SortCmp
    Child1 = Parent * 2 + 1
    Child2 = Parent * 2 + 2
    if (Child2 <= Boundary):
      self.AddSearchCount()
      ChildLarge = Child2 if cmp(NumberList[Child1],NumberList[Child2])<0 else Child1
      self.AddSearchCount()
      if cmp(NumberList[Parent],NumberList[ChildLarge])<0:
        self.Swap(NumberList, Parent, ChildLarge)

    elif (Child1 <= Boundary):
      self.AddSearchCount()
      if cmp(NumberList[Parent],NumberList[Child1])<0:
        self.Swap(NumberList, Parent, Child1)
        
    return NumberList