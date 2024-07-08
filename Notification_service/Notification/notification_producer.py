# notification_producer.py

import pika
import json

def send_notification(user_id, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='notifications')

    notification = {
        'user_id': user_id,
        'message': message
    }

    channel.basic_publish(exchange='', routing_key='notifications', body=json.dumps(notification))
    print(f"Sent notification: {notification}")

    connection.close()

# Exemple d'utilisation
send_notification(1, 'This is a test notification')
