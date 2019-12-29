from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

# Create your views here.
def index(request):
    tweets = []
    account_name = None

    if request.POST:
        postData = request.POST.dict()
        account_name = postData.get('account_name')
        tweets.append(tweet('here is one tweet'))
    else:
        print("NOT POST")

    context = {
        'tweets': tweets,
        'account_name': account_name
    }
    return render(request, 'twt/index.html', context)

class tweet:  
    def __init__(self, text):  
        self.text = text

def get_tweets(account_name):
    print(f'Searching last 5 tweets for account: {account_name}')
