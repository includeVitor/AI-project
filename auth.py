import tweepy

class Auth:

    def __init__(self):
        self._consumer_key = ''
        self._consumer_secret = ''
        self._access_token = ''
        self._access_secret = ''
    
    def connect(self): 
        try:
            auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
            auth.set_access_token(self._access_token, self._access_secret)
            return auth
        except Exception as e:
            print(e)
