#Sample code to test pipeline

# Load libraries
import boto3
import pandas as pd

s3client = boto3.client(
    's3',
    aws_access_key_id = 'mlops',
    aws_secret_access_key = 'mlops123',
    endpoint_url="http://192.168.1.67:9000"
)

obj = s3client.get_object(
    Bucket = 'test-clean',
    Key = '8013472447257'
)

def getData():
    data = pd.read_csv(obj['Body'])
    print(data)

getData()
