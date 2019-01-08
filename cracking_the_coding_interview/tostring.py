# -*- coding:utf-8 -*-
'''
有一个非负整数，请编写一个算法，打印该整数的英文描述。

给定一个int x，请返回一个string，为该整数的英文描述。
'''

DIG   = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ']
TEEN  = ['Ten ', 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']
TY    = ['', '', 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']
KILO  = ['', 'Thousand,', 'Million,', 'Billion,', 'Trillion,', 'Quadrillion,', 'Sextillion,', 'Septillion,', 'Octillion,', 'Nonillion,']
HUND  = 'Hundred '
class ToString:
  def toString(self, x):
    if x == 0:
      return 'Zero'
    ret = ''
    i = 0
    while x:
      # thousands
      if x % 1000 == 0:
        x //= 1000
      else:
        ret = KILO[i] + ret
        # 0 / 1-9 / 10-19 / 20-99
        if x % 100 == 0:
          pass
        elif (x % 100 < 10) and (x % 100 > 0):
          ret = DIG[x % 100] + ret
        elif (x % 100 >= 10) and (x % 100 < 20):
          ret = TEEN[x % 100 - 10] + ret
        else:
          ret = TY[x % 100 // 10] + DIG[x % 10] + ret
        x //= 100
        # hundred
        if x % 10:
          ret = DIG[x % 10] + HUND + ret
        x //= 10
      i += 1

    return ret[:-1]


#testcase
x = 1335513200
print(ToString().toString(x))
x = 1010000000
print(ToString().toString(x))
x = 40
print(ToString().toString(x))