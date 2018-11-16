#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
背包问题
@Author: AC
2018-4-10
'''
__author__ = 'AC'


import numpy as np

class Knapsack(object):
    def __init__(self, N, V, w = None, p = None, c = None):
        '''
        :param N: 商品数
        :param V: 背包容量
        :param w: weight np.array
        :param p: price np.array
        :param c: 最大个数 np.array
        '''
        if isinstance(w, type(None)):
            w = np.random.randint(1,max(V//2,2),N)
            print('w=%s'%w)
        if isinstance(p, type(None)):
            p = np.random.randint(5,10,N)
            print('p=%s'%p)
        if isinstance(c, type(None)):
            c = np.random.randint(1,max(V//2,3),N)
            print('c=%s'%c)
        self.N, self.V, self.w, self.p, self.c = N, V, w, p, c
        self.x_tmp = np.zeros([N, V + 1], dtype=int) # 求x过程临时矩阵
        self.count_init()

    def count_init(self):
        self.n_recurrence_enter = 0
        self.n_recurrence = 0
        self.n_recursion_enter = 0
        self.n_recursion = 0


    def cal_x_result(self):
        '''计算x（每个商品所购买数量）'''
        N, V, w = self.N, self.V, self.w
        x_result = np.zeros([N], dtype=int)
        x_tmp = self.x_tmp
        # calculate each x in end
        v = V
        for i in np.arange(N - 1, -1, -1):
            x_result[i] = x_tmp[i][v]
            v = v - x_tmp[i][v] * w[i]
        return x_result

    def cal_knapsack(self):
        '''
        计算背包问题的解（递推）
        迭代公式：
        f[i][0] = 0
        f[i][v] = max{x[i]p[i] + f[i-1][v-x[i]w[i]]} x[i] in {0,c[i]}
        :return: max price
        '''
        N, V, w, p, c = self.N, self.V, self.w, self.p, self.c
        self.f = np.zeros([N,V+1],dtype=float) # 迭代表(直接赋初值0)
        f, x_tmp = self.f, self.x_tmp
        # calculate lut
        for i in np.arange(0, N):
            for v in np.arange(1, V+1):
                f[i][v] = -np.inf # 容量不为0时 初值为-inf
                for x in np.arange(0, c[i]+1):
                    self.n_recurrence_enter += 1
                    if v - x*w[i] < 0:
                        break # over weight
                    self.n_recurrence += 1
                    # f[i][v] = max(x*p[i] + f[i-1][v-x*w[i]], f[i][v])
                    # 注意此时i = 0可以索引到 i-1 = -1相当于(N-1)，但是由于初值设置为0，所以可以视作没有商品。
                    if x*p[i] + f[i-1][v-x*w[i]] > f[i][v]:
                        f[i][v] = x*p[i] + f[i-1][v-x*w[i]]
                        x_tmp[i][v] = x

        return f[N-1][V]

    def _cal_knapsack_recursion(self, i, v):
        '''
        计算背包问题的解（递归）
        :param i: 商品序号 {0, N-1}
        :param v: 当前背包容量 {0, V}
        :return: f[i][v]
        '''
        N, V, w, p, c = self.N, self.V, self.w, self.p, self.c
        f, x_tmp = self.f, self.x_tmp
        self.n_recursion_enter += 1

        if v < 0 or v > V: # 边界条件
            return -np.inf
        elif v == 0 or i == -1: # 初始条件
            return 0
        elif f[i][v] != -1: # 避免重复计算
            return f[i][v]

        self.n_recursion += 1
        f[i][v] = -np.inf # 容量不为0时 初值为-inf
        for x in np.arange(0, c[i]+1):
            tmp = self._cal_knapsack_recursion(i-1, v-x*w[i]) + x*p[i]
            if tmp > f[i][v]:
                f[i][v] = tmp
                x_tmp[i][v] = x
        return f[i][v]

    def cal_knapsack_recursion(self):
        N, V = self.N, self.V
        self.f = -np.ones([N, V+1], dtype=float) # 迭代表(-1代表没有计算)
        return self._cal_knapsack_recursion(N-1, V)

    def knap_test(self):
        self.count_init()
        # 递推
        print('recurrence:')
        val = self.cal_knapsack()
        x = self.cal_x_result()
        print('val=%s, x=%s' % (val, x))
        print('lut=\n%s' % self.f)

        # 递归
        print('recursion:')
        val = self.cal_knapsack_recursion()
        x = self.cal_x_result()
        print('val=%s, x=%s' % (val, x))
        print('lut=\n%s'%self.f)

        print('recurrence entered:    %s'%self.n_recurrence_enter)
        print('recurrence calculated: %s'%self.n_recurrence)
        print('recursion entered:     %s'%self.n_recursion_enter)
        print('recursion calculated:  %s'%self.n_recursion)


if __name__ == '__main__':
    N = 6
    V = 10
    print('N = %s, V = %s'%(N,V))
    kp = Knapsack(N, V)
    kp.knap_test()




