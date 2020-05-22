def func():
    '''
    :param name:参数 name
    :param age : age是干嘛的
    :return:返回xxx
    :creator:创建者
    :author:作者
    :data:创建日期
    '''
    print("你好")

# a = func
#
# print(a.__name__) # 查看原始函数内容
# print(a.__doc__) # 查看该函数内容

# 闭个包吧
def wrapper():
    name = "你好啊"
    def inner():
        print(name)
    return inner

ret = wrapper()
ret()
print(ret.__name__)  # 查看真正执行的函数
