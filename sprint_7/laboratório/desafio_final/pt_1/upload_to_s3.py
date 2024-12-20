import boto3
from datetime import datetime
import var_ambientes

def read_csv(file_path):
    with open(file_path, 'r', errors='ignore') as file:
        data = file.read()
    print("Arquivo lido")
    return data

def upload_to_s3(data, bucket, tipo):
    current_date = datetime.now().strftime("%Y/%m/%d")
    s3_key = f'Raw/Local/CSV/{tipo}/{current_date}/{tipo.lower()}.csv'
    print(f'Caminho:{s3_key}')

    session = boto3.Session(aws_access_key_id=acess_key,aws_secret_access_key=secret_key,aws_session_token=session_token, region_name=region_name)
    s3 = session.client("s3")
    print("Sessão criada")

    s3.put_object(Body=data, Bucket=bucket, Key=s3_key)
    print(f'Dados carregados para S3: s3://{bucket}/{s3_key}')

# Configurações AWS
acess_key = var_ambientes.acess_key
secret_key = var_ambientes.secret_key
session_token = var_ambientes.session_token
region_name = "us-east-1"
bucket = var_ambientes.bucket

# Leitura dos arquivos CSV
movies = read_csv('movies.csv')
series = read_csv('series.csv')

# Carregar dados para o S3
upload_to_s3(movies, bucket, 'Movies')
upload_to_s3(series, bucket, 'Series')