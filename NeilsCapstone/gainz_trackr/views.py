from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return render(request, 'gainz_trackr/index.html')


def all_workouts(request):
    return HttpResponse("Ok!")
