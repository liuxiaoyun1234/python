
from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000),index = np.arange(1000))
print(data)
data = data.cumsum()
print(data)


data = pd.DataFrame(np.random.randn(1000,4),index = np.arange(1000),columns=['A','B','C','D'])
print(data)
data = data.cumsum()
print(data)

ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class 1')
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
plt.show()
