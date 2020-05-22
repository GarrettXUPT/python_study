import socket
import os
import json
import struct

client = socket.socket()

server_ip_port = ('192.168.0.114',8001)

client.connect(server_ip_port)
# 获得文件大小
filesize = os.path.getsize(r'F:\python_study\视频.mp4')

# 统计文件描述信息给服务端，服务端按照此描述信息来保存文件，命名文件等，将信息置于字典中
file_info = {
    "file_name":"视频.mp4",
    "file_size":filesize,
}
# by_dic = bytes(str(file_info), encoding='utf-8')
# 由于字典无法直接转化为bytes类型的数据，所以需要json将字典转化为json字符串，再讲字符串转化为bytes类型

# json.dumps()将字典转化为字符串
file_info_json = json.dumps(file_info)
# 将字符串转化为bytes类型
file_info_bytes = file_info_json.encode('utf-8')
# 为防止粘包现象，将文件长度打包后，与文件的描述信息数据一起发送过去
data_len = len(file_info_bytes)
data_len_struct = struct.pack('i', data_len)

client.send(data_len_struct + file_info_bytes)
sum = 0  # 作为每次读取文件长度的累计值
with open('../视频.mp4', mode="rb") as f:
    while sum < filesize:
        # 每次读取文件内容
        every_read_data = f.read(1024)  # 一次读取1024b的数据
        sum = sum + len(every_read_data)  # 将sum累加，统计长度
        client.send(every_read_data)    # 将每次读取文件的真实数据发送给服务器