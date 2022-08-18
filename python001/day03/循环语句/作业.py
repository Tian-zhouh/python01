"""
1. 三合一
2. 将当天练习独立完成
3. 代码练习
一个球从100米的高度落下，每次弹回原高度的一半
问总共弹起多少次？（假定最小弹起高度是0.01米）
总共弹了多少米
4. 在控制台中录入一个整数，判断是否为素数（只能被1和自身整除的数字）
6. 看书，第三章
"""
# 作业3
height = 100
length = 0
count = 0
# 存放可以弹起的条件
while height * 0.5 >= 0.01:
    length += height
    height *= 0.5
    count += 1
    length += height

print("总共弹起" + str(count) + "次")
print("总共走了" + str(round(length, 2)) + "米")

# 作业4
import math

num = int(input("请输入一个整数>>>"))
if num < 2:
    print("不是素数")
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print("不是素数")
            break
    else:
        print("是素数")
