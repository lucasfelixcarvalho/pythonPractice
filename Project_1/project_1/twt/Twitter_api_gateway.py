import twitter
import json

class Twitter_api_gateway:
    def __init__(self):
        try:
            with open('twt/coonfig.json', 'r') as f:
                self.keys = json.load(f)
        except FileNotFoundError:
            self.keys = None
            print('Could not locate file')
        except:
            self.keys = None
            print('An error has occurred')


    def get_api(self):
        if self.keys:
            print(self.keys)
        else:
            print('Could not load keys')
            return None

        api = twitter.Api(consumer_key=self.keys['twitter_keys']['consumer_key'],
            consumer_secret=self.keys['twitter_keys']['consumer_secret'],
            access_token_key=self.keys['twitter_keys']['access_token_key'],
            access_token_secret=self.keys['twitter_keys']['access_token_secret'])

        if api.VerifyCredentials():
            print('Credentials are valid')
            return api
        else:
            print('Invalid credentials')
            return None
