import time
for i in range(20):
    print('\r'+i*'*', end='')  # \r 表示每一次打印都要到行首去打印
    time.sleep(0.2)