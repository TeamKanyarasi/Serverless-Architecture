import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sns = boto3.client('sns')
    sns_topic = 'arn:aws:sns:us-west-2:123456789012:MyTopic'  # replace with your SNS Topic ARN

    response = s3.list_buckets()
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        try:
            encryption = s3.get_bucket_encryption(Bucket=bucket_name)
        except Exception as e:
            if "ServerSideEncryptionConfigurationNotFoundError" in str(e):
                message = f'Bucket {bucket_name} does not have server-side encryption enabled.'
                print(message)
                sns.publish(TopicArn=sns_topic, Message=message)

    return {
        'statusCode': 200,
        'body': 'Audit completed!'
    }
