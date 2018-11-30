# -*- coding:utf-8 -*-
'''
利用字符重复出现的次数，编写一个方法，实现基本的字符串压缩功能。比如，字符串“aabcccccaaa”经压缩会变成“a2b1c5a3”。若压缩后的字符串没有变短，则返回原先的字符串。

给定一个string iniString为待压缩的串(长度小于等于10000)，保证串内字符均由大小写英文字母组成，返回一个string，为所求的压缩后或未变化的串。
'''

class Zipper:
  def zipString(self, iniString):
    ret = ""
    if len(iniString)<=0:
      return ret
    count = 1
    ret += iniString[0]
    for i in range(1,len(iniString)):
      if iniString[i]==iniString[i-1]:
        count+=1
      else:
        ret+=str(count)
        ret+=iniString[i]
        count=1
    ret+=str(count)
    if len(ret)>=len(iniString):
      return iniString
    else:
      return ret

# test case
iniString = "aabcccccaaa"
print(Zipper().zipString(iniString) == "a2b1c5a3")