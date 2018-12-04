# -*- coding:utf-8 -*-
'''
约瑟夫问题是一个非常著名的趣题，即由n个人坐成一圈，按顺时针由1开始给他们编号。然后由第一个人开始报数，数到m的人出局。现在需要求的是最后一个出局的人的编号。

给定两个int n和m，代表游戏的人数。请返回最后一个出局的人的编号。保证n和m小于等于1000。
'''
class Joseph:
  def getResult(self, n, m):
    # write code here
    people = list(range(1, n+1))
    i = 0 # index of people
    while(len(people)>1):
      i += m - 1 # next removed people
      i %= len(people)
      people.pop(i)
    return people[0]

# testcase
n = 7
m = 3
res = 4
print(Joseph().getResult(n,m) == res)