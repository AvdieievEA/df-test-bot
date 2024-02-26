import boto3
import pytest
from sqs import lambda_handler
from tests.test_data import TEST_SQS_DATA


@pytest.fixture
def lambda_event():

    return TEST_SQS_DATA


def test_lambda_function(lambda_event):
    result = lambda_handler(lambda_event, None)
    assert result == 'ok'
