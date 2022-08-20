"""
列表:由一系列变量组成的可变序列容器
注意:列表是变量，不是常量


基础操作:
创建列表: []
添加元素: insert
获取元素:
删除元素:
"""

# 1.创建空列表的两种方式
list01 = []
list02 = list()

# 2.创建具有默认值的列表
list01 = [1, True, 1.2]
list02 = list("abcd")  # 存放的是可迭代对象
list03 = list(range(5))
print(list02)

# 3.添加元素

# append 在末尾追加元素
list02.append("q")
list02.append("t")
print(list02)

# insert(索引,元素) 在索引位置处插入元素
list02.insert(1, "x")
print(list02)

# 4.删除元素
# remove(元素) 移除指定的元素
list02.remove("b")
print(list02)

# 删除指定位置的元素
del list02[2]
print(list02)

# 5.修改元素

# 6.定位元素(索引   切片)（可以进行增删改查）
# 获取前三个元素
print(list02[:3])
list02[:3] = [1, 2, 3, 4, 5, 6]
print(list02)

# 7.遍历元素
for item in list02:
    print(item)
for item in list02[::-1]:
    print(item)
for item in range(len(list02)):
    print(list02[item])
for item in range(0, len(list02), 2):
    print(item)
for item in range(len(list02) - 1, -1, -1):
    print(item)
