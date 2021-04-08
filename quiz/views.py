from django.shortcuts import render,redirect,HttpResponse,Http404
from .models import *

# Create your views here.

def home(request):
    questions = Questions.objects.all()
    return render(request,"index.html",{"questions":questions})

def saveresponse(request):
    if(request.method=="POST"):
        name = request.POST["name"]
        questions = Questions.objects.all()
        for i in questions:
            answer = request.POST[str(i.id)]
            Responses.objects.create(name=name,question_id=i.id,response = answer)
        return HttpResponse("Your response has been submitted")
    else:
        raise Http404
