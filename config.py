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


now_config = line_dev_config


# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", now_config['username'])
password = os.environ.get("MYSQL_PASSWORD", now_config['password'])
db_address = os.environ.get("MYSQL_ADDRESS", now_config['db_address'])
SecretId = now_config['SecretId']
SecretKey = now_config['SecretKey']