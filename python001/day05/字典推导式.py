"""
字典推导式
"""
# key:数字  value:数字平方
dict01 = {}
for item in range(1, 10):
    dict01[item] = item ** 2
print(dict01)

# 字典推导式
dict02 = {item: item ** 2 for item in range(1, 10)}
print(dict02)

# 只想找出偶数的
dict03 = {item: item ** 2 for item in range(1, 10) if item % 2 == 0}
print(dict03)

# 练习01:
# 有一个列表，存放的有["张三丰","无忌","赵敏"]
# 做成{"张三丰":3,"无忌":2,"赵敏":2}
list_name = ["张三丰", "无忌", "赵敏"]
list_num = (3, 2, 2)
dict_people = {list_name[item]: list_num[item] for item in range(0, len(list_name))}
dict_people = {item: len(item) for item in list_name}
print(dict_people)

# 练习02:
# ["张三丰","无忌","赵敏"]
# [101,102,103]
# (1)根据两个列表形成一个字典：键是姓名，值时房间号
# (2)将字典的键与值进行翻转.即key变成房间号，值变成姓名
list_room = [101, 102, 102]
dict_room = {list_name[item]: list_room[item] for item in range(0, len(list_name))}
print(dict_room)
# dict_room = {value: key for key, value in dict_room.items()}
# print(dict_room)

list03 = [(value, key) for key, value in dict_room.items()]
print(list03)
