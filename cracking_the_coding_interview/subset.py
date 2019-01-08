# -*- coding:utf-8 -*-
'''
请编写一个方法，返回某集合的所有非空子集。

给定一个int数组A和数组的大小int n，请返回A的所有非空子集。保证A的元素个数小于等于20，且元素互异。各子集内部从大到小排序,子集之间字典逆序排序。
'''
class Subset:
  # 返回二维[[],[],[]]
  def getSubsets(self, A, n):
    A.sort()
    res = [[]]
    for i in range(n):
      tmp = res[:]
      tmp = [[A[i]]+tmp[k] for k in range(len(tmp))]
      res = tmp + res
    return res[:-1]

# test case
A = [123,456,789]
n = 3
res = [[789,456,123],[789,456],[789,123],[789],[456,123],[456],[123]]
print(Subset().getSubsets(A, n) == res)