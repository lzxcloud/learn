#!/usr/bin/env python3
import pika

# ########################## 消费者 ##########################

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.0.100'))
channel = connection.channel()

channel.queue_declare(queue='hello') #防止生产者没有队列而报错




def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()