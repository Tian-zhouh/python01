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
34: 34
