import pika


class RabbitHelper:
    def __init__(self):
        self.url = "amqp://qczjyzij:IVRv_qJxkk8EajfE4MFRNqNcQ3rCQOGB@sparrow.rmq.cloudamqp.com/qczjyzij"
        self.queue_name = "advertisement"
        self.connection = pika.BlockingConnection(pika.URLParameters(self.url))
        self.channel = self.connection.channel()
        self.body = None

    def insert_to_queue(self, message):
        self.channel.queue_declare(queue=self.queue_name)
        self.channel.basic_publish(exchange='', routing_key='key', body=str(message))
        print(f"{message} Sent")
        # self.connection.close()

    def read_from_queue(self):
        self.channel.queue_declare(queue=self.queue_name)

        def callback(ch, method, properties, body):
            print("Received %r" % body)
            self.body = int(body)
            # TODO return id to other class
            print("body:", self.body)

        self.channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
        print("foo:", self.body)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def get_id(self):
        return self.body


if __name__ == '__main__':
    RabbitHelper().read_from_queue()
