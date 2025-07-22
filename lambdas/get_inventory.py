import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    items = table.scan().get('Items', [])
    return {
        'statusCode': 200,
        'body': json.dumps({'items': items})
    }
