"""
字符串是由一系列字符组成的不可变序列容器
"""
name = "悟空"
name = "孙悟空"
print(name)  # 不是将字符串悟空改变为孙悟空
# 而是创建了新的字符串对象，孙悟空，替换变量name中存储的地址

# 编码
# 解码
# ASCII编码
# GBK编码  兼容ASCII码表
# unicode字符集
# UTF-8编码

# 字符-》编码值
print(ord("a"))
print(ord("b"))
print(ord("孙"))

# 编码值-》字符
print(chr(97))
print(chr(23385))

# 练习01：
# 在控制台中获取一个字符串，打印每个字符的编码值

Str = input("请输入字符串>>>")
for code in Str:
    print(ord(code))
# 练习02：
# 在控制台中循环输入编码值，显示字符，直到输入负数时退出
while True:
    Code = int(input("请输入一个正整数>>>"))
    if Code <= 0:
        break
    print(chr(Code))
