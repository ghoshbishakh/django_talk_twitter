# simpletwitterapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Tweet

# Create your views here.
def index(request):
    if request.method == "POST":
        print(request.POST)
        new_tweet = Tweet()
        new_tweet.username = request.POST["userinput"]
        new_tweet.content = request.POST["tweetinput"]
        new_tweet.save()

    all_tweets = Tweet.objects.all().order_by('-datetime')
    print(all_tweets) # for sanity check.
    context = {}
    context["all_tweets"] = all_tweets
    return render(request, "simpletwitterapp/index.html", context)

def apipage(request):
    all_tweets = Tweet.objects.all().order_by('-datetime')
    print(all_tweets) # for sanity check.
    context = {}
    context["all_tweets"] = all_tweets
    return render(request, "simpletwitterapp/apipage.html", context)


def api(request):
    all_tweets = list(Tweet.objects.all().order_by('-datetime'))
    tweet = {"username": all_tweets[0].username,
    "content": all_tweets[0].content,
    "datetime": all_tweets[0].datetime}
    return JsonResponse(tweet)