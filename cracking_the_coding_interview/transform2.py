'''
编写一个函数，确定需要改变几个位，才能将整数A转变成整数B。

给定两个整数int A，int B。请返回需要改变的数位个数。
'''

class Transform:
  def calcCost(self, A, B):
    tmp = A ^ B
    cnt = 0
    while tmp:
      if tmp & 0b1 == 1:
        cnt += 1
      tmp >>= 1
    return cnt


# test case
A = 10
B = 5
res = 4
print(Transform().calcCost(A, B) == res)