"""
day01 复习
    1.python 定义: 免费的，开源的，跨平台的，动态的，面向对象的编程语言
    2.执行方式: 交互式，文件式
    3.执行过程: 源代码 __编译__> 字节码 __解释-执行__>机器码
    4.函数:
        print(参数)  将括号中的内容显示到控制台
        input(参数)  从控制台中获取信息
    5.变量:
"""

# 练习：在控制台中获取两个变量，让两个变量交换输出

param01 = input("请输入>>>")
param02 = input("请输入>>>")
param03 = param01
param01 = param02
param02 = param03
print(param01)
print(param02)

