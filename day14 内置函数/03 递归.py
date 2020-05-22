# 递归：自己调用自己
def func():
    print("我叫递归")
    func()
func() # maximum recursion depth exceeded while calling a Python object 超过最大递归长度 最大为1000 跑不到1000

# 树形结构的遍历