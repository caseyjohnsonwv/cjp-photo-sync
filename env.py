from dotenv import load_dotenv
load_dotenv()

from os import getenv
SQS_QUEUE_URL = getenv('SQS_QUEUE_URL')
S3_ACCESS_KEY = getenv('S3_ACCESS_KEY')
S3_ACCESS_SECRET = getenv('S3_ACCESS_SECRET')
