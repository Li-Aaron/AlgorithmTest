# -*- coding:utf-8 -*-
'''
n皇后问题
'''
class Queens:
  def nQueens(self, n):
    # use 1-deminsion array to place a queen
    # 0 = no queen, 1 = has queen
    self.column = [0]*n
    # right   left
    # [0|1|2] [2|3|4]
    # [1|2|3] [1|2|3]
    # [2|3|4] [0|1|2]
    self.leftslash = [0]*(2*n-1)
    self.rightslash = [0]*(2*n-1)
    self.count = 0 # all posissble ways
    self.QueenRollback(0, n)
    return self.count
  
  # roll back func, from current row to n row
  def QueenRollback(self, row, n):
    for col in range(n):
      idxl = (n-row-1)+col
      idxr = row+col
      if (self.column[col] | self.leftslash[idxl] | self.rightslash[idxr]) == 0:
        # if no queen, place queen
        self.column[col] = self.leftslash[idxl] = self.rightslash[idxr] = 1
        if row == n - 1:
          self.count += 1 # last row placed
        else:
          self.QueenRollback(row+1, n) # next row          
        # remove this queen
        self.column[col] = self.leftslash[idxl] = self.rightslash[idxr] = 0
    return

# testcase
n = 10
res = 724
print(Queens().nQueens(n))
print(Queens().nQueens(n) == res)