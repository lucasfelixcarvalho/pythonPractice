from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
import twitter

# Create your views here.
def index(request):
    tweets = []
    account_name = None

    if request.POST:
        postData = request.POST.dict()
        account_name = postData.get('account_name')
        raw_tweets = get_raw_tweets(account_name)
        tweets = get_clean_tweets(raw_tweets)
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

def get_raw_tweets(account_name):
    print(f'Searching last 5 tweets for account: {account_name}')
    api = twitter.Api(consumer_key='',
        consumer_secret='',
        access_token_key='',
        access_token_secret='')

    if api.VerifyCredentials():
        print('Credentials are valid')
    else:
        print('Invalid credentials')
        return

    results = api.GetUserTimeline(screen_name=account_name, count=2, exclude_replies=True)

    print(f'Searched. Results count: {len(results)}')
    return results

def get_clean_tweets(raw_tweets):
    tweets = []
    for row in raw_tweets:
        tweets.append(row.text)
        print(row.text)

    return tweets
