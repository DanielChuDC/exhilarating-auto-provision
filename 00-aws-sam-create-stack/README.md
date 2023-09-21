### How to run this project

```bash
# use of virtualenv
pyenv activate <env>
pip install --upgrade aws-sam-cli
sam --version
# SAM CLI, version 1.97.0


[*] Create pipeline: cd automated-solution-v1 && sam pipeline init --bootstrap
[*] Validate SAM template: cd automated-solution-v1 && sam validate
[*] Test Function in the Cloud: cd automated-solution-v1 && sam sync --stack-name {stack-name} --watch


sam init
sam validate
cfn-lint template.yaml # pip install cfn-lint
sam build

sam validate # Validate SAM template: 
sam local invoke # [*] Invoke Function:
sam sync --stack-name {{stack-name}} --watch # [*] Test Function in the Cloud: 
sam deploy --guided # [*] Deploy: 


# local testing 
sam local invoke "ApprovalStageFn" 
sam local invoke "ApprovalStageFn" -e "exampl
e.json"


```