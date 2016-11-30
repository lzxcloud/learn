#!/usr/bin/env python3
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        # print self.request,self.client_address,self.server
        # conn == self.request
        conn = self.request
        conn.sendall(bytes('欢迎致电 10086，请输入1xxx,0转人工服务.', encoding='utf-8'))
        Flag = True
        while Flag:
            data = str(conn.recv(1024), encoding='utf-8')

            if data == 'exit':
                Flag = False
                break
            elif data == '0':
                conn.sendall(bytes('通话可能会被录音.balabala一大推',encoding='utf-8'))
            else:
                conn.sendall(bytes('请重新输入.',encoding='utf-8'))
if __name__ == '__main__':
    #内部创建了一个socket.socket()  bind
    # Threading 创建一个进程
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    #其实就是一个循环等待用户连接  可以帮助处理并发连接
    server.serve_forever()
