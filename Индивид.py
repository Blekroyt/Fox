#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
import sys

def fun1(type_='max'):
    def fun2(lst):
        return eval(f'{type_}(lst)')
    return fun2
a = [1, 2, 3, 4, 5, 65, 6,]
max_fun = fun1()
min_fun = fun1('min')
print(max_fun(a))
print(min_fun(a))