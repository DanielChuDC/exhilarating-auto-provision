import json
import boto3

sfn_client = boto3.client('stepfunctions')

def lambda_handler(event, context):
    action = event['result']
    message = { "Status": "" }
    if action == "provisioned":
        message = { "Status": "provisioned" }
    elif action == "failed":
        message = { "Status": "failed" }
    else:
        error_message = "Unrecognized action. Expected: Provisioned or failed."
        print(error_message)
        return {
            'statusCode': 400,
            'body': json.dumps(error_message)
        }

    return {
        'statusCode': 200,
        'body': f"Provision successful with {message['Status']}. Sending email!"
    }
