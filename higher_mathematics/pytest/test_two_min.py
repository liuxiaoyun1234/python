
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