
from threading import Thread
import queue

q = queue.Queue(3)  # 先进先出队列FIFO,队列的长度为3

q.put(1)
q.put(2)
print('当前队列内容长度%s'%q.qsize())  # 当前队列内容长度2
print('查看队列是否已经满了', q.full())  # 查看队列是否已经满了 False
q.put(3)

print(q.get())
print(q.get())
print(q.get())

# def f1():
#     pass
#
# if __name__ == '__main__':
#     t = Thread(target=f1, )
