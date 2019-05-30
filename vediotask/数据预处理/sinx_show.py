from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
import math
import pylab

#x = np.linspace(0,180,50)  #初始化随机数据
x = pylab.arange( 0, 10, 0.1)
print(x)
#y = math.sin(x)
y = np.sin(x)
print(y)
plt.plot(x,y)
plt.show()
