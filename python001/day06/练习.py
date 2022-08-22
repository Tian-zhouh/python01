"""
练习1
"""
for i in [1, 2]:
    for j in [1, 2, 3]:
        print(i, j)
        break
    else:
        print("for-j")
else:
    print("for-i")
"""
输出结果:
    1,1
    2,1
    for-i
"""

"""
练习2
"""
s = "Python2best"
s1 = [3, 5, 4, 2]
# 生成列表
s2 = [item for item in s]
print(s2)
# 修改s2列表值
s2 = ['P', 'y', 't', 'h', 'o', 'n', '3']
# 向s2列表中追加元素
s2.append("!")
# 列表s2的长度
print(len(s2))
# 删除列表中的‘3’元素
s2.remove("3")
# 清空s2
s2.clear()
# 计算列表s1中的和
print(sum(s1))
# 将s1中的元素按照升序排列
s1.sort(reverse=False)
print(s1)
# 将s1的元素翻转
s1.reverse()
print(s1)