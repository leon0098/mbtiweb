import json

from django.db import models


# Create your models here.
class Paper(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024,null=True)
    def __unicode__(self):
        return u'%s' % (self.name)
    
class Question(models.Model):
    serialno = models.IntegerField()
    content = models.CharField(max_length=1024)
    paper = models.ForeignKey(Paper)
    def __unicode__(self):
        return u'%s' % (self.content)   
    
class Option(models.Model):
    serialno = models.CharField(max_length=32)
    content = models.CharField(max_length=1024)
    answer_type = models.CharField(max_length=32)
    question = models.ForeignKey(Question)
    def __unicode__(self):
        return u'%s' % (self.content) 
    
class Answer(models.Model):
    description = models.CharField(max_length=1024,null=True)
    question = models.ForeignKey(Question)
    option = models.ForeignKey(Option,unique=True)
    def __unicode__(self):
        return u'%s %s' % (self.question, self.option)
    
class User_Paper(models.Model):
    user_id = models.CharField(max_length=64)
    paper = models.ForeignKey(Paper)
    serialno = models.IntegerField()
    def __unicode__(self):
        return u'%s %s' % (self.userId, self.paper)    
    
class User_Answer(models.Model):
    user_paper = models.ForeignKey(User_Paper)
    question = models.ForeignKey(Question)
    option = models.ForeignKey(Option)
    def __unicode__(self):
        return u'%s %s' % (self.question, self.option)  
    