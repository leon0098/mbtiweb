'''
Created on Jun 5, 2014

@author: xiafeng
'''
from django.shortcuts import render_to_response

from paper.models import Question, Option


def index(request):
    return render_to_response('index.html')

def question(request):
    question = Question.objects.filter(paper_id=1)[0]
    options = Option.objects.filter(question_id = question.id)
    return render_to_response('question.html',locals())

# question = Question.objects.filter(paper_id=1)[0]
# print question.id
# print Option.objects.filter(question_id = question.id)