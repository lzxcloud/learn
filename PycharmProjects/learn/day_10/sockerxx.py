#!/usr/bin/env python3

import socket

ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print('server waiting...')
    conn,addr = sk.accept()
    #对方的 conn连接 addr
    # client_data = conn.recv(1024)
    # print(client_data)
    a = bytes('不要回答,不要回答,不要回答', encoding='UTF-8')
    conn.sendall(bytes('欢迎致电lzx', encoding='UTF-8'))
    while True:
        ret_byte = conn.recv(1024)
        ret_str = str(ret_byte, encoding='UTF-8')
        if ret_str == 'q':
            break
        else:
            conn.sendall(bytes(ret_str + '好', encoding="UTF-8"))
