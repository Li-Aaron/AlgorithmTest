# -*- coding:utf-8 -*-
'''
有数量不限的硬币，币值为25分、10分、5分和1分，请编写代码计算n分有几种表示法。

给定一个int n，请返回n分有几种表示法。保证n小于等于100000，为了防止溢出，请将答案Mod 1000000007。
'''

class Coins:
  def countWays(self, n):
    coins = [1,5,10,25]
    dp = [0]*(n+1)
    dp[0] = 1
    for coin in coins:
      for i in range(coin,n+1):
        dp[i] = (dp[i]+dp[i-coin])%1000000007
    return dp[n]

# test case
n = 11746
res = 217265490
print(Coins().countWays(n) == res)