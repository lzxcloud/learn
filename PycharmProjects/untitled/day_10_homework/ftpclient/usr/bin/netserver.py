#!/usr/bin/env python3
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        # print self.request,self.client_address,self.server
        # conn == self.request
        conn = self.request
        conn.sendall('欢迎使用ftp')
        Flag = True


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()
