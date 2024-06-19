import boto3

# Crear clientes de AWS
apigateway = boto3.client('apigateway')
lambda_client = boto3.client('lambda')

# Configuración de la API
api_name = 'my-api'
api_description = 'API para gestionar recursos'
lambda_function_name = 'my-lambda-function'
lambda_function_handler = 'lambda_function.lambda_handler'

# Crear la función de Lambda
lambda_function_code = """
def lambda_handler(event, context):
    http_method = event['httpMethod']
    resource_id = event['pathParameters']['id'] if 'id' in event['pathParameters'] else None

    if http_method == 'GET':
        if resource_id:
            # Lógica para obtener un solo recurso
            return {
                'statusCode': 200,
                'body': '{"message": "Recurso obtenido"}'
            }
        else:
            # Lógica para obtener todos los recursos
            return {
                'statusCode': 200,
                'body': '{"message": "Todos los recursos obtenidos"}'
            }
    elif http_method == 'POST':
        # Lógica para crear un nuevo recurso
        return {
            'statusCode': 201,
            'body': '{"message": "Recurso creado"}'
        }
    elif http_method == 'PUT':
        # Lógica para actualizar un recurso
        return {
            'statusCode': 200,
            'body': '{"message": "Recurso actualizado"}'
        }
    elif http_method == 'DELETE':
        # Lógica para eliminar un recurso
        return {
            'statusCode': 204,
            'body': ''
        }
    else:
        return {
            'statusCode': 400,
            'body': '{"message": "Método HTTP no válido"}'
        }
"""

lambda_function_response = lambda_client.create_function(
    FunctionName=lambda_function_name,
    Runtime='python3.9',
    Role='arn:aws:iam::123456789012:role/my-lambda-role',
    Handler=lambda_function_handler,
    Code={
        'ZipFile': lambda_function_code.encode()
    }
)

# Crear la API en API Gateway
api_response = apigateway.create_rest_api(
    name=api_name,
    description=api_description
)
api_id = api_response['id']

# Crear los recursos de la API
root_resource_id = apigateway.get_resources(restApiId=api_id)['items'][0]['id']
resource_response = apigateway.create_resource(
    restApiId=api_id,
    parentId=root_resource_id,
    pathPart='{id}'
)
resource_id = resource_response['id']

# Crear los métodos HTTP para la API
for method in ['GET', 'POST', 'PUT', 'DELETE']:
    apigateway.put_method(
        restApiId=api_id,
        resourceId=resource_id,
        httpMethod=method,
        authorizationType='NONE'
    )
    apigateway.put_method_response(
        restApiId=api_id,
        resourceId=resource_id,
        httpMethod=method,
        statusCode='200'
    )
    apigateway.put_integration(
        restApiId=api_id,
        resourceId=resource_id,
        httpMethod=method,
        type='AWS_PROXY',
        integrationHttpMethod='POST',
        uri=f'arn:aws:apigateway:{boto3.Session().region_name}:lambda:path/2015-03-31/functions/{lambda_function_response["FunctionArn"]}/invocations'
    )
    apigateway.put_integration_response(
        restApiId=api_id,
        resourceId=resource_id,
        httpMethod=method,
        statusCode='200'
    )

# Desplegar la API
stage_name = 'dev'
apigateway.create_deployment(
    restApiId=api_id,
    stageName=stage_name
)

print(f"API creada: https://{api_id}.execute-api.{boto3.Session().region_name}.amazonaws.com/{stage_name}")
