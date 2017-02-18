#!/usr/bin/env python3

import socket
ip_port = ('127.0.0.1', 9999)

sk = socket.socket()
sk.connect(ip_port)

ret_byted = sk.recv(1024)
ret_str = str(ret_byted,encoding='utf-8')
print(ret_str)
# sk.sendall(a)
#
# server_reply = sk.recv(1024)
#
#
# print(str(server_reply, encoding='UTF-8'))



while True:
    inp = input("请输入内容")
    if inp == "q":
        sk.sendall(bytes(inp, encoding='UTF-8'))
        break
    else:
        sk.sendall(bytes(inp, encoding='UTF-8'))
        ret = str(sk.recv(1024), encoding="UTF-8")
        print(ret)
