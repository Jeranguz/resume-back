import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('cloud-resume-challenge')

def lambda_handler(event, context):
    print("Hello from GitHub Actions!")
    response = table.update_item(
        Key={
            'id': 'visitor_count'
        },
        UpdateExpression='ADD #c :val',
        ExpressionAttributeNames={
            '#c': 'count'
        },
        ExpressionAttributeValues={
            ':val': 1
        },
        ReturnValues="UPDATED_NEW"
    )
    return json.dumps({
        'statusCode': 200,
        'body': int(response['Attributes']['count']),
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,GET,PUT,PATCH'
        }
    })
