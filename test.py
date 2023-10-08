import config


from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client


cos_config = CosConfig(Region='ap-nanjing', SecretId=config.SecretId, SecretKey=config.SecretKey, Token=None)
client = CosS3Client(cos_config)

response = client.list_buckets()
print(response['Buckets']['Bucket'])


