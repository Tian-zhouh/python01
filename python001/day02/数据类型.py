"""
数据类型
"""
# 整形 int
# 十进制，二进制，八进制，十六进制
# 十进制
num01 = 1
# 二进制(逢二进一)
num02 = 0b1101
# 八进制(逢八进一)
num03 = 0o765
# 十六进制(逢十六进一)
num04 = 0xa2f
print(num01)
print(num02)
print(num03)
print(num04)
# 小整数对象池  0-256的对象不会被释放
# 主要体现在交互式方式中，文件式小整数对象池不适用
print(id(num01))

# 浮点型 float
f01 = 1.0
f02 = 1.234e2
f03 = 1.234e-3
print(f01)
print(f02)
print(f03)

# 字符串 string
str01 = "你好呀"
str02 = "10"
str03 = "1.5"
print(str01)
print(str02)
print(str03)
print("10 + " + "2", end=" = ")
print(10 + 2)

# 复数 complex
# 由虚部和实部组成的数字
# 虚部由j和J结尾
# 字面值：1j  1+1j  1-1j
c01 = 1j
c02 = 1 + 1j
print(c02)
print(type(c02))

# 布尔型 bool
bool01 = True
bool02 = False

# 数据类型之间的转换
str_score = input("请输入成绩>>>")
# input函数的结果就是str，如果需要做数学运算，必须转换成数字
print(type(str_score))
str_score = float(str_score)
print(type(str_score))
