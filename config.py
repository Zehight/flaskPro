import os

# 是否开启debug模式
DEBUG = True

# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", 'root')
password = os.environ.get("MYSQL_PASSWORD", 'Foriinrange10+-;')
db_address = os.environ.get("MYSQL_ADDRESS", 'localhost:3306')
