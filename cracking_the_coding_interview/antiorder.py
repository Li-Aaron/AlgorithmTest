# -*- coding:utf-8 -*-
'''
有一组数，对于其中任意两个数组，若前面一个大于后面一个数字，则这两个数字组成一个逆序对。
请设计一个高效的算法，计算给定数组中的逆序对个数。

给定一个int数组A和它的大小n，请返回A中的逆序对个数。保证n小于等于5000。
'''

class AntiOrder:
  def count(self, A, n):
    self.ReversedNums = 0
    self._Sort(A, 0, n)
    return self.ReversedNums
    
  def _Sort(self, NumberList, left, right):
    '''
    Recursive inner sort function
    :param NumberList:  Number List (IN/OUT)
    :param left:      List Left Margin Index
    :param right:     List Right Margin Index
    :return:          Number List (OUT)
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
    :param NumberList:  Number List (IN/OUT)
    :param left:        Left Index
    :param middle:      Middle Index
    :param right:       Right Index
    :return:            Number List (OUT)
    '''
    NumberListMerged = []
    idxL, idxR = left, middle
    while(idxL < middle and idxR < right):
      # left < right then append left
      # right < left then append right
      if NumberList[idxL] < NumberList[idxR]:
        NumberListMerged.append(NumberList[idxL])
        idxL += 1
      else:
        NumberListMerged.append(NumberList[idxR])
        idxR += 1
        # each time, a value from right list is lover than (middle - idxL) values from left list.
        self.ReversedNums += middle - idxL 
    # rest part of left/right
    if(idxL < middle):
      NumberListMerged += NumberList[idxL:middle]
    else:
      NumberListMerged += NumberList[idxR:right]
    NumberList[left:right] = NumberListMerged
    return NumberList

# testcase
A = [1,2,3,4,5,6,7,0]
n = len(A)
res = 7
print(AntiOrder().count(A, n) == res)