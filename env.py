from dotenv import load_dotenv
load_dotenv()

from os import getenv
SQS_QUEUE_URL = getenv('SQS_QUEUE_URL')
AWS_ACCESS_KEY = getenv('AWS_ACCESS_KEY')
AWS_ACCESS_SECRET = getenv('AWS_ACCESS_SECRET')
ALLOW_SQS_DELETE = True if str(getenv("ALLOW_SQS_DELETE")).lower() == 'true' else False
