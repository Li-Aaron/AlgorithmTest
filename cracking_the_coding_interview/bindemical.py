'''
有一个介于0和1之间的实数，类型为double，返回它的二进制表示。如果该数字无法精确地用32位以内的二进制表示，返回“Error”。

给定一个double num，表示0到1的实数，请返回一个string，代表该数的二进制表示或者“Error”。
'''

class BinDecimal:
  def printBin(self, num):
    string = '0.'
    cnt = 0
    while cnt < 32:
      num *= 2
      if num >= 1:
        num -= 1
        string += '1'
      else:
        string += '0'
      if num == 0:
        return string
      cnt += 1
    return 'Error'

# test case
num = 0.625
res = '0.101'
print(BinDecimal().printBin(num) == res)