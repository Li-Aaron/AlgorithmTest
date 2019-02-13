# -*- coding:utf-8 -*-
'''
有一个方阵，其中每个单元(像素)非黑即白(非0即1)，请设计一个高效算法，找到四条边颜色相同的最大子方阵。

给定一个01方阵mat，同时给定方阵的边长n，请返回最大子方阵的边长。保证方阵边长小于等于100。
'''
class SubMatrix:
  def maxSubMatrix(self, mat, n):
    self.mat = mat
    self.n = n
    return self._maxSubMatrix(n)

  def _maxSubMatrix(self, length):
    l = self.n - length + 1
    subs = [(i, j) for j in range(l) for i in range(l)]
    for sub in subs:
      if self.isMatrix(sub, length):
        return length
    return self._maxSubMatrix(length-1)

  def isMatrix(self, sub, length):
    idxs = [sub]
    # find all indexs
    for i in range(length):
      idxs.append((sub[0],sub[1]+i))
      idxs.append((sub[0]+i,sub[1]))
      idxs.append((sub[0]+length-1,sub[1]+i))
      idxs.append((sub[0]+i,sub[1]+length-1))
    idxs = list(set(idxs))
    color = self.mat[sub[0]][sub[1]]
    for idx in idxs:
      if color != self.mat[idx[0]][idx[1]]:
        return False
    return True


# test case
mat, n = [[1,1,1],[1,0,1],[1,1,1]],3
res = 3
print(SubMatrix().maxSubMatrix(mat, n) == res)
