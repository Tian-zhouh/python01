"""
元组:
    由一系列变量组成的不可变序列容器
    列表和元组不同，列表由增删改的操作，元组没有增删改的操作

    列表的扩容原理：
        1.创建新列表(更大的列表)
        2.拷贝原有元素
        3.替换列表地址
    # python采用分布式原理存储列表

    元组没有扩容原理，但是性能会更高；当未来数量是固定的，优先考虑元组

"""
list01 = [1, 2, 3]
# 扩容
print(id(list01))

# 创建空元组
tuple01 = ()
tuple02 = tuple()

# 创建具有默认值的元组
tuple01 = (1, 2, [1, 2, 3])
tuple02 = tuple(range(1, 6))
print(tuple01)
print(tuple02)

# 元组内部可以嵌套列表；列表内部可以嵌套元组；互不影响

# 3.修改（报错）
# tuple01[0] = 100
# 元组内部的列表可以修改
tuple01[2][0] = 100
print(tuple01)

# 4.获取元素  (索引  /   切片)
print(tuple01[:2])

# 获取元组所有元素
for item in tuple01:
    print(item)

# 倒序获取元组所有元素
for item in tuple01[::-1]:
    print(item)

# 根据索引倒序获取
for item in range(len(tuple01) - 1, -1, -1):
    print(tuple01[item])

tuple02 = ("a", "b")
list02 = ["a", "b"]

tuple03 = tuple02
list03 = list02

tuple02 += ("c", "d")  # 创建了新的元组对象，改变了tuple02存储的位置
list02 += ["c", "d"]  # 没有创建新的列表对象，而是在原始列表进行追加操作

print(tuple03)  # (a,b)
print(tuple02)  # (a,b,c,d)
print(list03)  # (a,b,c,d)

# 如果元组只有一个元素，必须多写一个逗号，否则视为普通对象，不是容器(元组)对象
tuple00 = (1)  # 普通容器对象
tuple00 = (1,)  # 元组对象
