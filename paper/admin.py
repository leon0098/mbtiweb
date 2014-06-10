from django.contrib import admin

from paper.models import Paper, Question, Answer, Option


# Register your models here.
admin.site.register(Paper)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Answer)
