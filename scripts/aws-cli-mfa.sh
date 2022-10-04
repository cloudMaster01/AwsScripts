#!/bin/bash
# Usage
#
# ./setup-mfa-cred.sh $PROFILE $MFA_DEVICE_ARN $TOKEN
# ./setup-mfa-cred.sh mfa arn:aws:iam::123456789012:mfa/MFA-User 123456
#
# aws s3 ls --profile mfa

PROFILE=$1
MFA_DEVICE_ARN=$2
TOKEN=$3

echo "Getting MFA credentials"
sts=$(aws sts get-session-token \
  --serial-number $MFA_DEVICE_ARN \
  --token-code $TOKEN \
  --query 'Credentials.[AccessKeyId,SecretAccessKey,SessionToken]' \
  --output text)
sts=($sts)
echo "AWS_ACCESS_KEY_ID is ${sts[0]}"
aws configure set aws_access_key_id ${sts[0]} --profile $PROFILE
aws configure set aws_secret_access_key ${sts[1]} --profile $PROFILE
aws configure set aws_session_token ${sts[2]} --profile $PROFILE
echo "MFA Credentials stored in the AWS CLI profile: $PROFILE"
