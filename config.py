import os

# 是否开启debug模式
DEBUG = True

home_dev_config = {
    'username': 'root',
    'password': 'Foriinrange10+-;',
    'db_address': 'localhost:3306',
    'SecretId': 'AKIDeDPTO9i7RitzgVJwYK1a0DIDze5d6Rlt',
    'SecretKey': '543z8DNeprhPzMUCi2GKDEG94rW6Wisv'
}

line_dev_config={
    'username':'root',
    'password':'Foriinrange10+-;',
    'db_address':'43.156.126.106:3306',
    'SecretId':'AKIDeDPTO9i7RitzgVJwYK1a0DIDze5d6Rlt',
    'SecretKey':'543z8DNeprhPzMUCi2GKDEG94rW6Wisv'
}

config={
    'username':'root',
    'password':'RZ3WHtJ4',
    'db_address':'sh-cdb-php1aito.sql.tencentcdb.com:63541',
    'SecretId':'AKIDeDPTO9i7RitzgVJwYK1a0DIDze5d6Rlt',
    'SecretKey':'543z8DNeprhPzMUCi2GKDEG94rW6Wisv'

}


now_config = config


# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", now_config['username'])
password = os.environ.get("MYSQL_PASSWORD", now_config['password'])
db_address = os.environ.get("MYSQL_ADDRESS", now_config['db_address'])
SecretId = os.environ.get("secret_id", now_config['SecretId'])
SecretKey = os.environ.get("secret_key", now_config['SecretKey'])
API_GATEWAY = os.environ.get("API_GATEWAY", '')