"""
字符串字面值
    单引号和双引号的区别
    单引号和双引号没有却别
    三引号可以进行换行，单引号和双引号不支持换行操作
"""

# 单引号与双引号功能相同
str01 = "大家好"
str01 = '大家好'

# 三引号：所见即所得
str01 = """大家好"""
str01 = '''大
家好'''
print(str01)

str02 = "我爱'python'."
print(str02)

# 转义符：改变原始含义的特殊字符
# 如果字符串内部，需要使用多种引号，使用转义符
str03 = "我爱\"python\""
print(str03)

# \n 换行
str04 = "大家好，\n我是QTX."
print(str04)

# \t  水平制表格 ，tab键
str04 = "大家好,\t我是***"

# \\ 反斜杠
str04 = "大家好，\\我是***"

# r 原始字符串，取消转义
str05 = r"\d\n\s"

# \0  空字符
str06 = "\0"
