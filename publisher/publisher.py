import pika
import time

def publish_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672,credentials=pika.PlainCredentials('user','password')))
    channel = connection.channel()

    channel.queue_declare(queue='example_queue')

    for i in range(100):
        message = f"Message {i} created at {time.time()}"
        channel.basic_publish(exchange='', routing_key='example_queue', body=message)
        print(f" [x] Sent '{message}'")
        time.sleep(4)  # Simulate delay between messages
    connection.close()

if __name__ == '__main__':
    print(' [*] Starting publisher and waiting for 5 seconds')
    time.sleep(5)
    publish_message()