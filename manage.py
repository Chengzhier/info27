from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import app, db


manager = Manager(app)
# 將app于db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session["name"] = "baidu.com"
    return 'index'


if __name__ == '__main__':
    manager.run()


