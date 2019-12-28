from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    tweets = []

    if request.POST:
        postData = request.POST.dict()
        print(f"account_name: {postData.get('account_name')}")        
        tweets.append(tweet('here is one tweet'))
    else:
        print("NOT POST")

    context = {
        'tweets': tweets
    }
    return render(request, 'twt/index.html', context)

class tweet:  
    def __init__(self, text):  
        self.text = text