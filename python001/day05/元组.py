"""
元组:
    由一系列变量组成的不可变序列容器
    列表和元组不同，列表由增删改的操作，元组没有增删改的操作

    列表与元组的区别:
    元组与列表都可以存储一系列变量，由于列表会预留内存空间
    元组会按需分配内存，所以如果变量数量固定，建议使用元组，因为占用空间更小

    应用:
    变量交换的本质就是创建元组 x,y=y,x
    格式化字符串的本质就是创建元组  "姓名:%d,性别:%d",(x,y)

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

# 练习:
# 根据月份计算天数
mounths = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
mounth30 = (4, 6, 9, 11)
mounth31 = (1, 3, 5, 7, 8, 10, 12)
mounth28 = (2,)
mounth = int(input("请输入月份>>>"))
if mounth in mounth30:
    print("30天")
elif mounth in mounth31:
    print("31天")
elif mounth in mounth28:
    print("28天")
else:
    print("输入月份有误")

# 脑洞大开
day_of_mouth = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
if mounth not in mounths:
    print("输入有误")
else:
    print(day_of_mouth[mounth - 1])

# 练习2:在控制台中输入月，日
# 计算这是一年的第几天

mounth = int(input("请输入月份>>>"))
date = int(input("请输入日期>>>"))
if mounth not in mounths:
    print("输入月份有误")
else:
    if date < 0 or day_of_mouth[mounth - 1] < date:
        print("输入日期有误")
    else:
        day = 0
        # for item in day_of_mouth[0:mounth - 1]:
        #     day += item

        # 更优方法
        day = sum(day_of_mouth[:mounth - 1])
        day += date
        print(day)
