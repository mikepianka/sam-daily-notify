import os
import datetime
import boto3


client = boto3.client("sns")


def lambda_handler(event, context):
    # an example message
    msg = f"Current datetime: {datetime.datetime.now()}"

    # publish message to SNS topic
    response = client.publish(TopicArn=os.environ["SNS_TOPIC_ARN"], Message=msg)

    print(f"Message published with ID: {response['MessageId']} and content: {msg}")
    return response
