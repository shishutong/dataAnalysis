#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 6/12/2019 9:58 AM
# @Author: Gao Chengdong
# @Project: dataAnalysis
# @File  : CreateArrageRange.py

import  numpy as np

"""
numpy.arange
numpy 包中的使用 arange 函数创建数值范围并返回 ndarray 对象，函数格式如下：

numpy.arange(start, stop, step, dtype)
根据 start 与 stop 指定的范围以及 step 设定的步长，生成一个 ndarray。

参数说明：

参数	描述
start	起始值，默认为0
stop	终止值（不包含）
step	步长，默认为1
dtype	返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。
"""
# 生成 0 到 5 的数组:
x = np.arange(5)
print(x)

# 设置返回类型位 float:
x = np.arange(5, dtype=float)
print(x)

# 设置了起始值、终止值及步长：
x = np.arange(10, 20, 2)
print(x)

"""
numpy.linspace
numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：

np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
参数说明：

参数	        描述
start	    序列的起始值
stop	    序列的终止值，如果endpoint为true，该值包含于数列中
num	        要生成的等步长的样本数量，默认为50
endpoint	该值为 ture 时，数列中中包含stop值，反之不包含，默认是True。
retstep	    如果为 True 时，生成的数组中会显示间距，反之不显示。
dtype	    ndarray 的数据类型
"""
a = np.linspace(1, 10, 10)
print(a)

a = np.linspace(10, 10, 5, endpoint=False)
print(a)

a = np.linspace(1, 10, 10, retstep=True)
print(a)
b = np.linspace(1, 10, 10).reshape([10, 1])
print(b)

"""
numpy.logspace
numpy.logspace 函数用于创建一个于等比数列。格式如下：

np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
base 参数意思是取对数的时候 log 的下标。

参数	描述
start	序列的起始值为：base ** start
stop	序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中
num	要生成的等步长的样本数量，默认为50
endpoint	该值为 ture 时，数列中中包含stop值，反之不包含，默认是True。
base	对数 log 的底数。
dtype	ndarray 的数据类型
"""
a = np.logspace(1.0, 2.0, num=10)
print(a)

b = np.logspace(0, 9, 10, base=2)
print(b)
