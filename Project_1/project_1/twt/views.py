from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .Twitter_api_gateway import Twitter_api_gateway

# Create your views here.
def index(request):
    tweets = []
    account_name = None

    if request.POST:
        postData = request.POST.dict()
        account_name = postData.get('account_name')
        gateway = Twitter_api_gateway()
        tweets = gateway.get_tweets(account_name)        
    else:
        print("NOT POST")

    context = {
        'tweets': tweets,
        'account_name': account_name
    }
    return render(request, 'twt/index.html', context)
