# 创建应用实例
import sys
import pymysql
from app import app
from flask_sqlalchemy import SQLAlchemy
import config

pymysql.install_as_MySQLdb()

app.config['DEBUG'] = config.DEBUG
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 设定数据库链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/flask_demo'.format(config.username, config.password,
                                                                              config.db_address)

# 初始化DB操作对象
db = SQLAlchemy(app)

# 加载配置
app.config.from_object('config')


# 启动Flask Web服务


if __name__ == '__main__':
    app.run(host=sys.argv[1], port=sys.argv[2])
    # app.run(host='localhost', port=5000)
