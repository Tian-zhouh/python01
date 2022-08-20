"""
在控制台中循环录入字符串，输入q时退出
然后显示一个新的字符串
"""
list_result = []
while True:
    str_input = input("请输入>>>")
    if str_input == "q":
        break
    # 1.使用列表拼接
    list_result.append(str_input)

# 2.使用join合并
str_list = "".join(list_result)
print(str_list)

# 字符串 --》 列表
list01 = list("abc")
list02 = "a-b-c".split("-")

"""
判断字符串是否是回文
提示:字符串翻转 <--重点
"""
str01 = "上海自来水来自海上"
str02 = str01[::-1]
if str01 == str02:
    print("是回文")
else:
    print("不是回文")

"""
一注彩票7个球
前六个是红球:1--33之间的数字，且不能重复
最后一个是蓝球:1--16之间的数字
（1）在控制台中购买彩票
（2）随机产生一注彩票
"""
ticket = []
# 前6个红球
while len(ticket) < 6:
    number = int(input("请输入第%d个红球号码>>>" % (len(ticket) + 1)))
    if number not in range(1, 34):
        print("不在范围内")
        continue
    elif number in ticket:
        print("该号码已经存在")
        continue
    ticket.append(number)
# 蓝球
while True:
    number = int(input("请输入篮球号码>>>"))
    if number in range(1, 17):
        ticket.append(number)
        break
    else:
        print("不在范围内")

# 只是将列表转换成字符串  再显示  并不能获取每个元素，
# 若想获取每个元素则需要使用for循环遍历
print(ticket)

import random

ticket = []
while len(ticket) < 6:
    number = random.randint(1, 33)
    if number not in ticket:
        ticket.append(number)
ticket.sort()  # 排序
ticket.append(random.randint(1, 16))

# 需求:对列表指定范围的元素进行排序
# 通过切片返回新列表
temp = ticket[:6]
# 对新列表进行排序
temp.sort()
# 将新列表赋值给原列表
ticket[:6] = temp
print(ticket)
