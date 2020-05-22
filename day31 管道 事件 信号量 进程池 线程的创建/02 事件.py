from multiprocessing import Process, Event

e = Event()  # 创建时间对象，这个对象的初始状态为FALSE

print("进程运行到这里了,e的状态为%s" % e.is_set())  # 进程运行到这里了,e的状态为False
e.set()  # 将初始状态False改为True
# e.clear()  # 将true 改为false
e.wait()  # 若事件对象状态为FALSE，则程序会在wait这里等待

print("进程过了wait,e的状态为%s" % e.is_set())  # 进程过了wait,e的状态为True
