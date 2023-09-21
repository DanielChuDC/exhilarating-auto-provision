""" 
Sample Lambda function which deploy the template 
and make web app in aws

 """


def handler(event, context):

    result = event["result"]
    app_name = event["ApplicationName"]
    target_environment =  event["TargetEnvironment"]
    project_type =  event["ProjectType"]
    tech_stack =  event["TechStack"]
    project_url =  event["ProjectURL"]
    access_token =  event["AccessToken"]
    private_key =  event["PrivateKey"]
    project_email =  event["ProjectEmail"]

    # start proviison if approved
    if result is "Approved":
        return { result : "provisioned"} 
    

