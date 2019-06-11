#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 6/11/2019 2:02 PM
# @Author: Gao Chengdong
# @File  : cerateArray.py

import numpy as np

"""
numpy.empty
    方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
    numpy.empty(shape, dtype = float, order = 'C')

参数	    描述
shape	数组形状
dtype	数据类型，可选
order	有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
"""
x = np.empty([3, 2], dtype=int)
print("empty: ", x)
# empty:  [[2053731104 1852383333]
#  [1954112032 1864397669]
#  [1752440934 1970413669]]

"""
numpy.zeros
创建指定大小的数组，数组元素以 0 来填充：
    numpy.zeros(shape, dtype = float, order = 'C')
参数说明：
参数	描述
shape	数组形状
dtype	数据类型，可选
order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组
"""
x = np.zeros(5)
print(x)
# [0. 0. 0. 0. 0.]

y = np.zeros((5,), dtype=np.int)
print(y)
# [0 0 0 0 0]

z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)
# [[(0, 0) (0, 0)]
#  [(0, 0) (0, 0)]]

"""
numpy.ones
创建指定形状的数组，数组元素以 1 来填充：
    numpy.ones(shape, dtype = None, order = 'C')
参数说明：
参数	描述
shape	数组形状
dtype	数据类型，可选
order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组
"""
x = np.ones(5)
print(x)
# [1. 1. 1. 1. 1.]

y = np.ones((4, 4))
print(y)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

z = np.ones((4, 4), dtype=[("x", 'i2'), ("y", 'i2')])
print(z)
# [[(1, 1) (1, 1) (1, 1) (1, 1)]
#  [(1, 1) (1, 1) (1, 1) (1, 1)]
#  [(1, 1) (1, 1) (1, 1) (1, 1)]
#  [(1, 1) (1, 1) (1, 1) (1, 1)]]
