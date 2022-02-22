import boto3

def lambda_handler(event, context):
    client = boto3.client('route53')
    response = client.change_resource_record_sets(
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': 'reader2.pruebardp.com.pruebardp.com',
                        'ResourceRecords': [
                            {
                                'Value': 'ENDPOINT-LECTURA-DRP-LOSABETERRAFORM.rds.amazonaws.com',
                            },
                        ],
                        'SetIdentifier': 'drp',
                        'TTL': 5,
                        'Type': 'CNAME',
                        'Weight': 100,
                    },
                },
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': 'writer.primary.pruebardp.com',
                        'ResourceRecords': [
                            {
                                'Value': 'ENDPOINT-ESCRITURA-DRP-LOSABEAWS.rds.amazonaws.com',
                            },
                        ],
                        'TTL': 5,
                        'Type': 'CNAME',
                    },
                },
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': 'reader2.pruebardp.com',
                        'ResourceRecords': [
                            {
                                'Value': 'ENDPOINT-LECTURA-PRODUCCION.rds.amazonaws.com',
                            },
                        ],
                        'SetIdentifier': 'prod',
                        'TTL': 5,
                        'Type': 'CNAME',
                        'Weight': 0,
                    },
                },
            ],
        },
        HostedZoneId='Z091004726I0IMRMRCA77',
    )
    print(response)