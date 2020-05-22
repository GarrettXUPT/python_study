import socket

server = socket.socket()  # TCP协议的网络通信
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 此处可解决地址重用问题

ip_port = ('192.168.43.39',8001)

server.bind(ip_port)

server.listen(5)  # listen中的参数表示，在当前通道正在被占用的情况下，后面排队的人数可以有5个

while 1:

    conn,addr = server.accept()

    while 1:
        from_client_msg = conn.recv(1024)

        print("宝宝说：", from_client_msg.decode('utf-8'))

        if from_client_msg.decode('utf-8') == "byebye":
            break


        To_client_msg = input("宝浪说：")

        conn.send(To_client_msg.encode('utf-8'))

    conn.close()