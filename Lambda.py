import json
import boto

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Prueba de GitHub Lambda!')
    }
