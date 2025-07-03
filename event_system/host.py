
import pika, json

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue='invitation_queue')

invitation = {
    "event": "Team Meetup",
    "host": "Alice",
    "time": "2025-07-05 17:00",
    "guests": ["guest1", "guest2", "guest3"]
}
channel.basic_publish(exchange='', routing_key='invitation_queue', body=json.dumps(invitation))
print("[Host] Invitation sent!")

def summary_callback(ch, method, properties, body):
    print("[Host] Final Guest Summary Received:\n", json.loads(body))
    connection.close()

channel.queue_declare(queue='summary_queue')
channel.basic_consume(queue='summary_queue', on_message_callback=summary_callback, auto_ack=True)
channel.start_consuming()
