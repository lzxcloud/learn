#!/usr/bin/env python3
import socket
#导入select模块
import select


sk = socket.socket()
sk.bind(('127.0.0.1', 9999,))
sk.listen()

sk2 = socket.socket()
sk2.bind(('127.0.0.1', 10000))
sk2.listen()

sk3 = socket.socket()
sk3.bind(('127.0.0.1', 10001))
sk3.listen()

inputs = [sk, sk2, sk3]

while True:
    r_list, w_list, e_list = select.select(inputs,[], [], 1)
    #select 内部自动监听socket对象,一旦socket变化感知到
    #等待1s 检测系统有没有变化 超时pass  这个时间是最多等待的时间
    #[sk,sk2],内部自动监听这两个对象 一旦某个句柄发生变化(sk.accpet)  ===》 r——list
    #如果有inputs 里面有发生错误了 ==》e_list
    #如果有人来连接sk1   r_list = [sk1]
    #第二个[] 里面有啥就会交个 w_list   如 [sk1,sk3]   ===   w_list = [sk1,sk3]
    for sk in r_list:
        conn, addr = sk.accept()
        conn.sendall(bytes('hello', encoding='utf-8'))
        conn.close()


    data_bytes = sk.recv(1024)
    data_str = str(data_bytes,encoding='utf-8')

   #  #移除出错的
   #  for sk in e_list:
   #      inputs.remove(sk)
   #