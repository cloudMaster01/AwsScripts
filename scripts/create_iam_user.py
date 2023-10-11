# Script to create IAM user

import argparse
import boto3

def create_iam_user(user_name):
    # Initialize a Boto3 IAM client using the default AWS profile
    iam = boto3.client('iam')

    # Create the IAM user
    iam.create_user(UserName=user_name)

    print(f'IAM User "{user_name}" created successfully.')

def main():
    parser = argparse.ArgumentParser(description='Create an AWS IAM user')
    parser.add_argument('username', help='Username for the new IAM user')

    args = parser.parse_args()

    create_iam_user(args.username)

if __name__ == '__main__':
    main()
