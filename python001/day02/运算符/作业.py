"""
day02 作业

1.（理论，代码，图示）三合一
2. 当天练习，做到独立完成
3. 温度换算器(华氏度，摄氏度，开氏度)
    摄氏度 = （华氏度 - 32） / 1.8
    华氏度 = （摄氏度 * 1.8） + 32
    开氏度 = (摄氏度 + 273.15)
    练习:
        在控制台中获取华氏度，计算摄氏度
        在控制台中获取摄氏度，计算华氏度
        在控制台中获取摄氏度，计算开氏度
4.在控制台中获取圆形半径计算面积与周长
    面积:3.14 * r ** 2
    周长:3.14 * 2 * r
5.优化商品购买问题，如果金额不足，提示还差多少钱
    如果金额足够，提示应找回多少钱
    尝试 如果总价到达100元打8折
6. 看书
"""

# 练习03
check = int(input("1:摄氏度，2:华氏度，3:开氏度>>>"))
temperature = float(input("请输入温度>>>"))
if check == 1:
    c = temperature
    Fahrenheit = (c * 1.8) + 32
    Degrees = c + 237.15
elif check == 2:
    c = (temperature - 32) / 1.8
    Fahrenheit = temperature
    Degrees = c + 273.15
elif check == 3:
    c = temperature - 273.15
    Fahrenheit = (c * 1.8) + 32
    Degrees = temperature
else:
    c = Fahrenheit = Degrees = 0
print("摄氏度:" + str(c))
print("华氏度:" + str(Fahrenheit))
print("开氏度:" + str(Degrees))

# 练习02
radius = float(input("请输入半径>>>"))
perimeter = round(radius * 2 * 3.14, 3)  # 四舍五入，保留三位小数
# round()函数可以四舍五入
area = round(3.14 * radius ** 2, 3)
print("周长为:" + str(perimeter))
print("面积为:" + str(area))

# 练习03
price = float(input("请输入商品单价>>>"))
count = int(input("请输入购买商品数量>>>"))
money = float(input("请输入支付金额"))
pay = price * count
if money < pay:
    print("支付金额不足，还差: " + str(round(pay - money), 3) + " 元")
else:
    if pay > 100:
        print("优惠: " + str(round(pay * 0.2, 3)) + " 元")
        pay *= 0.8
    print("支付: " + str(round(pay, 3)) + " 元")
    print("找零: " + str(round(money - pay, 3)) + " 元")
