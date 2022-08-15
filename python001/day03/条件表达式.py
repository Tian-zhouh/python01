"""
真值表达式和条件表达式(三目运算符)
变量 = 结果1 if 条件表达式 else: 结果02
"""

# sex = None
# if input("请输入性别:") == "男":
#     sex = 0
# else:
#     sex = 1

sex = 0 if input("请输入性别:") == "男" else 1
print(sex)

# 练习1：在控制台中输入一个整数，判断是奇数还是偶数，使用真值表达式
num = "奇数" if int(input("请输入一个整数")) % 2 != 0 else "奇数"
print(num)

# 练习2：在控制台中获取一个年份，如果是闰年给变量day赋值29，否则给变量day赋值28
year = int(input("请输入一个年份"))
day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
print(day)
