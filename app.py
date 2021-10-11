import logging
import json
import sqs, s3
from utils import AspectRatio

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

message = sqs.receive_message()
if message:
    receipt_handle = message['ReceiptHandle']
    message_data = json.loads(message['Body'])['Records'][0]
    event_type = message_data['eventName']
    object_name = message_data['s3']['object']['key']
    logging.info("Event: {e}".format(e=event_type))
    if 'created' in event_type.lower():
        logging.info("Retrieving file {f}".format(f=object_name))
        local_path = s3.download_file(object_name)
        aspect_ratio = AspectRatio.get_aspect_ratio(local_path)
        logging.info("Image is {a} aspect ratio".format(a=aspect_ratio))
    elif 'deleted' in event_type.lower():
        pass
    else:
        logging.warn("No action defined for S3 event type {e}".format(e=event_type))
        sqs.delete_message(receipt_handle)
