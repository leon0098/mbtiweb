#coding:utf-8
'''
Created on Jun 13, 2014

@author: xiafeng
'''
import json

from django.core.serializers import serialize, deserialize
from django.db import models
from django.db.models.query import QuerySet


#django对象转json字符串
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        #django queryset对象转json字典对象
        if isinstance(obj, QuerySet):
            return json.loads(serialize('json', obj))
        #django model对象转json字典对象
        if isinstance(obj, models.Model):
            return json.loads(serialize('json',[obj])[1:-1])
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)
    
#json字符串转django对象
def jsonBack(json):
    if json[0] == '[':
        return deserialize('json', json)
    else:
        return deserialize('json', '[' + json + ']')
    
#python对象转json字符串
def getJson(args):
    return json.dumps(args, cls=MyEncoder)
