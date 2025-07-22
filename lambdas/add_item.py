import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    item = {
        'item_id': str(uuid.uuid4()),
        'name': body['name'],
        'quantity': int(body['quantity']),
        'category': body.get('category', 'general')
    }
    table.put_item(Item=item)
    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Item added', 'item': item})
    }
