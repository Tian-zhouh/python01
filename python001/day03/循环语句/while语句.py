"""
循环语句
while

while 条件:
    执行代码
"""

while True:
    str_usd = float(input("请输入美元>>>"))
    rmb = str_usd * 6.708
    print(rmb)
    if input("按e键退出>>>") == "e":
        break  # 退出循环体

# 练习：在控制台中分别获取两个整数，一个作为开始值，一个作为结束值
# 请输出中间的数字

start = int(input("请输入一个整数"))
end = int(input("请输入第二个整数"))
while True:
    if start >= end:
        start, end = end, start
    start += 1
    if end <= start:
        break
    else:
        print(start)

# 更优的算法
while start < end - 1:
    start += 1
    print(start)

# 练习02:一张纸的厚度是0.01毫米
# 请问，对着多少次可以超过珠穆朗玛峰8844.43
paper = 0.01
count = 0
while paper <= 8844.43*1000:
    count += 1
    paper *= 2
print(paper)
print(count)
