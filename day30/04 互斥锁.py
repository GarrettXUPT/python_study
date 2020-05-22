
# 互斥锁/进程锁/同步锁
# 当多个数据端共同修改一个数据时会造成数据不安全，所以需要进程锁来保证数据安全性
# 加锁以后的效果是牺牲了代码的效率，保证了数据安全

import json
from multiprocessing import Process, Lock
import time

def show_t(i):
    ticket_data = json.load(open('ticket', mode='r', encoding='utf-8'))  # 直接将文件中的字符串转化为字典
    print("%s查询剩余票数为%s" % (i, ticket_data["count"]))

def get_t(i, lic):
    lic.acquire()
    ticket_data = json.load(open('ticket', mode='r', encoding='utf-8'))
    if ticket_data['count'] > 0:
        ticket_data['count'] = ticket_data['count'] - 1
        print("%s抢票中>>>>>>" % i)
        time.sleep(0.2)
        json.dump(ticket_data, open("ticket", mode="w", encoding='utf-8'), ensure_ascii=False)
        print("%s抢票成功" % i)

    else:
        print("票已售完")
    lic.release()

if __name__ == '__main__':
    lic = Lock()
    # for i in range(10):  # 十个人查票，抢票
    #     p1 = Process(target=show_t, args=(i, ) )
    #     p1.start()
    for i in range(10):
        p2 = Process(target=get_t, args=(i, lic) )
        p2.start()

# 进程锁例程

# def f1(i,lic):
#     lic.acquire()  # 将该进程加锁,执行过程中，只有一个进程可以抢到该锁
#     print(i)
#     lic.release()  # 上述代码执行完以后解锁
#
# if __name__ == '__main__':
#     lic = Lock()
#     for i in range(10):
#         p = Process(target=f1, args=(i,lic))
#         p.start()