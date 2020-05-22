from collections import namedtuple

# 类
p = namedtuple("Point", ["x", "y"])

# 对象
p1 = p(10, 20)
print(p1)
print(p1.x)
print(p1.y)

# 上述代码相当于
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
