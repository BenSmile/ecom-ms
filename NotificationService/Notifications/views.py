# Notifications/views.py

import pika
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Notification

def consume_message():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.RABBITMQ['HOST'])
    )
    channel = connection.channel()
    channel.queue_declare(queue=settings.RABBITMQ['QUEUE'])

    def callback(ch, method, properties, body):
        data = json.loads(body)
        Notification.objects.create(
            order_id=data['order_id'],
            message=f"New order created with ID {data['order_id']} and total amount {data['total_amount']}"
        )
        print(f" [x] Received {body}")

    channel.basic_consume(
        queue=settings.RABBITMQ['QUEUE'], on_message_callback=callback, auto_ack=True
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

@csrf_exempt
def start_consumer(request):
    if request.method == 'POST':
        consume_message()
        return JsonResponse({'status': 'Consumer started'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
