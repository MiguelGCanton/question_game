from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Game, Question, Memorama
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .forms import Team_form

def index(request):
    game_list = Game.objects.all()
    template = loader.get_template('question_game/index.html')
    context = {
        'game_list': game_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, game_id):
    game = get_object_or_404(game, pk=game_id)
    question_list = Question.objects.filter(game=game_id)
    
    return render(request, 'question_game/detail.html', {'game': game
    	, 'question_list':  question_list})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def memorama(request, memorama_id):
    memorama = get_object_or_404(Memorama, pk=memorama_id)
    question_list = memorama.question_set.all()
    return render(request, 'question_game/memorama.html', {'question_list':question_list})


def answer_me(request):
    form = Team_form()
    return render(request, 'question_game/register_team.html', {'form': form} )
