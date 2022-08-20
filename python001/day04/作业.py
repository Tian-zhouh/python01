"""
1. 三合一
2. 当天练习独立完成
3. 练习：
    001：在控制台中循环录入字符串，输入q退出，然后显示一个新的字符串
4.回文:
    上海自来水来自海上  是回文
    奶牛产牛奶    是回文
    判断字符串是否是回文
    提示：字符串翻转
5. 双色球:一注彩票7个球
    前六个是红球:1-33 之间的数字，且不能重复
    最后一个是蓝球:1-16 之间的数字
    (1)在控制台中购买彩票:
    (2)随机产生一注彩票
"""
# 3:001
list_inp = []
while True:
    inp = input("请输入字符串>>>")
    if inp == "q":
        break
    list_inp.append(inp)

list_inp = "".join(list_inp)
print(list_inp)
# 4.
inp = input("请输入字符串>>>")
inp_len = len(inp)
coun = inp_len // 2
if inp[:coun] == inp[-1:-coun - 1:-1]:
    print("是回文")
else:
    print("不是回文")
# 5.
list_douball = []
item = 0
while item < 7:
    item += 1
    if item < 7:
        ball_inp = int(input(f"请输入第{item}个1-33之间的双色球号码>>>"))
        if ball_inp > 33 or ball_inp < 0:
            print("请输入合法的数字")
            item -= 1
            continue
        elif ball_inp in list_douball:
            print("你已经输入过了")
            item -= 1
            continue
        list_douball.append(ball_inp)
    elif item == 7:
        ball_inp = int(input(f"请输入第{item}个1-16之间的双色球号码>>>"))
        if ball_inp > 16 or ball_inp < 0:
            print("请输入合法的数字")
            item -= 1
            continue
        list_douball.append(ball_inp)
import random

double_num = []
i = 0
while i < 7:
    if i < 6:
        rand_in = random.randint(1, 33)
        if rand_in not in double_num:
            double_num.append(rand_in)
            i += 1
    elif i == 6:
        double_num.append(random.randint(1, 16))
        i += 1
print(list_douball)
print(double_num)
