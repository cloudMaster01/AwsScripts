# Python script which deletes all the items in a DynamoDb table via scan and delete.

# TableName = 'deteleitems'
# Primary Key = 'no'
# Sort Key = 'name'

import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('deteleitems')

scan = table.scan()

with table.batch_writer() as batch:
    for each in scan['Items']:
        batch.delete_item(
            Key={
                'name': each['name'],
                'no': each['no']
            }
        )
