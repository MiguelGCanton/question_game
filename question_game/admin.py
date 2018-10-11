from django.contrib import admin

# Register your models here.

from .models import Question, Choice, Team, Answer, Memorama, Game

admin.site.register(Game)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Team)
admin.site.register(Answer)
admin.site.register(Memorama)


