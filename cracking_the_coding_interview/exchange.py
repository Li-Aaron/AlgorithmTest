'''
请编写程序交换一个数的二进制的奇数位和偶数位。（使用越少的指令越好）

给定一个int x，请返回交换后的数int。
'''
class Exchange:
  def exchangeOddEven(self, x):
    return ((x & 0xAAAAAAAA) >> 1) | ((x & 0x55555555) << 1)

# test case
x = 10
print(Exchange().exchangeOddEven(10) == 5)