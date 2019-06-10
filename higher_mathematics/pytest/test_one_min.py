#一维函数最小值
def f(x):
    return x ** 2 + 4 * x + 1
def df(x):
    return 2 * x + 4

x_old = 3.14
for itr in range(20):
    x_new = x_old - 0.1 * df(x_old)
    x_old = x_new
    print("f({})={}".format(x_new,f(x_old)))