# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, request
from flask_restful import Resource, Api
import redisgetvalue


app = Flask(__name__)
api = Api(app)

commonObj = redisgetvalue.dataProcess()

class getTempvalues(Resource):
    def post(self):
        requestValues = request.get_json();
        print(requestValues['blogID'])
        tempItems = commonObj.getTemps(requestValues['blogID'])
        return {'temp': tempItems}
    
class putTempvalue(Resource):
    def post(self):
        requestValues = request.get_json();
        isTempSave = commonObj.saveTemps(requestValues['blogID'], requestValues['items'])
        return {'put': isTempSave}

api.add_resource(getTempvalues, '/redis/get')
api.add_resource(putTempvalue, '/redis/put')

if __name__ == '__main__':
    app.run(debug=True)





#retget.decode("utf-8")