# 练习1:在控制台中随意录入多个字符串
# 按q退出，再显示所有不重复的字符串
# subs = ""
# while True:
#     strs = input("请输入字符串")
#     if strs == "q":
#         break
#     subs += strs
# set01 = set(subs)
# str01 = str(set01)
# print(str01)

# 更优方法
set_target = set()
while True:
    str_input = input("请输入")
    if str_input == "q":
        break
    set_target.add(str_input)
for item in set_target:
    print(item)

# 练习02：经理:[曹操,刘备,孙权]  技术员:[曹操,刘备,张飞,关羽]
# 计算:既是经理也是技术员的有谁
# 是经理但不是技术员的有谁
# 是技术员但不是经理的有谁
# 张飞是经理吗？
# 身兼一职的有谁?
# 经理和技术员总共有多少人?
set01 = frozenset(["曹操", "刘备", "孙权"])
set02 = frozenset(["曹操", "刘备", "张飞", "关羽"])
print("既是经理也是技术员的有:" + str(set01 & set02))
print("是经理但不是技术员的有:" + str(set01 - set02))
print("是技术员但不是经理的有:" + str(set02 - set01))
print("张飞是经理吗?" + str(("张飞" in set01)))
print("身兼一职的有:" + str(set01 ^ set02))
print("经理和技术员一共有:" + str(len(set01 | set02)))
