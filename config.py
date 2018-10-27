from redis import StrictRedis


class Config(object):
    """项目配置"""
    DEBUG = True

    SECRET_KEY = "5+9tcCc7h7jEYd4fCKMoKwnqxAspf+WuIKNwST5l77L10kJqEMSUF+nMiOE7jCsL"
    # 为mysql添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/info27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis 配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # session配置session数据保存的类型 是redis数据库
    SESSION_TYPE = "redis"
    # session签名开启
    SESSION_USE_SIGNER = True
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # session不是永久保存的
    SESSION_PERMANENT = False
    # 设置session的过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


class Development(Config):
    """开发环境下的配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生成环境下的配置"""
    DEBUG = False


class TestingConfig(Config):
    """单元测试环境下的配置"""
    DEBUG = True
    TESEING = True


config = {
    "development": Development,
    "production": ProductionConfig,
    "testing": TestingConfig
}