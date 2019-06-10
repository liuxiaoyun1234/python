#二维函数可视化


#二维函数最小值
def f_2d(x,y):
    return x ** 2 + 4 * x + y ** 2 + 4 * y + 1
def df_2d(x,y):
    return 2 * x + 4, 2 * y + 4

x,y=4,4

for itr in range(200):
    v_x,v_y = df_2d(x,y)
    x,y = x-0.1*v_x,y-0.1*v_y
    #12行的数学表达方式：
    # x_t = x_t - 0.1 * grad
    # grad 梯度 = x或者y的偏导数
    print("f({},{})={}".format(x,y,f_2d(x,y)))


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

surf = ax.plot_surface(X,Y,f_2d(X,Y))
plt.show()