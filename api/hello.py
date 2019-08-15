from flask_restful import Resource
from flask_script import Manager

CALL_COUNT = 1


class helloworld(Resource):
    def get(self):
        global CALL_COUNT
        CALL_COUNT = CALL_COUNT + 1
        return {
                   'message': 'Hello Wrold! 呼叫次數: ' + str(CALL_COUNT)
               }, 200


# 命名不要重複取名為 'Manager' ,會有衝突
APIManager = Manager()


@APIManager.command
def reset():
    print('初始化DB內容、初始化DB資料表')
