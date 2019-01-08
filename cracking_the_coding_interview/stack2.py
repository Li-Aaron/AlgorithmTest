# -*- coding:utf-8 -*-
'''
叠罗汉是一个著名的游戏，游戏中一个人要站在另一个人的肩膀上。
为了使叠成的罗汉更稳固，我们应该让上面的人比下面的人更轻一点。
现在一个马戏团要表演这个节目，为了视觉效果，我们还要求下面的人的身高比上面的人高。
请编写一个算法，计算最多能叠多少人，注意这里所有演员都同时出现。

给定一个二维int的数组actors，每个元素有两个值，分别代表一个演员的身高和体重。
同时给定演员总数n，请返回最多能叠的人数。保证总人数小于等于500。
'''
class Stack:
  def getHeight(self, actors, n):
    # height first, then weight
    A = sorted(actors, key=lambda actor:(actor[0], actor[1]))
    dp = [0] * n
    for i in range(n):
      tmp = 0
      for j in range(i)[::-1]:
        if A[i][0] > A[j][0] and A[i][1] > A[j][1] and dp[j] > tmp:
          tmp = dp[j]
      dp[i] = tmp + 1
    return max(dp)

# test case
actors = [[1,2],[2,3],[3,1],[4,5],[4,3],[5,4]]
n = len(actors)
res = 3
print(Stack().getHeight(actors,n) == res)
