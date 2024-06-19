# send_message.py

import pika
import json

def send_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='order_notifications')

    message = {
        'order_id': 1,
        'total_amount': 100.0
    }

    channel.basic_publish(exchange='', routing_key='order_notifications', body=json.dumps(message))
    print(" [x] Sent 'Order created'")
    connection.close()

if __name__ == '__main__':
    send_message()
