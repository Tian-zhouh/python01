"""
字典:
    由一系列键值对组成的可变映射容器
    映射: 通过键获取值(字符串/列表/元组通过索引)
    键必须唯一且不可变(字符串/数字/元组),值没有限制

    # 字典是无序的

    # 向字典存入新数据，都需要对key进行哈希运算
    # 向字典取出数据(目的:进行快速定位操作)
    # 同一字典中字典的键不允许相同，值允许相同
"""
dict01 = {"key": "value"}
print(dict01)
print(dict01["key"])

# 创建空字典
dict01 = {}
dict02 = dict()

# 创建非空字典
dict01 = {"a": "b", "c": "d"}
# dict02 = dict("ab")分不清key value
dict02 = dict([(1, 2), (3, 4)])  # 需要使用这种方式进行存放
print(dict02)

# 继续给字典添加新内容
# 第一次增加
dict01["name"] = "catch"
# 第二次修改
dict01["name"] = "cc"
print(dict01)
# 若字典中没有key 则报错
# 建议，在字典中读取元素，先判断存在，再进行读取、
# 字典不支持切片
if "d" in dict01:
    print(dict01["d"])

# 删除
if "name" in dict01:
    del dict01["name"]
print(dict01)

# 获取字典中所有元素
for key in dict01:
    print(key, end=":")
    print(dict01[key])

# 获取字典中所有键值对(元组)
# 重点
for key, value in dict01.items():
    print(key, value)

# 获取所有的键
print(dict01.keys())

# 获取所有的值
print(dict01.values())

# 练习01
# 输入季度，显示值
seasons = {
    "春": [1, 2, 3],
    "夏": [4, 5, 6],
    "秋": [7, 8, 9],
    "冬": [10, 11, 12]
}
# 建议字典写多个值时使用这种方式进行书写
# 字典会使代码的逻辑更加清晰，可能不会缩短代码长度
season = input("请输入季度>>>")
# 判断键是否存在
if season in seasons:
    print(seasons[season])
else:
    print("输入有误")

# 练习02
# 在控制台中录入一个字符串
# 打印这个字符串中的字符，以及出现的次数

string = input("请输入字符串")
num_dict = {}
for i in string:
    if i not in num_dict:
        num_dict[i] = 1
    else:
        num_dict[i] += 1
print(num_dict)
