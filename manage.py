from flask_script import Manager, Server
from run import app
from api.hello import APIManager

# 設定你的 app
manager = Manager(app)
# 設定 python manage.py runserver 為啟動 server 指令
manager.add_command('runserver', Server())


# 設定 python manage.py shell 為啟動互動式指令 shell 的指令
@manager.shell
def make_shell_context():
    return dict(app=app)


# 透過command 管理API
manager.add_command('api', APIManager)


# 自定義command "test"
@manager.command
def test():
    print(u'test run')


if __name__ == '__main__':
    manager.run()
