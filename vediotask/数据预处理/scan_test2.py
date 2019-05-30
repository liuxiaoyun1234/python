from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-1,1,50)  #初始化随机数据
print(x)
y = 2 * x+ 1
plt.plot(x,y)
plt.show()

