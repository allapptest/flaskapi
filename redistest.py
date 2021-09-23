# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, request
from flask_restful import Resource, Api
#import modules.redisgetvalue as redisgetvalue
import proc.redisproc as redisproc
import json


app = Flask(__name__)
api = Api(app)

commonObj = redisproc.dataProcess()

class getTempvalues(Resource):
    def post(self):
        requestValues = request.get_json();
        print(requestValues['blogID'])
        tempItems = commonObj.getTemps(requestValues['blogID'])
        return {'temp': tempItems}
    
class putTempvalue(Resource):
    def post(self):
        requestValues = request.get_json();
        # print(type(requestValues), "############################", requestValues);
        json_object = json.dumps(requestValues['items'], indent = 4) 
        # print(type(json_object), "############################", json_object);
        
        #print(json_object)
        # print(type(requestValues['items']), "############################", requestValues['items'])
        tester = commonObj.itemSave(requestValues['blogID'], requestValues['items'])
        if tester == True:
            return {'Status': 201, 'Message': 'Value inserted'}
        else:
            return {'Status': 500, 'Message': 'Error'}
        
        # isTempSave = commonObj.saveTemps(requestValues['blogID'], requestValues['items'])
        
        # return {'put': isTempSave}
        

api.add_resource(getTempvalues, '/redis/get')
api.add_resource(putTempvalue, '/redis/put')

if __name__ == '__main__':
    app.run(debug=True)





#retget.decode("utf-8")