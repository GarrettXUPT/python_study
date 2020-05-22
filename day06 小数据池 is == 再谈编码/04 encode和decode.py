# s = "我今天挺困的" # 21个utf-8的字节 14 个gbk
# bs = s.encode("utf-8")
# # b'\xe6\x88\x91\xe4\xbb\x8a\xe5\xa4\xa9\xe6\x8c\xba\xe5\x9b\xb0\xe7\x9a\x84
# bss = s.encode("gbk")
# # b'\xce\xd2\xbd\xf1\xcc\xec\xcd\xa6\xc0\xa7\xb5\xc4'
# # bytes 不是给人看的，而是给机器用的
# # print(bss)

bss = b'\xce\xd2\xbd\xf1\xcc\xec\xcd\xa6\xc0\xa7\xb5\xc4'
# utf-8 与 gbk 不能直接进行转化，不使用unicode进行转化

# 将字节转化回字符串
bs = bss.decode("gbk") # 我今天挺困的

print(bs)

# 在程序中使用英文 并不影响整个编码

