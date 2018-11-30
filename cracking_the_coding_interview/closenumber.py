# -*- coding:utf-8 -*-
'''
有一个正整数，请找出其二进制表示中1的个数相同、且大小最接近的那两个数。(一个略大，一个略小)

给定正整数int x，请返回一个vector，代表所求的两个数（小的在前）。保证答案存在。
'''

class CloseNumber:
  def getCloseNumber(self, x):
    return [self.getSmallerNumber(x), self.getLargerNumber(x)]

  def getSmallerNumber(self, x):
    # last '10' to '01'
    if x < 2:
      return None
    n = 0
    while x>>n & 0b11 != 0b10:
      n += 1
    x ^= (0b11 << n)
    # '0' after '10' shift to end
    cnt = 0
    for idx in range(n):
      if x >> idx & 1 == 0:
        cnt += 1
      # all 0 convert to 1
      x |= 1 << idx
    # put 0 to end
    x ^= 2**cnt-1
    return x

  def getLargerNumber(self, x):
    # last '01' to '10'
    if x < 1:
      return None
    n = 0
    while x>>n & 0b11 != 0b01:
      n += 1
    x ^= (0b11 << n)
    # '1' after '01' shift to end
    cnt = 0
    for idx in range(n):
      if x >> idx & 1 == 1:
        cnt += 1
      # all 1 convert to 0
      x &= ~(1 << idx)
    # put 1 to end
    x ^= 2**cnt-1
    return x

# testcase
x = 2651
res = [2647, 2653]
print(CloseNumber().getCloseNumber(x) == res)