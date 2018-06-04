import re
import json
class TokensIdentify:
    def __init__(self):
        self._emoticons_str = r"""
        (?:
            [:=;] # Eyes
            [oO\-]? # Nose (optional)
            [D\)\]\(\]/\\OpP] # Mouth
        )"""
        self._regex_str = [
        self._emoticons_str,
        r'<[^>]+>', # HTML tags
        r'(?:@[\w_]+)', # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
    
        r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
        r'(?:[\w_]+)', # other words
        r'(?:\S)' # anything else
        ]
        self._tokens_re = re.compile(r'('+'|'.join(self._regex_str)+')', re.VERBOSE | re.IGNORECASE)
        self._emoticon_re = re.compile(r'^'+self._emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

    def tokenize(self,s):
        return self._tokens_re.findall(s)

    def preprocess(self, s, lowercase=False):
        tokens = self.tokenize(s)
        if lowercase:
            tokens = [token if self._emoticon_re.search(token) else token.lower() for token in tokens]
        return tokens

    def dict_tweets(self,file):
        tweets_data = []
        tweets_file = open(file, "r")
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tweets_data.append(tweet)
            except:
                continue  
        return tweets_data
