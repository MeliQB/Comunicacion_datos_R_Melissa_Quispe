import boto3  # permite utilizar el SDK de AWS (interactuar con servicios de AWS --> ROute53)

# Crear un cliente de Route53
route53 = boto3.client('route53') #para interactuar con el servicio

# Configuración de la zona alojada
hosted_zone_name = 'midominio.com'
hosted_zone_comment = 'Zona alojada de mi aplicación'

# Crear la zona alojada
response = route53.create_hosted_zone(
    Name=hosted_zone_name,
    CallerReference='my-hosted-zone',
    HostedZoneConfig={
        'Comment': hosted_zone_comment,
        'PrivateZone': False
    }
)
hosted_zone_id = response['HostedZone']['Id']
print(f"Zona alojada creada: {hosted_zone_id}")

# Agregar un registro A
record_name = 'www'
record_type = 'A'
record_value = '192.0.2.1'
route53.change_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': f"{record_name}.{hosted_zone_name}",
                    'Type': record_type,
                    'TTL': 300,
                    'ResourceRecords': [
                        {
                            'Value': record_value
                        }
                    ]
                }
            }
        ]
    }
)
print(f"Registro A creado: {record_name}.{hosted_zone_name} -> {record_value}")

# Agregar un registro CNAME
cname_record_name = 'app'
cname_record_type = 'CNAME'
cname_record_value = 'www.midominio.com'
route53.change_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': f"{cname_record_name}.{hosted_zone_name}",
                    'Type': cname_record_type,
                    'TTL': 300,
                    'ResourceRecords': [
                        {
                            'Value': cname_record_value
                        }
                    ]
                }
            }
        ]
    }
)
print(f"Registro CNAME creado: {cname_record_name}.{hosted_zone_name} -> {cname_record_value}")

# Configurar balanceo de carga de tráfico basado en latencia
latency_record_name = 'api'
latency_record_type = 'A'
latency_record_values = [
    {
        'Value': '192.0.2.10',
        'Region': 'us-east-1'
    },
    {
        'Value': '192.0.2.20',
        'Region': 'us-west-1'
    }
]
route53.change_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': f"{latency_record_name}.{hosted_zone_name}",
                    'Type': latency_record_type,
                    'TTL': 60,
                    'RegionLatencyRecords': latency_record_values
                }
            }
        ]
    }
)
print(f"Registro de latencia creado: {latency_record_name}.{hosted_zone_name}")

