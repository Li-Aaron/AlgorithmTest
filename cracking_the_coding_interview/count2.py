# -*- coding:utf-8 -*-
'''
请编写一个方法，输出0到n(包括n)中数字2出现了几次。

给定一个正整数n，请返回0到n的数字中2出现了几次。
'''

class Count2:
  def countNumberOf2s(self, n):
    # write code here
    cnt, d = 0, 1
    while n // d:
      cur  = n // d % 10
      low  = n - n // d * d
      high = n // (d * 10)
      if cur < 2:
        cnt += high * d
      elif cur == 2:
        cnt += high * d + low + 1
      else:
        cnt += (high + 1) * d
      d *= 10
    return cnt

# testcase
n = 22
print(Count2().countNumberOf2s(n))