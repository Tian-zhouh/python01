"""
字符串与列表
"""
# 根据某些逻辑，拼接成一个字符串

# result = ""
#
# for item in range(10):
#     result += str(item)
# print(result)
# 上述方法不推荐，每次拼接创建一个新对象，替换变量地址

list_result = []
for item in range(10):
    # 不会每次拼接都生成一个新列表
    list_result.append(str(item))
# 将列表使用连接符，合成一个字符串
result = "-".join(list_result)
print(result)

# 将列表使用分隔符，拆分成一个列表
list = result.split("-")
print(list)
