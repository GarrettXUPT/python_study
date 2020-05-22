import yitian  # 该处为pycharm进行报错，而不是程序报错，此时要避免错误，则只需要打开只该文件夹即可
from yitian import fight_on_shaolin  # 导入了模块中的某一个功能
# 导入模块时，我们看到的是将模块中的代码进行了执行，
# import yitian 如果重复导入模块，那么不会再执行模块中的代码了

# 模块的搜索路径
# import sys
# print(sys.path)

# 导入模块时执行的操作：
#   1、去判断当前正在导入的模块是否已经导入过了。
#   2、如果已经导入那么不再导入，若没导入过，则开辟内存空间，将模块中的代码放在内存空间中，并运行该模块中的代码
#   3、将当前文件的名字作为当前名称空间的名字（前提是没有as）

print(yitian.main_person_man)

yitian.main_person_man = "宝宝"  # 从另一个模块中想改变模块中变量的值，不能使用global进行修改，因为global改变得是当前模块的全局变量


yitian.fight_on_light__top()
yitian.fight_on_shaolin()
yitian.end()
