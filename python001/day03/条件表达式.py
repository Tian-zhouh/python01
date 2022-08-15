"""
真值表达式和条件表达式(三目运算符)
变量 = 结果1 if 条件表达式 else: 结果02
"""

sex = None
if input("请输入性别:") == "男":
    sex = 0
else:
    sex = 1

sex = 0 if input("请输入性别:") == "男" else 1
print(sex)
