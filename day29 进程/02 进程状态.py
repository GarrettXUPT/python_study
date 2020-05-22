# 程序开始运行之后，并不是立即执行代码，而是会进入就绪状态，等待操作系统调用执行

# 程序运行状态
import time
print("程序正在运行")
# 进行用户操作，进入阻塞状态，等待用户输入结束后，又进入就绪状态，等待操作系统调用执行
name = input(">>>>")
# 执行
print(name)
# 阻塞 运行
time.sleep(1)
print("程序结束")
# 结束