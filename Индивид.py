#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
import sys
#Используя замыкания функций, объявите внутреннюю функцию, которая принимает в качестве аргумента коллекцию (список или кортеж) и возвращает или минимальное значение, или максимальное, в зависимости от значения параметра type внешней функции. Если type равен «max», то возвращается максимальное значение, иначе – минимальное. По умолчанию type должно принимать значение «max». Вызовите внутреннюю функцию замыкания и отобразите на экране результат ее работы.

def fun1(type_='max'):
    def fun2(lst):
      return eval(f'{type_}(lst)')
    return fun2
   
if __name__ == '__main__':
 a = [1, 2, 3, 4, 5, 65, 6,]
 max_fun = fun1()
 min_fun = fun1('min')
print(max_fun(a))
print(min_fun(a))
