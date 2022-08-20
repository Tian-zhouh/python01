"""
列表:由一系列变量组成的可变序列容器
注意:列表是变量，不是常量


基础操作:
创建列表: []
添加元素: insert
获取元素:
删除元素:
"""

# 1.创建空列表的两种方式
list01 = []
list02 = list()

# 2.创建具有默认值的列表
list01 = [1, True, 1.2]
list02 = list("abcd")  # 存放的是可迭代对象
list03 = list(range(5))
print(list02)

# 3.添加元素

# append 在末尾追加元素
list02.append("q")
list02.append("t")
print(list02)

# insert(索引,元素) 在索引位置处插入元素
list02.insert(1, "x")
print(list02)

# 4.删除元素
# remove(元素) 移除指定的元素
list02.remove("b")
print(list02)

# 删除指定位置的元素
del list02[2]
print(list02)

# 5.修改元素

# 6.定位元素(索引   切片)（可以进行增删改查）
# 获取前三个元素
print(list02[:3])
list02[:3] = [1, 2, 3, 4, 5, 6]
print(list02)

# 7.遍历元素
for item in list02:
    print(item)
for item in list02[::-1]:
    print(item)
for item in range(len(list02)):
    print(list02[item])
for item in range(0, len(list02), 2):
    print(item)
for item in range(len(list02) - 1, -1, -1):
    print(item)

# 练习:在控制台中录入学生成绩,输出总分，最高分，最低分
student_num = int(input("请输入学生总数>>>"))

student_record = []
for item in range(student_num):
    student_record.append(float(input(f"请输入第{item+1}个学生成绩>>>")))

print(f"总分:{sum(student_record)}")
print(f"最高分:{max(student_record)}")
print(f"最低分:{min(student_record)}")

# 练习:在控制台中录入学生姓名。
# 要求:姓名不能重复
# 如果录入esc,则停止录入"打印学生姓名"
student_info = []
while True:
    student_name = input("请输入学生姓名>>>")
    if student_name == "esc":
        for item in student_info:
            print(item)
        break
    if student_name in student_info:
        print("该学生信息已存在")
        continue
    student_info.append(student_name)

list01 = [34, 5, 6, 78, 9, 0, 5, 8, 88, 4]
# 假设第一个元素就是最大值
# 依次与后面元素进行比较
# 发现更大的，则替换假设的
# 最后假设的就是真的最大值
max_enum = list01[0]
min_enum = list01[0]
for item in list01:
    if max_enum < item:
        max_enum = item
    if min_enum > item:
        min_enum = item

print(max_enum)
print(min_enum)
