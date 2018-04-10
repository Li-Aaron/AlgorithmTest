#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
背包问题
@Author: AC
2018-4-10
'''
__author__ = 'AC'


import numpy as np

def cal_knapsack(N, V, w = None, p = None, c = None):
    '''
    计算背包问题的解
    迭代公式：
    f[i][0] = 0
    f[i][v] = max{x[i]p[i] + f[i-1][v-x[i]w[i]]} x[i] in {0,c[i]}
    :param N: 商品数
    :param V: 背包容量
    :param w: weight np.array
    :param p: price np.array
    :param c: 最大个数 np.array
    :return: max price
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

    f = np.zeros([N,V+1],dtype=float) # 迭代表
    x_tmp = np.zeros([N,V+1],dtype=int)
    x_result = np.zeros([N],dtype=int) # 迭代结果对应的x
    # calculate lut
    for i in np.arange(0, N):
        for v in np.arange(1, V+1):
            f[i][v] = -np.inf # 容量不为0时 初值为-inf
            for x in np.arange(0, c[i]+1):
                if v - x*w[i] < 0:
                    break # over weight
                # f[i][v] = max(x*p[i] + f[i-1][v-x*w[i]], f[i][v])
                if x*p[i] + f[i-1][v-x*w[i]] > f[i][v]:
                    # print('(i:%2s,v:%2s,x:%2s) v-x*w[i]                  = %s' % (i, v, x, v - x * w[i])))
                    # print('(i:%2s,v:%2s,x:%2s) x*p[i] + f[i-1][v-x*w[i]] = %s' % (i, v, x, x * p[i] + f[i - 1][v - x * w[i]]))
                    # print('(i:%2s,v:%2s,x:%2s) f[i][v]                   = %s' % (i, v, x, f[i][v]))
                    # print('')
                    f[i][v] = x*p[i] + f[i-1][v-x*w[i]]
                    x_tmp[i][v] = x

    # calculate each x in end
    v = V
    for i in np.arange(N-1, -1, -1):
        x_result[i] = x_tmp[i][v]
        v = v-x_tmp[i][v]*w[i]

    return f[N-1][V], x_result

if __name__ == '__main__':
    N = 6
    V = 10
    print 'N = %s, V = %s'%(N,V)
    # w = np.array([3, 1, 5, 1, 4])
    # p = np.array([9, 19, 14, 14, 16])
    # c = np.array([2, 2, 1, 1, 1])
    # val, x = cal_knapsack(N,V,w=w,p=p,c=c)
    val, x = cal_knapsack(N,V)
    print val
    print 'x=%s'%x



