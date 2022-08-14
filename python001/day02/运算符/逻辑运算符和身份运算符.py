"""
逻辑运算符 :与and  或or  非not
            假     真     反
身份运算符
"""

# and 一假俱假
print(True and True)
print(True and False)
print(False and False)
print(False and False)

# or 一真俱真
print(True or False)
print(True or True)
print(False or True)
print(False or False)

print(not False)
print(not True)

print(1 > 2 and 5 > 3)  # False
print(1 < 2 and 5 > 3 and 10 > 5)  # True

# 典型案例：限制元件移动范围

# 短路逻辑
# and
# 如果第一个条件不满足，则不再考虑第二个条件
# or
# 如果第一个条件满足，则不再考虑第二个条件

# 建议将比较耗费时间的逻辑放在条件判断语句靠后的位置，有一定概率可以节省一些时间

# 身份运算符

# is 用于判断两个对象是否为同一对象
# 和id(差不多)
num01 = 800
num02 = 900
num03 = num01
print(num01 is num02)
print(id(num01) == id(num02))

print(num01 is num03)
print(id(num01) is id(num03))

# 练习01：
# 闰年:判断标准：年份能被4整除，但是不能被100整除
#       年份能被400整除
# 在控制台中获取年份
# 判断是否为闰年，如果是显示true，否则显示false

year = int(input("请输入年份>>>"))
print((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0))

# 练习02:
# 在控制台中获取一个四位整数，计算每位相加和
num = int(input("请输入四位整数>>>"))
num01 = num // 1000
num02 = num // 100 % 10
num03 = num // 10 % 10
num04 = num % 10
print(num01 + num02 + num03 + num04)

# 练习03:
# 在控制台中输入一个总秒数，计算几小时几分钟几秒

time = int(input("请输入秒数>>>"))
hour = time // 60 ** 2
second = time % 60
minute = time // 60 % 60
print(str(hour) + " 小时 " + str(minute) + " 分钟 " + str(second) + " 秒")
