import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    item_id = event['pathParameters']['item_id']
    body = json.loads(event['body'])
    update_expr = "SET quantity = :q"
    expr_vals = {":q": int(body['quantity'])}

    table.update_item(
        Key={'item_id': item_id},
        UpdateExpression=update_expr,
        ExpressionAttributeValues=expr_vals
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Item {item_id} updated'})
    }
