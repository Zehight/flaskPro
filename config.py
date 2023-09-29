import os

# 是否开启debug模式
DEBUG = True

cpy_dev_config={
    'username':'root',
    'password':'Foriinrnge10+-;',
    'db_address':'localhost:3306'
}

home_dev_config={
    'username':'root',
    'password':'Foriinrange10+-;',
    'db_address':'localhost:3306'
}

now_config = home_dev_config


# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", now_config['username'])
password = os.environ.get("MYSQL_PASSWORD", now_config['password'])
db_address = os.environ.get("MYSQL_ADDRESS", now_config['db_address'])
