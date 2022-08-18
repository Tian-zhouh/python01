"""
定义:生成一定格式的字符串
语法:字符串%(变量)
"""
name = "qtx"
age = 32
msg = "我的名字是%s,年龄是%d" % (name, age)
print(msg)
msg = f"我的名字是{name},年龄是{age}"
print(msg)
msg = "我的名字是{},年龄是{}".format(name, age)
print(msg)

msg = "整数是:%d" % (32)
print(msg)
msg = "整数是:%8d." % (32)
print(msg)
msg = "整数是:%-8d." % (32)
print(msg)
msg = "整数是:%05d" % (32)  # 时间
print(msg)
msg = "整数是:%+5d" % (32)
print(msg)
msg = "整数是:%6.2f" % (32.12112)  # 宽度.精度
print(msg)

import time

# 练习：在控制台中显示120秒倒计时
times = 2

while times > 0:
    second = 60
    times -= 1
    while second > 0:
        print("%02d:%02d" % (times, second))
        second -= 1

for second in range(120, -1, -1):
    time.sleep(1)
    print("%02d:%02d" % (second // 60, second % 60))
