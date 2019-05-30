import random

choose = random.randint(1,10);

temp = input("不妨猜一下小甲鱼心在心里想的是什么数字")
guess = int(temp)
while guess != choose:
    temp = input("猜错了，请重新输入")
    guess = int(temp)
    if guess == choose:
        print("你是小甲鱼的蛔虫吗")
        print("猜对了")
    else:
        if guess > choose:
            print("大了")
        else:
            print("小了")
