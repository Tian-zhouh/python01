"""
列表推导式
"""
list01 = [3, 4, 5, 6, 7, 9]
# 需求:创建新列表，每个元素是list01中的元素的平方
list02 = []
for item in list01:
    list02.append(item ** 2)
print(list02)

# 列表推导式的语法:
# [对变量的操作 for 变量名 in 可迭代对象]
list03 = [item ** 2 for item in list02]
print(list03)

# 需求:创建新列表，如果元素是偶数，则将每个元素的平方放入新列表
list04 = [item ** 2 for item in list01 if item % 2 == 0]
print(list04)

# 练习，使用range生成1-10之间的数字，存入list01中
# 使用列表推导式，将list01中所有奇数存入list02
#               将list01中所有偶数存入list03
#               将list01中元素大于3的存入list04
list01 = [item for item in range(1, 11)]
list02 = [item for item in list01 if item % 2 == 1]
list03 = [item for item in list01 if item % 2 == 0]
list04 = [item for item in list01 if item > 3]
print(list01)
print(list02)
print(list03)
print(list04)
