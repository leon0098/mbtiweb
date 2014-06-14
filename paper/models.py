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
    type = models.CharField(max_length=32)
    question = models.ForeignKey(Question)
    def __unicode__(self):
        return u'%s' % (self.content) 
    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)
        return json.dumps(d)
    
class Answer(models.Model):
    description = models.CharField(max_length=1024,null=True)
    question = models.ForeignKey(Question)
    option = models.ForeignKey(Option,unique=True)
    def __unicode__(self):
        return u'%s %s' % (self.question, self.option)
