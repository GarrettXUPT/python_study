# coding=utf-8
# name = input("请输入你的名字：")
# address = input("请问你来自哪里：")
# wife = input("你的老婆是：")
# not_like = input("请输入你不喜欢谁：")
#
# #print("我叫"+name+"，我来自"+address+", 我的老婆是"+wife+", 我不喜欢"+not_like)
#
# # 格式化输出
# # print("我叫%s，我来自%s，我老婆是%s，我不喜欢%s" % (name, address, wife, not_like))
#
# # 新版本的格式化输出
# print(f"我叫{name}, 我来自{address}, 我老婆时候{wife}, 我不喜欢{not_like}")

#f"{变量}"
# %s 表示字符串的占位string 。全能的占位
# %d 表示占位数字 只能放入数字digital
# %f 表示占位浮点数float

# 如果一句话使用了格式化输出，% 就是占位， 如果想写正常的 % 那么应该输入 %% 表示转义

# print("我的名字是%s，我度过了30%的人生" % "周杰伦")  # 报错
print("我的名字是%s，我度过了30%%的人生" % "周杰伦")
