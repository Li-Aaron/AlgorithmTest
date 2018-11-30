# -*- coding:utf-8 -*-
'''
请编写一个方法，实现整数的乘法、减法和除法运算(这里的除指整除)。只允许使用加号。

给定两个正整数int a,int b,同时给定一个int type代表运算的类型，1为求a ＊ b，0为求a ／ b，-1为求a － b。请返回计算的结果，保证数据合法且结果一定在int范围内。
'''

class AddSubstitution:
  def calc(self, a, b, t):
    if t == 1:
      return self.mul(a, b)
    elif t == 0:
      return self.div(a, b)
    elif t == -1:
      return self.sub(a, b)

  def sub(self,a,b):
    return a + (~b) + 1

  def mul(self,a,b):
    res = 0
    if a == 0 or b == 0:
      return res
    if b < 0:
      b = ~b + 1
      a = ~a + 1
    for _ in range(b):
      res += a
    return res

  def div(self,a,b):
    if a < 0:
      a = ~a + 1
      a_t = -1
    else:
      a_t = 1
    if b < 0:
      b = ~b + 1
      t = self.mul(-1, a_t)
    else:
      t = a_t
    cnt = 0
    while a >= b:
      a = self.sub(a, b)
      cnt += 1
    return self.mul(cnt, t)

# test case
x = 513
y = 25
print(AddSubstitution().calc(x, y, 1) == x * y)
print(AddSubstitution().calc(x, y, 0) == x // y)
print(AddSubstitution().calc(x, y, -1) == x - y)