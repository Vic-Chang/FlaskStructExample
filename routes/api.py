from run import api
from api import User, hello


# API註冊路由
#api.add_resource(User.Users, '/users/')
#api.add_resource(User.User, "/user/<string:name>")
api.add_resource(hello.helloworld, "/hello/")
