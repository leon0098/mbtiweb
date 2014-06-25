#coding:utf-8
#使本文件能写中文

from django.db import models


#试卷基本信息
class Paper(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024,null=True)
    def __unicode__(self):
        return u'%s' % (self.name)
    
#题目信息    
class Question(models.Model):
    serialno = models.IntegerField()
    content = models.CharField(max_length=1024)
    paper = models.ForeignKey(Paper)
    def __unicode__(self):
        return u'%s' % (self.content) 
      
#题目选项信息       
class Option(models.Model):
    serialno = models.CharField(max_length=32)
    content = models.CharField(max_length=1024)
    answer_type = models.CharField(max_length=32)
    question = models.ForeignKey(Question)
    def __unicode__(self):
        return u'%s' % (self.content)
     
#题目答案信息       
class Answer(models.Model):
    description = models.CharField(max_length=1024,null=True)
    question = models.ForeignKey(Question)
    option = models.ForeignKey(Option,unique=True)
    def __unicode__(self):
        return u'%s %s' % (self.question, self.option)

#用户测试信息      
class User_Paper(models.Model):
    user_id = models.CharField(max_length=64)
    paper = models.ForeignKey(Paper)
    serialno = models.IntegerField()
    def __unicode__(self):
        return u'%s %s' % (self.userId, self.paper)    
    
#用户测试答案信息       
class User_Answer(models.Model):
    user_paper = models.ForeignKey(User_Paper)
    question = models.ForeignKey(Question)
    option = models.ForeignKey(Option)
    def __unicode__(self):
        return u'%s %s' % (self.question, self.option) 
     
#报告模板信息    
class Report_Template(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    def __unicode__(self):
        return u'%s %s' % (self.name, self.description) 
    
#报告模板段落信息  
class Report_Paragraph_Template(models.Model):
    report_template = models.ForeignKey(Report_Template)
    serialno = models.IntegerField()
    title = models.CharField(max_length=128)
    content = models.TextField()
    def __unicode__(self):
        return u'%s %s' % (self.serialno, self.title) 

#用户报告信息              
class User_Report(models.Model):
    user_paper = models.ForeignKey(User_Paper)
    report_template = models.ForeignKey(Report_Template)
    def __unicode__(self):
        return u'%s %s' % (self.user_paper, self.report_template)     
    
   
    