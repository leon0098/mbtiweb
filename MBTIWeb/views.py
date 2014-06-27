# coding:utf-8
'''
Created on Jun 5, 2014

@author: xiafeng
'''

import uuid

from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from paper.models import Question, Option, User_Paper, User_Answer,Report_Template


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
    user_paper_id = request.session["user_paper_id"]
    #查询用户试卷信息
    paper = User_Paper.objects.get(id = 25)
#     answers = paper.user_answer_set.all()
    #查询用户答案基本信息
    answers = paper.user_answer_set.all()
    #查询用户答案对应的选项信息
    answers_ids = answers.values_list("option_id",flat=True)
#     answers = User_Answer.objects.filter(user_paper_id = 21)
    options = Option.objects.filter(id__in=answers_ids)
    #查询用户选项类型信息
    options_types = options.values_list("answer_type",flat=True)
    
    ENum = options.filter(answer_type="E").count()
    INum = options.filter(answer_type="I").count()
    if(ENum>=INum):
        EIType = "E"
    else:
        EIType = "I"
    if(ENum==0):
        EN = 0
        IN = 100
    elif(INum==0):
        EN = 100
        IN = 0        
    else:
        EN = round(100/(ENum+INum)*ENum)
        IN = 100-EN 
           
    SNum = options.filter(answer_type="S").count()
    NNum = options.filter(answer_type="N").count()
    if(SNum>=NNum):
        SNType = "S"
    else:
        SNType = "N"  
    if(SNum==0):
        SN = 0
        NN = 100
    elif(NNum==0):
        SN = 100
        NN = 0        
    else:
        SN = round(100/(SNum+NNum)*SNum)
        NN = 100-SN
             
    TNum = options.filter(answer_type="T").count()
    FNum = options.filter(answer_type="F").count()
    if(TNum>=FNum):
        TFType = "T"
    else:
        TFType = "F" 
    if(TNum==0):
        TN = 0
        FN = 100
    elif(FNum==0):
        TN = 100
        FN = 0        
    else:
        TN = round(100/(TNum+FNum)*TNum)
        FN = 100-TN
                    
    JNum = options.filter(answer_type="J").count()
    PNum = options.filter(answer_type="P").count()
    if(JNum>=PNum):
        JPType = "J"
    else:
        JPType = "P"
    if(JNum==0):
        JN = 0
        PN = 100
    elif(PNum==0):
        JN = 100
        PN = 0        
    else:
        JN = round(100/(JNum+PNum)*JNum)
        PN = 100-JN
                
    user_type = EIType+SNType+TFType+JPType
    print locals()
    
    #根据用户类型查询报告模板信息
    report = Report_Template.objects.get(name=user_type)
    report_paragraph = report.report_paragraph_template_set.all()
    return render_to_response('report.html', locals())