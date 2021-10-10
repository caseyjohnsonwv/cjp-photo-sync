import logging
import sqs

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

message = sqs.receive_message()
logging.info("Message received: {}".format(message is not None))

if message:
    receipt_handle = message['ReceiptHandle']
    body = message['Body']
