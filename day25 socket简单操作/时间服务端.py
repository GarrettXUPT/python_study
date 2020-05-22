import socket, time
server = socket.socket()

ip_port = ('192.168.43.39',8001)
server.bind(ip_port)

server.listen()
conn,addr = server.accept()

while 1:
    from_client_msg = conn.recv(1024)
    from_client_time = float(from_client_msg.decode('utf-8'))

    struct_time = time.localtime(from_client_time)
    from_client_struct= time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
    print(from_client_struct)