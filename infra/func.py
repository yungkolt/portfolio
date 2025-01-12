import json
import boto3
from decimal import Decimal

# Initialize the DynamoDB resource and table
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Ensure correct region
table = dynamodb.Table('cloud-resume-test')

# Helper function to convert Decimal to standard types
def decimal_to_standard(obj):
    if isinstance(obj, Decimal):
        return int(obj)
    raise TypeError("Object of type Decimal is not JSON serializable")

def lambda_handler(event, context):
    try:
        # Get the origin of the request
        origin = event.get('headers', {}).get('origin', '')

        # Define allowed origins
        allowed_origins = ['https://kolton.cloud', 'https://www.kolton.cloud']

        # Validate the request origin and set Access-Control-Allow-Origin
        if origin in allowed_origins:
            allow_origin = origin
        else:
            allow_origin = 'null'

        print("Fetching current viewer count...")
        # Get the current viewer count from DynamoDB
        response = table.get_item(Key={'id': '0'})
        views = decimal_to_standard(response['Item']['views']) if 'Item' in response and 'views' in response['Item'] else 0

        # Increment the viewer count
        views += 1

        # Update the viewer count in DynamoDB
        table.put_item(Item={'id': '0', 'views': views})

        # Return the updated viewer count
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': allow_origin,  # Dynamically set origin
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'views': views})
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',  # Allow all origins for errors
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'error': 'An error occurred', 'details': str(e)})
        }
