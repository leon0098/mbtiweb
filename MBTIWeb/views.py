# coding:utf-8
'''
Created on Jun 5, 2014

@author: xiafeng
'''
import json

from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import Context
from django.template.loader import get_template

from common.jsonUtil import MyEncoder
from paper.models import Question, Option


def index(request):
    return render_to_response('index.html')

def question(request):
    question = Question.objects.filter(paper_id=1)[0]
    options = Option.objects.filter(question_id=question.id)
    return render_to_response('question.html', locals())

def jsonTest(request):
    question = Question.objects.filter(paper_id=1)[1]
    options = Option.objects.filter(question_id=question.id)
    jsonData = {}
    jsonData["question"] = MyEncoder().default(question)
    jsonData["options"] = MyEncoder().default(options)
#     return HttpResponse(json.dumps(jsonData), content_type="application/json")
#     return render_to_response('question_content.html', locals())
    t = get_template('question_content.html')  
    content_html = t.render(Context(locals()))
    jsonReturn = {'content_html': content_html,'success': True} 
    return HttpResponse(json.dumps(jsonReturn),mimetype="application/json")
    
    


