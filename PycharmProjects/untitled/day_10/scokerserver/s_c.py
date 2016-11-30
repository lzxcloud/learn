#!/usr/bin/env python3
import socket
ip_port = ('127.0.0.1', 9999)
while True:
    sk = socket.socket()
    sk.connect(ip_port)
    text = str(sk.recv(1024), encoding='utf-8')
    print(text)
    choose = input('请输入号码')
    sk.sendall(bytes(choose, encoding='utf-8'))
    textb = str(sk.recv(1024), encoding='utf-8')
    print(textb)
    sk.close()