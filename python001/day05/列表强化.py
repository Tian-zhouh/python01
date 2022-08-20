"""
这里需要格外注意
"""

list01 = [1, 2]
# 将列表地址赋值给list02
list02 = list01[:]
# 等价于
list02 = list01.copy()
# 改变的是列表第一个元素所存储的地址
list01[0] = 100
print(list02[0])  # 输出100

# 这里涉及深拷贝+浅拷贝
# 上方为浅拷贝
# 下方为深拷贝

import copy

list02 = copy.deepcopy(list01)  # 深拷贝
