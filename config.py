import os

# 是否开启debug模式
DEBUG = True

# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", 'root')
password = os.environ.get("MYSQL_PASSWORD", 'Mccbts_Liubin123')
db_address = os.environ.get("MYSQL_ADDRESS", '192.168.51.24:3306')