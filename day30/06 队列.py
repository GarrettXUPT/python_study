from multiprocessing import Process, Queue

q = Queue(3)  # 创建一个队列对象，队列长度为3，先进先出

q.put(1)
q.put(2)
q.put(3)
print(q.qsize())  # 3 返回当前对列中元素的数量
print(q.full())  # True 判断队列是否已经装满，但是该种方法并不可靠
# q.put(4) 放入数据时，当队列中已满，会在put的地方阻塞
try:
    q.put_nowait(4)  # 不阻塞程序，但是会报错，可以通过报错来进行其他的处理
except:
    print("队列满了")

q.get()
q.get()
q.get()
try:
    q.get_nowait()  # 若队列中的元素都被取出，则在此处会进行阻塞
except:
    print("队列已空")





