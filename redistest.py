# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, request
from flask_restful import Resource, Api
import getvalue
import redis 
from rq import Queue


obj = getvalue.getValue().caller()

app = Flask(__name__)
api = Api(app)

r = redis.Redis(host='localhost', port=6379, db=0)
val = r.set('foo', 'bar')
print(val)
q = Queue(connection=r)

def rediscall(n):
    print("Task running")
    
    
class HelloWorld(Resource):
    def get(self):
        someval=r.get('foo')
        sendto=f"redis: {someval} and {obj}"
        return {'hello': sendto}
    
class redispost(Resource):
    def post(self):
        some_json = request.get_json();
        print(some_json['key'])
        retset = r.set(some_json['key'], some_json['blogID'])
        someval=r.get('foo')
        sendto=f"redis: {someval} and {obj} and set - {retset}"
        return {'hello': sendto}
    
class redisget(Resource):
    def post(self):
        some_json = request.get_json();
        print(some_json['key'])
        retget = r.get(some_json['key'])
        print(retget.decode("utf-8") )
        return {'value': retget.decode("utf-8") }

api.add_resource(HelloWorld, '/')
api.add_resource(redispost, '/redis/set')
api.add_resource(redisget, '/redis/get')

if __name__ == '__main__':
    app.run(debug=True)
