import pika
import time

def callback(ch, method, properties, body):
    print(f" [x] Received '{body}'")
    time.sleep(2)

def start_subscriber():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672,credentials=pika.PlainCredentials('user','password')))
    channel = connection.channel()

    channel.queue_declare(queue='example_queue')

    channel.basic_consume(queue='example_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    print(' [*] Starting subscriber and waiting for 5 seconds')
    time.sleep(5)
    start_subscriber()