# simpletwitterapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

from .models import Tweet

# Create your views here.
def index(request):
    all_tweets = Tweet.objects.all()
    print(all_tweets)
    context = {}
    context["all_tweets"] = all_tweets
    return render(request, "simpletwitterapp/index.html", context)