
import pika, json, sys, random

guest_name = sys.argv[1]
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
queue_name = f"{guest_name}_queue"
channel.queue_declare(queue=queue_name)

def decide_response():
    return random.choice(["Yes", "No", "Maybe"])

def on_invitation(ch, method, properties, body):
    invitation = json.loads(body)
    print(f"[{guest_name}] Received invitation for {invitation['event']} from {invitation['host']}")
    response = {
        "guest": guest_name,
        "response": decide_response()
    }
    channel.basic_publish(exchange='', routing_key='response_queue', body=json.dumps(response))
    print(f"[{guest_name}] Sent response: {response['response']}")
    connection.close()

channel.basic_consume(queue=queue_name, on_message_callback=on_invitation, auto_ack=True)
print(f"[{guest_name}] Waiting for invitations...")
channel.start_consuming()
