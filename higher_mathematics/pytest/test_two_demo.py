#二维函数极小值练习
#f(x,y)=x**2 + 3 *x + y**2+8y+1
def f(x,y):
    return x**2 + 3*x + y**2 + 8*y + 1
def df(x,y):
    return 2*x+3,2*y+8

x,y=4,4

for itr in range(200):
    x_t,y_t = df(x,y)
    x,y = x-0.1*x_t,y-0.1*y_t
    print("f({},{})={}".format(x,y,f(x,y)))