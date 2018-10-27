from flask import session, current_app
from flask import logging
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db

# 通过制定的配置名字创建对应配置app
# create_app 就类似于工厂方法
app = create_app('development')
manager = Manager(app)
# 將app于db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    # session["name"] = "baidu.com"
    # 测试打印日志
    logging.debug("测试debug")
    logging.warning("测试warning")
    logging.error("测试error")
    logging.fatal("测试fatal")
    #根据项目应用logger 会根据应用程序的调试状态去调整日志级别
    current_app.logger.error("测试error")
    return 'index'


if __name__ == '__main__':
    manager.run()


