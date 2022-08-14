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
