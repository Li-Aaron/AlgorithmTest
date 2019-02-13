# -*- coding:utf-8 -*-
'''
现有一个字典，同时给定字典中的两个字符串s和t，给定一个变换，
每次可以改变字符串中的任意一个字符，请设计一个算法，计算由s变换到t所需的最少步数，
同时需要满足在变换过程中的每个串都是字典中的串。

给定一个string数组dic，同时给定数组大小n，串s和串t，请返回由s到t变换所需的最少步数。
若无法变换到t则返回-1。保证字符串长度均小于等于10，且字典中字符串数量小于等于500。
'''
import copy

class Change:
  def countChanges(self, dic, n, s, t):
    self.s = s
    stack = [t]
    unsearched = copy.copy(dic)
    unsearched.append(s)
    unsearched = list(set(unsearched))
    unsearched = [w for w in unsearched if len(w) == len(t) ]
    ret = self._countSearch(stack, unsearched, 1)
    return ret

  def _countSearch(self, stack, unsearched, dep):
    if not unsearched or not stack:
      return -1
    newstack = []
    for t in stack:
      if self.calDistance(self.s, t) == 1:
        return dep
      for word in unsearched:
        if self.calDistance(word, t) == 1:
          newstack.append(word)
    newstack = list(set(newstack))
    for word in newstack:
      unsearched.remove(word)
    return self._countSearch(newstack, unsearched, dep+1)

  def calDistance(self, word1, word2):
    d = 0
    for idx in range(len(word1)):
      if word1[idx] != word2[idx]:
        d += 1
    return d

# test case
dic,n,s,t = ["byba","lwr","baab","rybb","aaaa","baaa","ryba","baab","ca","izv","ayba","ryac","baaa","ryaa","babb","baaa","aybb","bbab","baba","ryqc","vba","baab"],22,"ryqc","bbab"
res = 8
print(Change().countChanges(dic, n, s, t) == res)
