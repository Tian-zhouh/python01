"""
1.三合一
2.当天练习独立完成
3.内存图:
list01 = ["a",(1,2,3),{"b":"B","c":"C"}]
list02 = list01
list03 = list01[:]
list02[0] = "b"
print(list01[0])
list02[2]["b"]="BB"
print(list01[2]["b"])
list03[0] = "bb"
print("list01[0]")

4.在控制台录入5个学生信息(姓名/性别/年龄)
#数据结构列表中嵌套字典

5.猜拳
规则:系统随机出拳,在控制台中循环猜测
提示:将胜利的策略存入容器
(
    ("石头","剪刀")
    ("剪刀","布")
    ("布","石头")
)
将用户猜的拳与系统出拳形成一个元组

6.群讨论:
(1) ==  is  的区别:
(2) 讨论 列表中的元素如何根据条件批量删除
    [1,2,34,5,5,6,79,0,8]
    要求删除大于3的数字
"""
# 04
student_list = []
for i in range(5):
    inp_name = input("请输入学生姓名>>>")
    inp_age = input("请输入学生年龄>>>")
    inp_sex = input("请输入学生性别>>>")
    student_list.append({
        "name": inp_name,
        "age": inp_age,
        "sex": inp_sex
    })
print(student_list)
for stu in student_list:
    for key, value in stu.items():
        print("%s--%s" % (key, value))

# 05
win_stage = (
    ("石头", "剪刀"),
    ("剪刀", "布"),
    ("布", "石头")
)
stage = ("剪刀", "石头", "布")
import random

count = 0
for item in range(3):
    tupe_compute = stage[random.randint(0, 2)]
    while True:
        tuple_user = input("请输入'剪刀','石头','布'>>>")
        if tuple_user not in stage:
            print("请重输")
            continue
        else:
            break
    tuple_result = (tuple_user, tupe_compute)
    if tuple_user == tupe_compute:
        print("平局")
    elif tuple_result in win_stage:
        print("赢了")
        count += 1
    else:
        print("输了")
    if count >= 2:
        print("胜利两局")
        break
else:
    print("你输了")

# 6.2
list01 = [1, 2, 34, 5, 5, 6, 79, 0, 8]
list02 = [item for item in list01 if item > 3]
[list01.remove(item) for item in list02]
print(list01)
2：07
