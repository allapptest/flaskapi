# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 19:47:38 2021

@author: Bishop
"""
# setting path
import sys
sys.path.append('../modules')
# setting path
import modules.redisgetvalue as redisgetvalue
import ast
import json

obj = redisgetvalue.getValue()

class dataProcess:
    def getTemps(self,blogID="framework"):
        print(f"getTemps:{blogID}")
        return obj.getItems(blogID)
    
    def saveTemps(self,blogID='gama',items='empty'):
        return obj.putRedisValue(blogID,items)
    
    
    def itemSave(self,blogID='gama',items='empty'):
        existValue = obj.getItems(blogID)
        
        #print(type(existValue), "::::::::::::::", existValue)
        someval = json.loads(existValue.decode("utf-8")) 
        
        print(type(someval), "::::::::::::::", someval)
        print(type(items), ":::::::::::::::::::", items)
        
        mix = someval + items
        print(type(mix), ":::::::::::::::::::", mix)
        print(json.dumps(mix))
        retval = obj.getsetRedis(blogID,json.dumps(mix))
        if retval != None:
            return True
        else:
            return False
        #print('Return:',retval)
        # convertJson = json.loads(existValue)
        # print(type(convertJson), ":::::::::::::::::::", convertJson)
        
        # convertJson = json.loads(existValue)
        # print(type(convertJson), ":::::::::::::::::::", convertJson)
        # mix = convertJson + items
        # print(type(mix), ":::::::::::::::::::", mix)
        # byte_message = bytes(str(mix), 'utf-8')
        # print(type(byte_message), ":::::::::::::::::::", byte_message)
        
        
        
        # jsonString = json.loads(json.dumps(items))
        # print(type(jsonString), "::::::::::::::", jsonString)
        # mix =  json.loads(some) + jsonString
        # print(mix)
        # print(str(mix))
        # retval = obj.getsetRedis(blogID,mix)
        # print(retval)
        # print(type(val))
        # print(val)
        # print(json.loads(val), type(json.loads(val)))
        # jsonarray = json.loads(val)
        # print(jsonarray)
        # print('#############################')
        # newarray = val + items
        # print(type(newarray))
        # print('#############################')
        # retval = obj.getsetRedis(blogID,str(newarray))
        # print('#############################')
        # print(retval)
        # print('#############################')


