# -*- coding:utf-8 -*-
'''
有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶、3阶。请实现一个方法，计算小孩有多少种上楼的方式。为了防止溢出，请将结果Mod 1000000007

给定一个正整数int n，请返回一个数，代表上楼的方式数。保证n小于等于100000。
'''
class GoUpstairs:
  def countWays(self, n):
    count = [1,2,4]
    count += list(self.countWayYield(n))
    return count[n-1]

  def countWayYield(self, n):
    a, b, c = 1, 2, 4
    i = 3
    while i < n:
      a, b, c = b, c, (a + b + c)%1000000007
      yield c
      i += 1

# test case
n = 5
res = 13
print(GoUpstairs().countWays(n) == res)