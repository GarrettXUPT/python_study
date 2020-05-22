# # 栈
# # 指针：指向下一个存放数据的位置
# # 先进后出
# class Stack_Full_Exception(Exception):
#     pass
#
#
# class Stack_Empty_Exception(Exception):
#     pass
#
#
# class Stack:
#     def __init__(self, size):
#         self.size = size
#         self.lst = []  # 存放数据列表
#         self.top = 0  # 栈顶指针
#
#     # 入栈
#     def push(self, el):
#         if self.top >= self.size:
#             raise Stack_Full_Exception("栈溢出")
#         else:
#             self.lst.insert(self.top, el)  # 放元素
#             self.top = self.top + 1  # 栈顶指针向上移动一项
#
#     # 出栈
#     def pop(self):
#         if self.top == 0:
#             raise Stack_Empty_Exception("栈已空")
#         else:
#             self.top = self.top - 1
#             el = self.lst[self.top]
#             return el
#
#
# s = Stack(6)
# s.push("宝宝")
# s.push("宝狼")
# s.push("你好")
# s.push("好什么好")
# s.push("有多好")
# s.push("你说啊")
#
#
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())




# 队列
# 先进先出 后进后出

# import queue
#
# q = queue.Queue()
# q.put("李继承1")
# q.put("李继承2")
# q.put("李继承3")
# q.put("李继承4")
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())


# 双向队列
from collections import deque

d = deque()  # 创建双向队列
d.append("宝宝")  # 此时添加时在右侧添加
d.append("no")
d.append("way")
d.append("哈哈")
d.appendleft("呵呵")  # 从左边添加
d.appendleft("嘿嘿")

print(d.pop())  # 从右边取出数据
print(d.popleft())  # 从左边拿数据
print(d.popleft())
print(d.popleft())
print(d.popleft())
print(d.popleft())
