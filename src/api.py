import json
import boto3
import logging
import os

import dotenv

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dotenv.load_dotenv()
SQS_QUEUE_URL = os.getenv('SQS_QUEUE_URL')

sqs = boto3.resource('sqs')
queue = sqs.Queue(SQS_QUEUE_URL)


def lambda_handler(event, context):
    logger.info("lambda_handler event: {}".format(json.dumps(event)))
    try:
        queue.send_message(MessageBody=event["body"])
        logger.info("add to queue event['body']: {}".format(json.dumps(event["body"])))
        return {
            'statusCode': 200,
            'body': 'Success'
        }


    except Exception as exc:
        return {
            'statusCode': 500,
            'body': 'Failure'
        }
