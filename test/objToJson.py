'''
Created on Jun 13, 2014

@author: xiafeng
'''
import json

from django.core import serializers

from paper.models import Question, Option


def convert_to_builtin_type(obj): 
    print 'default(', repr(obj), ')'
    d = {  }
    d.update(obj.__dict__)
    return d

class Object():
    name=""
    size=0
    def __init__(self,name, size):
        self.name = name
        self.size =  size

# obj= Object("123",456)
# print json.dumps(obj, default=convert_to_builtin_type)

question = Question.objects.filter(paper_id=1)[1]
# print json.dumps(question, default=convert_to_builtin_type)

options = Option.objects.filter(question_id = question.id)
# print options.toJSON
# print json.dumps(options, default=convert_to_builtin_type)

print serializers.serialize("json", question)
# print serializers.serialize("json", options)