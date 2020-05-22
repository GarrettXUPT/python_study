import os

# # 必须要记住，很常用
# os.makedirs("bao/baby/黄晓明")  # 可一次性创建多级目录，如果存在，则继续，若不存在，则会自动创建
#
# os.mkdir("baby/byby/sss")  # 目的是创建sss，所以上层文件夹必须存在

# os.removedirs("bao")  # 目录不为空，则不能删除，删除当前目录级中的所有空文件夹
# 需要记住
# os.rmdir("baobao")  # 指定文件夹删除

print(os.popen("dir").read())  # 执行shell脚本或者cmd命令

print(os.getcwd())  # 当前程序所在的文件夹

# os.path 和路径相关内容
print(os.path.abspath('user_info'))  # 将相对路劲改为绝对路径