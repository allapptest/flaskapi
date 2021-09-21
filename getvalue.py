# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:10:35 2021

@author: Tharindu
"""

class getValue:
    def caller(self):
        return "hello from get Value"
    
    def getRedisValue(key='default',blogID='gama'):
        output = f"{key} and {blogID}"
        return output