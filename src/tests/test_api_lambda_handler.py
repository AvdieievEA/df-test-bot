import json
import os
from unittest import TestCase

import boto3
import dotenv
import requests

from tests.test_data import TEST_API_BODY

"""
Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test. 
"""


class TestApiGateway(TestCase):
    api_endpoint: str

    @classmethod
    def get_stack_name(cls) -> str:
        dotenv.load_dotenv()
        stack_name = os.environ.get("AWS_SAM_STACK_NAME")
        print(stack_name)
        if not stack_name:
            raise Exception(
                "Cannot find env var AWS_SAM_STACK_NAME. \n"
                "Please setup this environment variable with the stack name where we are running integration tests."
            )

        return stack_name

    def setUp(self) -> None:
        """
        Based on the provided env variable AWS_SAM_STACK_NAME,
        here we use cloudformation API to find out what the Api URL is
        """
        stack_name = TestApiGateway.get_stack_name()

        client = boto3.client("cloudformation")

        try:
            response = client.describe_stacks(StackName=stack_name)
        except Exception as e:
            self.api_endpoint = os.environ.get("STACK_URL")
            return
            # raise Exception(
            #     f"Cannot find stack {stack_name}. \n" f'Please make sure stack with the name "{stack_name}" exists.'
            # ) from e

        stacks = response["Stacks"]

        stack_outputs = stacks[0]["Outputs"]
        api_outputs = [output for output in stack_outputs if output["OutputKey"] == "TelegramApi"]
        self.assertTrue(api_outputs, f"Cannot find output TelegramApi in stack {stack_name}")

        self.api_endpoint = api_outputs[0]["OutputValue"]

    def test_api_gateway(self):
        """
        Call the API Gateway endpoint and check the response
        """

        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.api_endpoint, data=json.dumps(TEST_API_BODY), headers=headers)
        self.assertEqual(response.text, 'Success')
