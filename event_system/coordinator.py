
import pika, json, requests

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue='invitation_queue')
channel.queue_declare(queue='response_queue')
channel.queue_declare(queue='summary_queue')

responses = {}
invitation_data = {}

def invitation_callback(ch, method, properties, body):
    global invitation_data, responses
    invitation_data = json.loads(body)
    guest_list = invitation_data["guests"]
    responses = {guest: None for guest in guest_list}
    print("[Coordinator] Forwarding invitation to guests...")

    for guest in guest_list:
        queue_name = f"{guest}_queue"
        channel.queue_declare(queue=queue_name)
        channel.basic_publish(exchange='', routing_key=queue_name, body=body)

channel.basic_consume(queue='invitation_queue', on_message_callback=invitation_callback, auto_ack=True)

def response_callback(ch, method, properties, body):
    global responses
    resp = json.loads(body)
    guest = resp["guest"]
    if guest in responses:
        responses[guest] = resp["response"]
        print(f"[Coordinator] Response received from {guest}: {resp['response']}")

    if all(v is not None for v in responses.values()):
        summary = {
            "event": invitation_data["event"],
            "host": invitation_data["host"],
            "responses": responses
        }
        channel.basic_publish(exchange='', routing_key='summary_queue', body=json.dumps(summary))
        print("[Coordinator] Sent final summary to host.")
        try:
            requests.post("http://127.0.0.1:5000/summary", json=summary)
        except Exception as e:
            print("Failed to send summary to Flask API:", e)
        connection.close()

channel.basic_consume(queue='response_queue', on_message_callback=response_callback, auto_ack=True)

print("[Coordinator] Waiting for messages...")
channel.start_consuming()
