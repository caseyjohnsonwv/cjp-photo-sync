import boto3
import env

S3 = boto3.client(
    's3',
    aws_access_key_id=env.AWS_ACCESS_KEY,
    aws_secret_access_key=env.AWS_ACCESS_SECRET,
)

def download_file(object_name):
    download_location = "images/{f}".format(f=object_name)
    S3.download_file(env.S3_BUCKET_NAME, object_name, download_location)
    return download_location
