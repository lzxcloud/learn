#!/usr/bin/env python3
import socket
import os

ip_port = ('127.0.0.1', 9999)

sk = socket.socket()
sk.connect(ip_port)

ret_byted = sk.recv(1024)
ret_str = str(ret_byted, encoding='utf-8')
print(ret_str)

# sk.sendall(a)

# server_reply = sk.recv(1024)

# print(str(server_reply, encoding='UTF-8'))

# 发送当前文件大小

size = str(os.stat('p1.jpg').st_size)
sk.sendall(bytes(size, encoding='utf-8'))
ack = str(sk.recv(1024), encoding='utf-8')
print(ack)
if ack == 'send':
    with open('p1.jpg', 'rb') as f:
        for line in f:
            sk.sendall(line)
    print('over')
    sk.close()

