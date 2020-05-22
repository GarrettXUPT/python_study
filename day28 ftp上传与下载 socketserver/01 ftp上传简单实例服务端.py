import socket
import json
import struct

server = socket.socket()
ip_port = ('192.168.0.114',8001)

server.bind(ip_port)
server.listen(5)

conn, addr = server.accept()
# 首先接收文件的描述长度
struct_data_len = conn.recv(4)
data_len = struct.unpack('i', struct_data_len)[0]
# 通过文件信息的长度，将文件的描述信息全部接收
print("data_len=", data_len)
file_info_bytes = conn.recv(data_len)
# 将文件转化为字典类型，以便操作
file_info_json = file_info_bytes.decode("utf-8")
file_info_dict = json.loads(file_info_json)
print(file_info_dict)
# 统计每次接收的累计长度
recv_sum = 0
# 根据文件信息，指定文件保存路径与名称
file_path = 'F:\python_study\day28 ftp上传与下载 socketserver' + '\\' + file_info_dict["file_name"]
# 接收文件的真实数据
with open(file_path, mode="wb") as f:
    # 循环接收，循环结束的依据是文件描述信息中文件的大小
    while recv_sum < file_info_dict["file_size"]:
        every_recv_data = conn.recv(1024)
        recv_sum = recv_sum + len(every_recv_data)
        f.write(every_recv_data)