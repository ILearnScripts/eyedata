#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
import matplotlib.mlab as mlab
from scipy.stats import norm


path='./EyeCloser'
cate=[path+'/'+x for x in os.listdir(path)]
interval00 = []
interval01 = []

for idx,folder in enumerate(cate): # loop for one txt
    im = folder
    with open(im,'r') as f:
        data = f.readlines()  # all the data in one txt
    f.close()
    # initialize the temp restore list
    time_interval = []
    interval00_current = []
    interval01_current = []
    # main loop
    data = data[1:] # 去掉第一个0
    
    if len(data)>1:        
        for index,line in enumerate(data): 
            # deal with the first line
            if index ==0:
                line = line.strip()
                one_line = line.split(',') # split to two values
                previous_time = float(one_line[1])
                continue    
            line = line.strip()
            one_line = line.split(',') # split to two values
            current_time = float(one_line[1])
            current_interval = current_time - previous_time
            time_interval.append(current_interval)
            previous_time = current_time
            
    interval01_current = time_interval[0:len(time_interval):2]
    len_01 = int(np.floor(len(time_interval)/2))
    for i in range(len_01):
        one_inverval_01 = time_interval[2*i] 
        if one_inverval_01 >100:
            temp = 1
        interval01_current.append(one_inverval_01)
    len_00 = int(np.floor(len(time_interval)/2))
    for i in range(len_00):
        one_inverval_00 = time_interval[2*i+1] +time_interval[2*i]
        if one_inverval_00 >100:
            temp = 1            
        interval00_current.append(one_inverval_00)
    interval00 = interval00 +  interval00_current  
    interval01 = interval01 +  interval01_current 

data_range01 = [np.min(interval01),np.max(interval01)]
data_range00 = [np.min(interval00),np.max(interval00)]
print(data_range01)
print(data_range00)

# draw 0-1
newnums = []
for i in interval01:
    if i<=1:
        newnums.append(i)
interval01 = newnums
mu =np.mean(interval01) 
sigma =np.std(interval01)
bin_interval01 = 0.01
data_range = [np.min(interval01),np.max(interval01)]
num_bins = 100 #直方图柱子的数量 
n, bins, patches = plt.hist(interval01, num_bins,density=1, alpha=0.75)
y = norm.pdf(bins, mu, sigma)
plt.grid(True)
plt.plot(bins, y, 'r--') #绘制y的曲线 
plt.xlabel('values') #绘制x轴 
plt.ylabel('Probability') #绘制y轴 
plt.title('Histogram : $\mu$=' + str(round(mu,2)) + ' $\sigma=$'+str(round(sigma,2)))  #中文标题 u'xxx' 
plt.show()

# draw 0-0
newnums = []
for i in interval00:
    if i<=10:
        newnums.append(i)
interval00 = newnums
mu =np.mean(interval00) 
sigma =np.std(interval00)
bin_interval01 = 0.01
data_range = [np.min(interval00),np.max(interval00)]
num_bins = 100 #直方图柱子的数量 
n, bins, patches = plt.hist(interval00, num_bins,density=1, alpha=0.75)
y = norm.pdf(bins, mu, sigma)
plt.grid(True)
plt.plot(bins, y, 'r--') #绘制y的曲线 
plt.xlabel('values') #绘制x轴 
plt.ylabel('Probability') #绘制y轴 
plt.title('Histogram : $\mu$=' + str(round(mu,2)) + ' $\sigma=$'+str(round(sigma,2)))  #中文标题 u'xxx' 
plt.show()

