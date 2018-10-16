from django.conf.urls import url

from . import views
 
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<activity_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<activity_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<memorama_id>[0-9]+)/memorama/$', views.memorama, name='memo'),
    
    #url(r'^ajax/get_response/$', views.answer_me, name='get_response'),
    url(r'^register_team/$', views.answer_me, name='register_team'),
]