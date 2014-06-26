# coding:utf-8
'''
Created on Jun 5, 2014

@author: xiafeng
'''

import uuid

from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from paper.models import Question, Option, User_Paper, User_Answer


def index(request):
    return render_to_response('index.html')

#生成用户测试结果的基本信息
def startExam(request):
    if "paper_id" in request.POST:
        paper_id = request.POST["paper_id"]
        if not paper_id:
            message = "fail"
            return HttpResponse(message)
        else:
            serialNo = 1
            userId = uuid.uuid1()
            userPaper = User_Paper(paper_id=paper_id,user_id=userId,serialno=serialNo)
            userPaper.save()
            message = "success"
            #存入session
            request.session["user_paper_id"] = userPaper.id  
            request.session["paper_id"] = paper_id 
            return HttpResponse(message)

#显示试题信息        
def question(request):
    paper_id = request.session["paper_id"]
    if "qno" in request.GET and request.GET["qno"]:
        qno = request.GET["qno"]
        qno = int(qno)+1
    else:
        qno = 0
    
    question = Question.objects.filter(paper_id=paper_id)[int(qno)]
    options = Option.objects.filter(question_id=question.id)
    #显示第一道问题时
    if qno == 0:
        #查询试题总数并存入session
        totalNum = len(Question.objects.all())
        request.session["totalNum"] = totalNum  
        return render_to_response('question.html', locals(), RequestContext(request))
    #显示下一道试题
    else:
        return render_to_response('question_content.html', locals())

#保存用户答案    
def saveAnswer(request):
    user_paper_id = request.session["user_paper_id"]
    if "question_id" in request.POST and request.POST["question_id"] and "option_id" in request.POST and request.POST["option_id"]:
        question_id = request.POST["question_id"]
        option_id = request.POST["option_id"]
        userAnswer = User_Answer(user_paper_id=user_paper_id,question_id=question_id,option_id=option_id)
        userAnswer.save()
        message = "success"       
        return HttpResponse(message)    

#生成用户报告
def report(request):
#     user_paper_id = request.session["user_paper_id"]
#     answers = User_Answer.objects.filter(user_paper_id=user_paper_id)
    #查询用户试卷信息
    paper = User_Paper.objects.get(id = 21)
    print paper
#     answers = paper.user_answer_set.all()
    #查询用户答案基本信息
    answers = paper.user_answer_set.all()
    print answers
    #查询用户答案对应的选项信息
    answers_ids = answers.values_list("option_id",flat=True)
    print answers_ids
#     answers = User_Answer.objects.filter(user_paper_id = 21)
    options = Option.objects.filter(id__in=answers_ids)
    print options
    #查询用户选项类型信息
    options_types = options.values_list("answer_type",flat=True)
    print options_types
    
    ENum = options.filter(answer_type="E").count()
    print ENum
    INum = options.filter(answer_type="I").count()
    print INum
    if(ENum>=INum):
        EIType = "E"
    else:
        EIType = "I"   
        
    SNum = options.filter(answer_type="S").count()
    print SNum
    NNum = options.filter(answer_type="N").count()
    print NNum
    if(SNum>=NNum):
        SNType = "S"
    else:
        SNType = "N"  
         
    TNum = options.filter(answer_type="T").count()
    print TNum
    FNum = options.filter(answer_type="F").count()
    print FNum
    if(TNum>=FNum):
        TFType = "T"
    else:
        TFType = "F" 
            
    JNum = options.filter(answer_type="J").count()
    print JNum
    PNum = options.filter(answer_type="P").count()
    print PNum   
    if(JNum>=PNum):
        JPType = "J"
    else:
        JPType = "P"
        
    user_type = EIType+SNType+TFType+JPType
    print user_type
