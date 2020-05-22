
# obj.run()
#

class Page:
    def __init__(self,lst,pagesize):
        self.lst = lst
        self.pagesize = pagesize

    @property
    def totle(self):
        if len(self.lst) % self.pagesize == 0:
            return len(self.lst) // self.pagesize
        else:
            return (len(self.lst) // self.pagesize) + 1
    # lst
    # pagesize : 3
    def start(self): # 首页
        return self.lst[0:self.pagesize]

    def end(self): # 尾页
        return self.lst[(self.totle - 1) * self.pagesize: self.totle * self.pagesize]

    def index(self): # 指定某页显示
        ye = int(input("请输入你要跳转的页面"))
        if ye < 1:
            print("页码输入错误")
        if ye > self.totle:
            print("页码超出适用范围")
        # 计算某一页的数据
        return self.lst[(ye - 1) * self.pagesize: ye * self.pagesize]

p = Page([1,2,3,4,5,6,7,8,9],3)
print(p.start())
print(p.end())
print(p.index())
# lst
# 1 5 4 6 9 2 7 6 4 8
# pagesize = 3
# 1
# 1 5 4 lst[0:3]
# 2
# 6 9 2 lst[3:6]
# 3
# 7 6 4 lst[6:9]
# 4
# 8
# lst[(ye - 1 ) * pagezize : ye * pagesize]
