import twitter
import json

class Twitter_api_gateway:
    def __init__(self):
        try:
            with open('twt/config.json', 'r') as f:
                self.keys = json.load(f)
        except FileNotFoundError:
            self.keys = None
            print('Could not locate file')
        except:
            self.keys = None
            print('An error has occurred')

    def __get_api(self):
        if self.keys:
            print(self.keys)
        else:
            print('Could not load keys')
            return None

        api = twitter.Api(consumer_key=self.keys['twitter_keys']['consumer_key'],
            consumer_secret=self.keys['twitter_keys']['consumer_secret'],
            access_token_key=self.keys['twitter_keys']['access_token_key'],
            access_token_secret=self.keys['twitter_keys']['access_token_secret'])

        try:
            api.VerifyCredentials()
            print('Credentials are valid')
        except:
            print('Invalid credentials')
            return None

        return api

    def __get_raw_tweets(self, account_name):
        print(f'Searching last 5 tweets for account: {account_name}')        
        api = self.__get_api()

        if not api:
            return []

        results = api.GetUserTimeline(screen_name=account_name, count=5, exclude_replies=False)

        print(f'Searched. Results count: {len(results)}')
        return results

    def get_tweets(self, account_name):
        tweets = []
        raw_tweets = self.__get_raw_tweets(account_name)

        for row in raw_tweets:
            tweets.append(row.text)
            print(row.text)

        return tweets