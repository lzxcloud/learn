#!/usr/bin/env python3
import pika
#生产者消费者分别在两台不同的机器上
# ######################### 生产者 #########################

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.0.100'))#封装socket逻辑部分
channel = connection.channel()# 拿到一个操作句柄

channel.queue_declare(queue='hello')#创建的队列的名字

channel.basic_publish(exchange='',#交换机
                      routing_key='hello',
                      body='Hello World!')#数据
print(" [x] Sent 'Hello World!'")
connection.close()

