"""
for for
"""
"""
在控制台内输出
*****
*****
*****
"""
for i in range(3):
    for j in range(5):
        print("*", end="")
    print()

"""
在控制台输出
******
######
******
######
结论:外层循环控制行     内层循环控制列
"""
for i in range(2):
    for j in range(6):
        print("*", end="")
    print()
    for j in range(6):
        print("#", end="")
    print()

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for i in range(4):
    for j in range(6):
        if i % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print()
"""
画出
#
##
###
####
"""
for i in range(5):
    for j in range(i):
        print("#", end="")
    print()

"""
画出
####
 ###
  ##
   #
"""
for i in range(5):
    for j in range(i):
        print(" ", end="")
    for j in range(4 - i):
        print("#", end="")
    print()

"""
列表中是否具有相同元素
[1,4,7,4,8,0,6]
"""
list1 = [1, 4, 7, 4, 8, 0, 6]
list2 = list(set(list1))
if list1 == list2:
    print(False)
else:
    print(True)

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] == list1[j]:
            print(list1[i])
"""
对列表进行排序
核心，将元素两两进行比较
    发现更大的或者更小的规则进行交换
        降序      升序
"""

for i in range(len(list1) - 1):
    for j in range(i + 1, len(list1)):
        if list1[i] < list1[j]:
            temp = list1[j]
            list1[j] = list1[i]
            list1[i] = temp
print(list1)

# 做编程要保持一种开放的态度

