"""
练习1：
    在控制台作中获取一个月份，打印季节
"""

mounth = int(input("请输入一个月份>>>"))

if 1 <= mounth <= 3:
    print("春天")
elif 3 < mounth <= 6:
    print("夏天")
elif 6 < mounth <= 9:
    print("秋天")
elif 9 < mounth <= 12:
    print("冬天")
else:
    print("请输入一个合法的月份")

# 更优算法
if mounth < 1 or mounth > 12:
    print("请输入一个合法的月份")
elif mounth <= 3:
    print("春天")
elif mounth <= 6:
    print("夏天")
elif mounth <= 9:
    print("秋天")
elif mounth <= 12:
    print("冬天")

# 练习02
# 在控制台输入一个季度，显示该季度中的月份
quarter = input("请输入一个季度>>>")
if quarter == "春天":
    print("1 - 3月")
elif quarter == "夏天":
    print("4 - 6月")
elif quarter == "秋天":
    print("7 - 9月")
elif quarter == "冬天":
    print("10 - 12月")
else:
    print("请输入一个合法的季度")

# 练习03：在控制台中输入一个月份，返回该月份你的天数
mounths = int(input("请输入月份"))
if mounths == 1 or mounths == 3 or mounths == 5 or mounths == 7 or mounths == 8 or mounths == 10 or mounths == 12:
    print("有31天")
elif mounths == 4 or mounths == 6 or mounths == 9 or mounths == 11:
    print("有30天")
elif mounths == 2:
    print("有28天")
else:
    print("输入月份有误")

# 更优方法
if mounths < 1 or mounths > 12:
    print("输入月份有误")
elif mounths == 2:
    print("28天")
elif mounths == 4 or mounths == 6 or mounths == 9 or mounths == 11:
    print("30天")
else:
    print("31天")

# 练习04
num01 = 8
num02 = 6
num03 = 10
num04 = 5
# 计算最大的数值
if num01 < num02:
    num = num02
else:
    num = num01
if num03 < num04:
    nums = num04
else:
    nums = num03
if num < nums:
    print(nums)
else:
    print(num)

# 其他方法
if num01 < num02:
    num01 = num02
if num01 < num03:
    num01 = num03
if num01 < num04:
    num01 = num04
print(num01)
