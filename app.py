import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('rekognition')
    # Este código detecta lo que hay en la foto
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = s3.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':key}})

    labels = [label['Name'] for label in response['Labels']]
    print(f"Encontrado en {key}: {labels}")

    return {
        'statusCode': 200,
        'body': json.dumps(f'Etiquetas detectadas: {labels}')
    }
