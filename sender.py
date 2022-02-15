try:
    import pika
except Exception as e:
    print(f'Missin module {e}')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Naber world')

print('Published message')
connection.close()