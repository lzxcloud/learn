#!/usr/bin/env python3
import socket

ip_port = ('127.0.0.1', 9999)
def file_serer(ip_port):
    sk = socket.socket()
    sk.bind(ip_port)
    sk.listen(5)
    while True:
        print('server waiting...')
        conn, addr = sk.accept()
        data_name = str(conn.recv(1024),encoding='UTF-8')
        data_size = int(str(conn.recv(1024), encoding='utf-8'))
        conn.sendall(bytes('send', encoding='utf-8'))
        has_recv = 0
        f = open(data_name, 'ab')
        while True:
            if data_size == has_recv:
                break
            data = conn.recv(1024)
            has_recv += len(data)
            f.write(data)
            print(has_recv)
        f.close()

