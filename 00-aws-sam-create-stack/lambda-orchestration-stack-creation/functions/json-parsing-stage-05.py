def handler(event, context):
    # Example JSON content
    json_content = {
        "Name of the application": "MyApp",
        "The target environment": "Production",
        "The target project type": "Dynamic",
        "Techstack": "Node.js",
        "Project URL": "github.com/myapp",
        "Project access token": "abc123",
        "Project private key": "xyz456",
        "Project email": "xxx@gmail.com"
    }

    try:
        # Parsing the JSON content
        parsed_data = parse_json(json_content)
        print(parsed_data)

        # You can perform further actions or processing based on the parsed data
        return "parsed with name"
    except Exception as e:
        return {"error": str(e)}

def parse_json(json_content):
    try:
        # Extracting information from the JSON data
        app_name = json_content.get("Name of the application", "")
        target_environment = json_content.get("The target environment", "")
        project_type = json_content.get("The target project type", "")
        tech_stack = json_content.get("Techstack", "") if project_type != "Static" else ""
        project_url = json_content.get("Project URL", "")
        access_token = json_content.get("Project access token", "")
        private_key = json_content.get("Project private key", "")
        project_email = json_content.get("Project email", "")

        # You can do further processing or validation here

        return {
            "ApplicationName": app_name,
            "TargetEnvironment": target_environment,
            "ProjectType": project_type,
            "TechStack": tech_stack,
            "ProjectURL": project_url,
            "AccessToken": access_token,
            "PrivateKey": private_key,
            "ProjectEmail": project_email,
        }
    except Exception as e:
        return {"error": str(e)}
