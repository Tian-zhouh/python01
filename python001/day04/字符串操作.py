"""
数学运算符
+ 用于拼接两个容器
+= 原容器与右侧容器拼接，并绑定新容器
*  重复生成容器元素
*= 用原容器生成重复元素，并绑定新变量

比较运算符

成员运算符
"""
# 1.数学运算
str01 = "悟空"
str02 = "八戒"
str03 = str01 + str02
print(str03)
# 创建新对象

str01 += str02
print(str01)

print(str02 * 2)

str02 *= 2
print(str02)

print(str01 > str02)

# 2.成员运算符
str03 = "猥琐发育，别浪"
print("猥琐" in str03)

# 索引
"""
作用：访问容器元素
->正向索引
<-反向索引
索引=len(元素)-1
"""
# 索引不能越界
str04 = "abcde"
print(str04[0])
print(str04[-1])

# 切片
"""
作用:从容器中取出相应的元素，重新组成一个容器
语法:容器[开始索引:结束索引:步长]
切片即使越界也不会报错
"""
str05 = "asdgjkhdklioq"
print(str05[2:9:3])
print(str05[::-1])

# 练习:在控制台中获取一个字符串
# 1.打印第一个字符
# 2.打印最后一个字符串
# 3.打印中间的字符串（如果是奇数打印中间的字符串）
# 4.打印倒数三个字符
# 5.倒序打印字符串

input_str = input("请输入一个字符串>>>")
# 1.
print("*" * 20)
print(input_str[0])
# 2.
print(input_str[-1])
# 3.
if len(input_str) % 2 == 1:
    print(input_str[int(len(input_str) / 2)])

# 4.
print(input_str[-3:])
# 5.
print(input_str[::-1])

# 练习:在控制台中输入一个整数，根据整数打印一个矩形
input_int = int(input("请输入一个整数>>>"))
for i in range(input_int):
    if i == 0 or i == input_int - 1:
        print("*" * input_int)
    else:
        print("*" + " " * (input_int - 2) + "*")
