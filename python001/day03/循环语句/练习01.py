"""
猜数字1.0
规则:系统产生1--100之间的随机数
    让用户重复猜测，直到猜对了为止
    提示:大了  小了  猜对了
猜数字2.0
最多只能猜10次.
"""
import random

num = int(input("请输入一个1-100的整数>>>"))
random_number = random.randint(1, 100)
count = 0
while count < 10:
    count += 1
    if num > random_number:
        print("猜大了")
    elif num < random_number:
        print("猜小了")
    else:
        print("猜对了")
        break
    num = int(input("请输入一个1-100的整数>>>"))

count = 0
while count < 10:
    count += 1
    input_number = int(input("第" + str(count + 1) + "次输入:"))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("猜对了")
        break
else:
    # 只有从whil条件结束，才执行else语句
    # 从循环体内部break，不会执行
    print("没机会了你")

# 02:13:39
