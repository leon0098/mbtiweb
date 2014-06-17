# coding:utf-8
'''
Created on Jun 5, 2014

@author: xiafeng
'''

import uuid

from django.shortcuts import render_to_response
from django.template.context import RequestContext

from common.jsonUtil import MyEncoder
from paper.models import Question, Option, User_Paper


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
    return render_to_response('question_content.html', locals())

def startExam(request):
    if "paper_id" in request.POST:
        paperId = request.POST["paper_id"]
        if not paperId:
            message = "fail"
            return render_to_response('exam.html', locals(), context_instance=RequestContext(request))
        else:
            serialNo = 1
            userId = uuid.uuid1()
            userPaper = User_Paper(paper_id=paperId,user_id=userId,serialno=serialNo)
            userPaper.save()    
            message = "success"       
            return render_to_response('exam.html', locals(), context_instance=RequestContext(request))
    
    
    


