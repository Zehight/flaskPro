import os

dev_config={
    'username':'root',
    'password':'RZ3WHtJ4',
    'db_address':'sh-cdb-php1aito.sql.tencentcdb.com:63541',
    'SecretId':'AKIDeDPTO9i7RitzgVJwYK1a0DIDze5d6Rlt',
    'SecretKey':'543z8DNeprhPzMUCi2GKDEG94rW6Wisv',
    'data_base' :'flask_demo'
}

now_config = dev_config

# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", now_config['username'])
password = os.environ.get("MYSQL_PASSWORD", now_config['password'])
db_address = os.environ.get("MYSQL_ADDRESS", now_config['db_address'])
data_base = os.environ.get("DATA_BASE", now_config['data_base'])
API_GATEWAY = os.environ.get("API_GATEWAY", '')
SecretId = os.environ.get("secret_id", now_config['SecretId'])
SecretKey = os.environ.get("secret_key", now_config['SecretKey'])

