# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:10:35 2021

@author: Tharindu
"""

import redis 
from rq import Queue
import json

r = redis.Redis(host='172.16.16.50', port=6379, db=0)
q = Queue(connection=r)

class getValue:
    def getItems(self,blogID="framework"):
        retval = r.get(blogID)
        return retval
    
    def putRedisValue(self,blogID='gama',items='empty'):
        output = f"{blogID} and {items}"
        return output
    
    def getsetRedis(self,blogID='gama',items='empty'):
        isexist = getValue.getItems(self,blogID)
        print('>>>>>>>>:::::::', isexist)
        if isexist != None:
            retvalue = r.getset(blogID, items) # This line create to generate error 
            print('>>>>>>>>>>>>>>>>>>>>>',retvalue)
            return retvalue
        else:
            return None
        
    
