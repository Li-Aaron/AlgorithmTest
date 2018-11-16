#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
24点游戏
@Author: AC
2018-4-26
'''

import random
import copy

NUM = 4
TARGET_NUM = 24

def fork(A_list, B_list):
    '''
    生成四则运算后的数组
    :param A_list:
    :param B_list: list, include dicts [{},{}] {'value','str'}
    :return: list, include dicts [{},{}]
    '''
    ret = []
    for a_dict in A_list:
        a = a_dict['value']
        a_str = a_dict['str']
        for b_dict in B_list:
            b = b_dict['value']
            b_str = b_dict['str']
            ret.append({'value':a+b,'str':'(%s + %s)'%(a_str,b_str)})
            ret.append({'value':a-b,'str':'(%s - %s)'%(a_str,b_str)})
            ret.append({'value':a*b,'str':'(%s * %s)'%(a_str,b_str)})
            if b != 0:
                ret.append({'value':a/b,'str':'(%s / %s)'%(a_str,b_str)})
    return ret

def run_points(A_list_all, target_num = 24):
    '''
    recursion, 求解到target_num的计算式
    :param A_list_all: list, include A_list [[{},{}],[{},{}]]
    :param target_num:
    :return: 计算式/None
    '''

    # recursion exit
    if len(A_list_all) == 1:
        for a in A_list_all[0]:
            if abs(a['value'] - target_num) < 1e-6:
                result_str = '%s = %s'%(a['str'],target_num)
                return result_str

    for A_list in A_list_all:
        # get A and remove
        B_list_All = copy.deepcopy(A_list_all)
        B_list_All.remove(A_list)
        for B_list in B_list_All:
            # get B and remove
            New_list_all = copy.deepcopy(B_list_All)
            New_list_all.remove(B_list)
            forked_list = fork(A_list, B_list)
            # append forked list
            New_list_all.append(forked_list)
            # recursion
            result_str = run_points(New_list_all, target_num)
            if result_str:
                return result_str


if __name__ == '__main__':
    A = [random.randint(0,TARGET_NUM/2) for x in range(NUM)]
    A_list_all = [[{'value': float(x), 'str': str(x)}] for x in A]
    print(A)
    print(run_points(A_list_all, TARGET_NUM))
