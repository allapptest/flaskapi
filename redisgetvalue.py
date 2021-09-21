# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:10:35 2021

@author: Tharindu
"""

import redis 
from rq import Queue

r = redis.Redis(host='localhost', port=6379, db=0)
q = Queue(connection=r)

class getValue:
    def getItems(self,blogID="framework"):
        return blogID
    
    def putRedisValue(blogID='gama',items='empty'):
        output = f"{blogID} and {items}"
        return output
    
class dataProcess:
    def getTemps(self,blogID="framework"):
        print(f"getTemps:{blogID}")
        return getValue.getItems(self,blogID)
    
    def saveTemps(self,blogID='gama',items='empty'):
        return getValue.putRedisValue(blogID,items)