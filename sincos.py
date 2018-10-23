#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:23:02 2018

@author: YvaineYUU
"""
#Simply Drawing a plot
##import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
x=np.linspace(0,2 * np.pi, 50)
plt.plot(x, np.sin(x))
plt.show()

#Two lines in one plot
x=np.linspace(0,2 * np.pi, 50)
plt.plot(x,np.sin(x),
        x,np.sin(2 * x))
plt.show()

#How to change the appearance
x=np.linspace(0,2 * np.pi,50)
plt.plot(x,np.sin(x),'r-o',
         x, np.cos(x), 'g--')
plt.show()