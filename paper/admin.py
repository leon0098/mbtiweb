from django.contrib import admin

from paper.models import Paper, Question, Answer, Option, User_Paper, \
    User_Answer, Report_Template, Report_Paragraph_Template, User_Report


# Register your models here.
admin.site.register(Paper)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Answer)
admin.site.register(User_Paper)
admin.site.register(User_Answer)
admin.site.register(Report_Template)
admin.site.register(Report_Paragraph_Template)
admin.site.register(User_Report)
