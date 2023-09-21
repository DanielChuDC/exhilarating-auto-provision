#  Reference

[Advanced Notice: Amazon S3 will automatically enable S3 Block Public Access and disable access control lists for all new buckets starting in April 2023](https://aws.amazon.com/about-aws/whats-new/2022/12/amazon-s3-automatically-enable-block-public-access-disable-access-control-lists-buckets-april-2023/)
[AWS::S3::Bucket OwnershipControls](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrols.html)



### Create the IAM role for step function 

```bash
aws cloudformation create-stack \
  --stack-name MyIAMRoleStack \
  --template-body file://iam-role-sf.yaml \
  --capabilities CAPABILITY_NAMED_IAM

# example output 

arn:aws:cloudformation:ap-southeast-1:638058664804:stack/MyIAMRoleStack/3cb262f0-57a8-11ee-a14d-062305c20852


```

### Update the iam role
```
aws cloudformation update-stack \
   --stack-name MyIAMRoleStack \
   --template-body file://iam-role-sf.yaml \
   --capabilities CAPABILITY_NAMED_IAM


```

