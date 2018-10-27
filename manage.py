from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask,session
from flask.ext.sqlalchemy import SQLAlchemy
#可以用来制定session的保存位置
from flask_session import Session
from flask_script import Manager

class Config(object):
    """项目配置"""
    DEBUG = True

    SECRET_KEY = "5+9tcCc7h7jEYd4fCKMoKwnqxAspf+WuIKNwST5l77L10kJqEMSUF+nMiOE7jCsL"
    # 为mysql添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/info27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #redis 配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    #session配置
    #session数据保存的类型 是redis数据库
    SESSION_TYPE = "redis"
    #session签名开启
    SESSION_USE_SIGNER = True

    SESSION_REDIS = StrictRedis(host=REDIS_PORT, port=REDIS_PORT)
    #session不是永久保存的
    SESSION_PERMANENT = False
    #设置session的过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2



app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)
#初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
#开启当前项目csrf保护，只做服务器验证功能
CSRFProtect(app)
#设置session保存指定位置
Session(app)

manger = Manager(app)


@app.route('/')
def index():
    session["name"] = "itheima"
    return 'index11'


if __name__ == '__main__':
    manger.run()


