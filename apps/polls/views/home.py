
from django.shortcuts import render


from apps.polls.models import *


def Home(request):    
     question=Question.objects.all().first()
     answer=Answer.objects.all().first()
     context={'question': question,'answer': answer,}
    #  context={'question': "How Are You ?",'answer': "I'm Fine!!",}
     return render(request, 'questionTemplate/questionAnswer.html',  {'context':context})