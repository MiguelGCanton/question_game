from django.contrib import admin

# Register your models here.

from .models import Question, Choice, Team, Answer

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Team)
admin.site.register(Answer)