import boto3
import env

SQS = boto3.client(
    'sqs',
    aws_access_key_id=env.AWS_ACCESS_KEY,
    aws_secret_access_key=env.AWS_ACCESS_SECRET,
)

def receive_message():
    response = SQS.receive_message(
        QueueUrl=env.SQS_QUEUE_URL,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10,
    )
    try:
        message = response['Messages'][0]
    except KeyError:
        message = None
    return message

def delete_message(receipt_handle):
    if env.ALLOW_SQS_DELETE:
        SQS.delete_message(
            QueueUrl=env.SQS_QUEUE_URL,
            ReceiptHandle=receipt_handle,
        )
    else:
        logging.warn("Message deletion disabled")
