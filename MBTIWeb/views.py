'''
Created on Jun 5, 2014

@author: xiafeng
'''
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html')

def question(request):
    return render_to_response('question.html')