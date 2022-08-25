"""
集合


"""
# 1.创建空集合
s01 = set()
# 2.创建具有默认值的集合
s01 = {1, 2, 3, 4}
s02 = set("abcde")
# 3.其他容器变为集合
s03 = set([1, 2, 3, 5, 2, 4])
l03 = list(s03)
# 4.添加
s02.add("a")
s02.add("c")
s02.add("f")
# 5.删除
s02.remove("c")  # 如果该元素不存在，则错误
if 9 in s02:
    s02.remove(9)
s02.discard(9)  # 当元素不存在，不会报错
# 6.获取所有元素
for item in s02:
    print(item)

# 7.计算
s03 = {1, 2, 3}
s04 = {2, 3, 4}
# 交集
s05 = s03 & s04  # 交集
print(s05)
s06 = s03 | s04  # 并集
print(s06)
s07 = s03 ^ s04  # 补集
print(s07)
s08 = s04 - s03  # 差集
print(s08)
# 子集
s09 = {1, 2, 3}
s10 = {1, 2}
print(s10 < s09)  # 子集
print(s10 > s09)  # 超集
# 相同，不同
print(s08 == s09)
print(s09 != s08)

# 集合推导式
# 字典且没有冒号

# 固定集合
f01 = frozenset([1, 2, 3, 2])
print(f01)
