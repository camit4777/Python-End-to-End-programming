import boto3
import logging
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize AWS clients
s3_client = boto3.client('s3')
lambda_client = boto3.client('lambda')

def upload_file_to_s3(bucket_name, file_path, object_name):
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        logger.info(f"File {file_path} uploaded to {bucket_name}/{object_name}")
    except Exception as e:
        logger.error(f"Error uploading file: {e}")

def invoke_lambda(function_name, payload):
    try:
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )
        result = json.loads(response['Payload'].read())
        logger.info(f"Lambda response: {result}")
        return result
    except Exception as e:
        logger.error(f"Error invoking Lambda: {e}")

if __name__ == "__main__":
    bucket = "my-demo-bucket"
    file_path = "sample.txt"
    object_name = "uploads/sample.txt"
    lambda_function = "processS3File"

    # Upload file
    upload_file_to_s3(bucket, file_path, object_name)

    # Trigger Lambda with metadata
    payload = {"bucket": bucket, "key": object_name}
    invoke_lambda(lambda_function, payload)
