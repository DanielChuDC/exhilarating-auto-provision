# Using pyenv and cdk

```bash
pyenv virutualenv 3.11 awscdk
pyenv activate awscdk
python -m pip install aws-cdk-lib

# install  cdk
npm install -g aws-cdk
cdk init app --language python

# import necessary component
pip install aws-cdk.core aws-cdk.aws-s3 aws-cdk.aws-cloudfront aws-cdk.aws-route53 aws-cdk.aws-lambda aws-cdk.aws-logs

# get account id
aws sts get-caller-identity --query 'Account' --output text
# get region
aws ec2 describe-regions --query 'Regions[*].[RegionName]' --output table


```




