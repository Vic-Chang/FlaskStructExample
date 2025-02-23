from flask_restful import Resource, reqparse

users = [{
    'name': 'kirai',
}]


class Users(Resource):
    def get(self):
        return {
            'message': '',
            'users': users
        }


class User(Resource):
    def get(self, name):
        find = [item for item in users if item['name'] == name]
        if len(find) == 0:
            return {
                       'message': 'username not exist!'
                   }, 403
        user = find[0]
        if not user:
            return {
                       'message': 'username not exist!'
                   }, 403
        return {
            'message': '',
            'user': user
        }

    def post(self, name):
        pass

    def put(self, name):
        pass

    def delete(self, name):
        pass
