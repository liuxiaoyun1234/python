#二维函数极小值练习可视化

def f(x,y):
    return x**2 + 3*x + y**2 + 8*y + 1
def df(x,y):
    return 2*x+3,2*y+8

#二维函数可视化
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
#Matlab中的一个指令,用于产生指定范围内的指定数量点数,相邻数据跨度相同,并返回一个行向量
x=np.linspace(-6,3)
y=np.linspace(-6,3)

#生成网格点坐标矩阵
X,Y = np.meshgrid(x,y)

#创建一个用来显示图形输出的一个窗口对象
fig = plt.figure()

ax = fig.gca(projection="3d")

surf = ax.plot_surface(X,Y,f(X,Y))
plt.show()