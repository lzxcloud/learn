#!/usr/bin/env python3
import socket
import os

class ftp_client:
    def __init__(self,ip_port):
        ip_port = tuple(ip_port)
        sk = socket.socket()
        self.sk.connect(ip_port)
        self.size = 0

    def getfileinfo(self):
        file_name = input('请输入文件路径与文件名')
        self.size = str(os.stat('p1.jpg').st_size)

    def sendfile(self):
        self.sk.sendall(bytes(self.size, encoding='utf-8'))
        ack = str(self.sk.recv(1024), encoding='utf-8')
        print(ack)
        ret_byted = self.sk.recv(1024)
        ret_str = str(ret_byted, encoding='utf-8')
        print(ret_str)

        if ack == 'send':
            with open('p1.jpg', 'rb') as f:
                for line in f:
                    self.sk.sendall(line)
            print('over')
            self.sk.close()

    def run(self,ip_port):
        self.__init__(ip_port=('172.0.0.1',10000))
        self.getfileinfo()
        self.sendfile()
    # sk.sendall(a)

    # server_reply = sk.recv(1024)

    # print(str(server_reply, encoding='UTF-8'))

    # 发送当前文件大小


fp = ftp_client()
