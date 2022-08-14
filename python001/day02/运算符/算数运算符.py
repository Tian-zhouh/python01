"""
算数运算符
"""

num01 = 5
num02 = 2
print(num01 / num02)
print(num01 // num02)
print(num01 % num02)

# 取余的作用
# 1.判断一个数能否被另外一个数整除
print(num01 % 5 == 0)
print(num01 % 2 == 0)

# 2.获取个位
print(67 % 10)

# 注意数据类型不统一的问题

# 比较运算符：略
# 返回布尔值


# 增强运算符
num03 = 1
print(num03 + 1)
print(num03)

num04 = 1
num04 += 1
print(num04)

# 练习01：在控制台中获取一个商品单价，再获取一个商品数量，获取一个金额，计算应该找零多少
price = float(input("商品单价>>>"))
num = int(input("商品数量>>>"))
mony = float(input("支付金额>>>"))

change = mony - price * num

print("找零:" + str(change))

# 练习02：在控制台中获取小时、分钟、秒，计算总秒数
hour = int(input("请输入小时>>>"))
minute = int(input("请输入分钟>>>"))
second = int(input("请输入秒>>>"))

result = hour * 60 ** 2 + minute * 60 + second

print("一共有 " + str(result) + " 秒")

# 练习03:古代的称一斤16两
# 在控制台中输入两，换算出几斤几两
weight = int(input("请输入多少两>>>"))
intage = weight // 16
floats = weight % 16
print("一共有 " + str(intage) + " 斤， " + str(floats) + " 两")
