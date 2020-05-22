from multiprocessing import Process, Manager, Lock
import time

def f1(m_d1, lic):
    lic.acquire()
    tmp = m_d1['num']
    tmp = tmp - 1
    time.sleep(0.1)
    m_d1['num'] = tmp
    lic.release()

# 该示例为子进程和主进程之间的通信
if __name__ == '__main__':
    m = Manager()
    lic = Lock()
    # m_d = m.dict({'name':'alex'})  # 获得了一个manager字典，专用于进程之间数据共享
    m_d1 = m.dict({'num':100})
    p_list = []

    for i in range(10):
        p = Process(target=f1, args=(m_d1, lic))
        p.start()
        p_list.append(p)
        p.join()

    print(m_d1['num'])