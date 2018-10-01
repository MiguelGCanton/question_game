from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
	
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Team(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	

class Answer(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return '%s - %s - %s' % (str(self.team), str(self.question), str(self.choice))
