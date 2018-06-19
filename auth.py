import tweepy

class Auth:

    def __init__(self):
        self._consumer_key = 'IY0Zy1Plve6aWj0nD4XmdbXKW'
        self._consumer_secret = 'QhBW3jXtqQpMojDeKbrFxwzrzBv5Nm4zEJZqB9ynTORfupR1Fq'
        self._access_token = '825405235887759360-GLZCnpU3Yo1j4sMBJ9ZPaWL3fryHTws'
        self._access_secret = 'EJu7dRbwrYgmxAunVHmwCAvpOBCYLhYqLdAzCdBTwVO9H'
    
    def connect(self): 
        try:
            auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
            auth.set_access_token(self._access_token, self._access_secret)
            return auth
        except Exception as e:
            print(e)
