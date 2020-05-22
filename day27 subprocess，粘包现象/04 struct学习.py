
import struct  # 打包数据的工具

num = 100
# 将num转化为4个字节,打包，将int类型打包为4个字节的bytes类型
byt = struct.pack('i', num)
print(byt)  # b'd\x00\x00\x00'

# 解包，将bytes类型的数据转化为int类型的数据
int_num = struct.unpack('i', byt)[0]
print(int_num)  # 100

