def sayhello(a="dfname"):
    return ("hello:"+a)

print(sayhello())
print(sayhello("liuxiaoyun"))

test = sayhello()
print(test)

def team(a,*b):  #扩展多个
    print(a+":"+str(b))

team("liuxiaoyun","huanglixiang")

team("liuxiaoyun","huanglixiang","liuke","xxx")