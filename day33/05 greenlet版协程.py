

from greenlet import greenlet
import time

def f1(s):
    print('第一次f1', s)
    g2.switch()  # 切换到g2这个对象的任务去执行
    time.sleep(1)
    print('第二次f1', s)
    g2.switch()

def f2():
    print("第一次f2")
    g1.switch()
    time.sleep(1)
    print("第二次f2")



g1 = greenlet(f1)  # 实例化一个greenlet对象，并将任务名称作为参数传入
g2 = greenlet(f2)

g1.switch('name')  # 执行g1对象中的任务

# 第一次f1
# 第一次f2
# 第二次f1
# 第二次f2