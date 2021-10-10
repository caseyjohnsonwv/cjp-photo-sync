from dotenv import load_dotenv
load_dotenv()

from os import getenv
AWS_ACCESS_KEY = getenv('AWS_ACCESS_KEY')
AWS_ACCESS_SECRET = getenv('AWS_ACCESS_SECRET')
SQS_QUEUE_URL = getenv('SQS_QUEUE_URL')
ALLOW_SQS_DELETE = True if str(getenv("ALLOW_SQS_DELETE")).lower() == 'true' else False
S3_BUCKET_NAME = getenv("S3_BUCKET_NAME")
