from django.http import HttpResponse
from django.shortcuts import render

from nsfw.models import Question

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'nsfw/index.html',context)
