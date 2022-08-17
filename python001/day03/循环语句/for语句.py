"""
for语句
用来遍历可迭代对象的数据元素
可迭代对象是指依次获取数据元素的对象
"""
for item in "可迭代对象":
    print(item)

# range(开始点，结束点，间隔)俗称整数生成器
# 熟练正序，倒序，跳跃式生成数字
for item in range(1, 5, 2):
    print(item)

for item in range(5, -1, -1):
    print(item)

# whiile不能使用整数生成器

# 练习01
# for num in range(0, 5):
#     input01 = input("请输入第一个变量>>>")
#     input02 = input("请输入第二个变量>>>")
#     input01, input02 = input02, input01

# 练习02:
# 随机加法考试
# 随机产生两个数字
# 在控制台中获取两个数字的相加结果
# 如果输入正确，成绩累加10分，如果输入错误，成绩扣除5分，总共5道题，最后显示总分

import random

results = 0
for i in range(5):
    random_number01 = random.randint(0, 100)
    random_number02 = random.randint(0, 100)
    answer = random_number01 + random_number02
    result = int(input(f"请输入{x} + {y}= "))
    if result == answer:
        results += 10
    else:
        results -= 5
print(f"最终得分{results}")
