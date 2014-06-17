# coding:utf-8
'''
Created on Jun 5, 2014

@author: xiafeng
'''

import uuid

from django.http.response import HttpResponse
from django.shortcuts import render_to_response

from paper.models import Question, Option, User_Paper, User_Answer


def index(request):
    return render_to_response('index.html')

def question(request):
    if "paper_id" in request.GET and request.GET["paper_id"]:
        if "qno" in request.GET and request.GET["qno"]:
            qno = request.GET["qno"]
            qno = int(qno)+1
        else:
            qno = 0
        if "user_paper_id" in request.GET and request.GET["user_paper_id"]:
            user_paper_id = request.GET["user_paper_id"]
            
        paper_id = request.GET["paper_id"]
        totalNum = len(Question.objects.all())
        #用户回答完所有试题时
        if qno == totalNum:      
            return render_to_response('report.html', locals())
        
        question = Question.objects.filter(paper_id=paper_id)[int(qno)]
        options = Option.objects.filter(question_id=question.id)
        #显示第一道问题时
        if qno == 0:
            return render_to_response('question.html', locals())
        #显示下一道试题
        else:
            return render_to_response('question_content.html', locals())

def startExam(request):
    if "paper_id" in request.POST:
        paperId = request.POST["paper_id"]
        if not paperId:
            message = "fail"
            return HttpResponse(message)
        else:
            serialNo = 1
            userId = uuid.uuid1()
            userPaper = User_Paper(paper_id=paperId,user_id=userId,serialno=serialNo)
            userPaper.save()
            message = "success"       
            return HttpResponse(userPaper.id)
    
def saveAnswer(request):
    if "user_paper_id" in request.POST and request.POST["user_paper_id"] and "question_id" in request.POST and request.POST["question_id"] and "option_id" in request.POST and request.POST["option_id"]:
        user_paper_id = request.POST["user_paper_id"]
        question_id = request.POST["question_id"]
        option_id = request.POST["option_id"]
        userAnswer = User_Answer(user_paper_id=user_paper_id,question_id=question_id,option_id=option_id)
        userAnswer.save()
        message = "success"       
        return HttpResponse(message)    
    


