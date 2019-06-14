#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 6/14/2019 11:24 AM
# @Author: Gao Chengdong
# @Project: dataAnalysis
# @File  : ArrayOperation.py

import numpy as np

"""
修改数组形状
函数	描述
reshape	不改变数据的条件下修改形状
flat	数组元素迭代器
flatten	返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
ravel	返回展开数组
"""

"""
numpy.reshape
numpy.reshape 函数可以在不改变数据的条件下修改形状，格式如下： numpy.reshape(arr, newshape, order='C')
arr：要修改形状的数组
newshape：整数或者整数数组，新的形状应当兼容原有形状
order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'k' -- 元素在内存中的出现顺序。
"""
a = np.arange(8)
print("原始数据：")
print(a)
print("\n")

b = a.reshape(4, 2)
print("b:")
print(b)
print("\n")

"""
numpy.ndarray.flat
numpy.ndarray.flat 是一个数组元素迭代器，实例如下:
"""
a = np.arange(8)
for i in a.flat:
    print(i)

"""
numpy.ndarray.flatten
numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下：
ndarray.flatten(order='C')
参数说明：
order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
"""
a = np.arange(8).reshape(2, 4)
print("原始数组：")
print(a)
print("\n")
print("flatten: ")
print(a.flatten())
print("按列排序：")
print(a.flatten(order='F'))

"""
numpy.ravel
numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图（view，有点类似 C/C++引用reference的意味），修改会影响原始数组。

该函数接收两个参数：

numpy.ravel(a, order='C')
参数说明：

order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
"""
a = np.arange(8).reshape(2, 4)

print('原数组：')
print(a)
print('\n')

print('调用 ravel 函数之后：')
print(a.ravel())
print('\n')

print('以 F 风格顺序调用 ravel 函数之后：')
print(a.ravel(order='F'))

"""
翻转数组
-------------------------------------------------------------------------------
函数	        描述
transpose	对换数组的维度
ndarray.T	和 self.transpose() 相同
rollaxis	向后滚动指定的轴
swapaxes	对换数组的两个轴
numpy.transpose
numpy.transpose 函数用于对换数组的维度，格式如下：

numpy.transpose(arr, axes)
参数说明:

arr：要操作的数组
axes：整数列表，对应维度，通常所有维度都会对换。
"""

"""
numpy.transpose
numpy.transpose 函数用于对换数组的维度，格式如下：

numpy.transpose(arr, axes)
参数说明:

arr：要操作的数组
axes：整数列表，对应维度，通常所有维度都会对换。
"""
a = np.arange(12).reshape(3, 4)

print('原数组：')
print(a)
print('\n')

print('对换数组：')
print(np.transpose(a))

# numpy.ndarray.T 类似 numpy.transpose：
a = np.arange(12).reshape(3, 4)

print('原数组：')
print(a)
print('\n')

print('转置数组：')
print(a.T)

"""
numpy.rollaxis
numpy.rollaxis 函数向后滚动特定的轴到一个特定位置，格式如下：

numpy.rollaxis(arr, axis, start)
参数说明：

arr：数组
axis：要向后滚动的轴，其它轴的相对位置不会改变
start：默认为零，表示完整的滚动。会滚动到特定位置。
"""




