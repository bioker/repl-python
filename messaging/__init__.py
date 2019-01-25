import pika

def pika_conn(host, user='guest', password='guest'):
    """Creates pika BlockingConnection with passed parameters
    :param host - amqp server hostname
    :param user - username (default 'guest')
    :param password - password (default 'guest')

    :type host: str
    :type user: str
    :type password: str
    """
    credentials = pika.credentials.PlainCredentials(
            username=user,
            password=password)
    return pika.BlockingConnection(pika.ConnectionParameters(
        host=host,
        credentials=credentials))


def publish(conn, queue_name, message_body, channel=None):
    """Publish single message to queue
    :param conn - pika connection
    :param queue_name - queue name to publish
    :param message_body - message body

    :type conn: pika.adapters.BlockingConnection
    :type queue_name: str
    :type message_body: str
    :type channel: pika.adapters.blocking_connection.BlockingChannel
    """
    ch = None
    if not channel:
        ch = conn.channel()
    else:
        ch = channel
    ch.basic_publish('', queue_name, message_body)
    if not channel:
        ch.close()