from boto3 import client
import json

"""
This function simulates a human approving/rejecting a creation of stack of resource in AWS

"""

sfn_client = client("stepfunctions")


def handler(event, context):

    # for rec in event["Records"]:

    #     msg = json.loads(rec["body"])

    #     _token = msg["TaskToken"]

    #     print(f"Sending Step Functions Success for: ${_token}")
    #     # send status to state
    #     sfn_client.send_task_success(taskToken=_token, output='"approved"')
    # _token = msg["TaskToken"]
    # print(f"Sending Step Functions Success for: ${_token}")
    return {"result": "Approved"}