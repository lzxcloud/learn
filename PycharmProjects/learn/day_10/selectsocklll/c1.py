#!/usr/bin/env python3

import socket
ip_port = ('127.0.0.1', 9999)

sk = socket.socket()
sk.connect(ip_port)
text = str(sk.recv(1024),encoding='utf-8')
print(text)
