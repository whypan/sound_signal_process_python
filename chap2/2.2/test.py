# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:36:36 2019

@author: lenovo
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20, endpoint=False)
y = np.cos(-x**2/6.0)
f = signal.resample(y, 100)
xnew = np.linspace(0, 10, 100, endpoint=False)

plt.figure()
plt.subplot(3,1,1)
plt.plot(x, y,'go-')
plt.xlabel("time/s")
plt.ylabel("归一化幅值")
plt.title("原始信号")

plt.subplot(3,1,2)
plt.plot(xnew, f,'go-')
plt.xlabel("time/s")
plt.ylabel("归一化幅值")
plt.title("原始信号")

plt.subplot(3,1,3)
plt.plot(10, y[0],'go-')
plt.xlabel("time/s")
plt.ylabel("归一化幅值")
plt.title("原始信号")

plt.show()