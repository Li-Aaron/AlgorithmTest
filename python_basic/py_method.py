#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        t=time.localtime()
        # 生成的是Date类
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @classmethod
    def cnow(cls):
        t = time.localtime()
        # 生成的是自身类
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    @staticmethod
    def date_now():
        t=time.localtime()
        print('year:%s, month:%s, day:%s'%(t.tm_year, t.tm_mon, t.tm_mday))

    @property
    def date(self):
        # 访问时返回值
        return (self.year, self.month, self.day)

class EuroDate(Date):
    def __str__(self):
        return 'year:%s, month:%s, day:%s'%(self.year, self.month, self.day)

if __name__ == '__main__':
    t = time.localtime()
    a = EuroDate(t.tm_year, t.tm_mon, t.tm_mday)

    print(1)
    print(a, type(a))
    print(a.year,a.month,a.day)
    a.date_now()
    print(a.date)

    a.date_now()
    b = EuroDate.now()
    print(2)
    print(b, type(b))
    print(b.year,b.month,b.day)
    b.date_now()
    print(b.date)

    c = EuroDate.cnow()
    print(3)
    print(c, type(c))
    print(c.year,c.month,c.day)
    c.date_now()
    print(c.date)