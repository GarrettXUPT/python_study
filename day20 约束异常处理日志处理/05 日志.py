import logging
import traceback

# 配置好日志的处理，默认就是GBK
# logging.basicConfig(filename='x1.txt',  # 将日志信息写入的文件名
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
#                     datefmt = '%Y-%m-%d %H:%M:%S',  # 时间的格式
#                     level=10)  # 当前配置表示 10以上的分数都会写入日志
# # 向日志文件写入内容
# logging.critical("今天挺开心的")  #大概是50级，几乎是最高的，系统要奔溃（当机）时候使用
# logging.error("昨天感觉还行")  # 大概40级，平时使用最多
# logging.warning("明天可能会不太行")  # 大概30级 警告级别
# logging.info("提示") # 20级
# logging.debug("开发的时候，需要开启")  # 10
# logging.log(999,"感觉不太行")

file_handler = logging.FileHandler('l.log', 'a', encoding = 'utf-8')
file_handler.setFormatter(logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s' ))
logger = logging.Logger('百度贴吧', level = logging.DEBUG)
logger.addHandler(file_handler)

logger.error("我才不去呢，太远了")


class Gender_Exception(Exception):
    pass


class Person:
    def __init__(self,name, gender):
        self.name = name
        self.gender = gender
        logger.info(f"创建了一个人，这个人的名字是{self.name},这个人的性别是{self.gender}")


    def xi_zao(self):
        print(f"{self.name}在洗澡")

class Zao_Tang:
    def nan(self, ren):
        if ren.gender == "男":
            print("欢迎光临")
        else:
            raise Gender_Exception("我这里是男澡堂")
    def nv(self, ren):
        if ren.gender == "女":
            print("欢迎光临")
        else:
            raise Gender_Exception("我这里是女澡堂")

try:

    p1 = Person("Garrett", "男")
    p2 = Person("Walker", "女")

    z = Zao_Tang()

    z.nan(p1)
    z.nan(p2)

    z.nv(p1)
    z.nv(p2)
except Gender_Exception:
    print("走混了")
    logger.error("走混了....")
    logger.error(traceback.format_exc())  # 把堆栈信息记录在日志里