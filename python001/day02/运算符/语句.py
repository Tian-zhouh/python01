"""
行: 物理行，逻辑行

选择语句
"""

sex = input("请输入性别>>>")
if sex == "man":
    print("你好先生")
elif sex == "woman":
    print("你好女士")
else:
    print("保密")

# 练习01:
# 在控制台中输入一个整数，如果是基数则显示奇数，否则显示偶数

num = int(input("请输入一个整数>>>"))
if num % 2 == 0:
    print("这是一个偶数")
else:
    print("这是一个奇数")

# 练习02:
# 在控制台中输入一个年份
# 如果是闰年 显示闰年，否则显示平年

year = int(input("请输入年份>>>"))
if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print("这是闰年")
else:
    print("这是平年")
