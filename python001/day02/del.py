# del 语句
# del 变量名

a = "清醒啊"
b = a

print(a)
del a
print(b)
# 至于变量值何时被删除和引用计数有关

# None数据类型
name01 = "八戒"
name02 = "悟空"
name02 = name01

del name01
name02 = None
