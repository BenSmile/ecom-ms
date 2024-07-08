# notification_consumer.py

import pika
import json
import django
import os

# Configurer l'environnement Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Notification_service.settings")
django.setup()

from .models import Notification

def callback(ch, method, properties, body):
    data = json.loads(body)
    user_id = data['user_id']
    message = data['message']

    # Enregistrer la notification dans la base de données
    notification = Notification(user_id=user_id, message=message)
    notification.save()

    print(f"Saved notification: {notification}")

# Connexion à RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='notifications')

channel.basic_consume(queue='notifications', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
