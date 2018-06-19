import tweepy
import operator
from nltk.tokenize import word_tokenize
import re
import json
import jsonlines
from auth import Auth
from dataCollector import DataCollector
from tokenizeIdentify import TokensIdentify
from collections import Counter
from nltk.corpus import stopwords
import string
import vincent
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

def app():
    #tokenize = []
    auth = Auth()
    auth = auth.connect()
    streaming_data = DataCollector()
    streaming_data = tweepy.Stream(auth, DataCollector())
    streaming_data.filter(track=['#python'])
    #tokenize = []
    #tokens = TokensIdentify()
    #tokenize = tokens.dict_tweets('data-ciro.jsonl')
    #count_all = Counter()

   # punctuation = list(string.punctuation)
    #punctuation = list(string.punctuation)
   # stop = stopwords.words('portuguese') + punctuation + ['rt', 'via', 'Ciro','RT','...','Gomes','O','ção',"...","disse","ão","é", "á", "ciro","Não"]

           
  #  positive_vocab = [ 'impressionante', 'excepcional', 'fantástico', 'formidável', 'Boa', 'bom', 'ótimo', ':)' ]
   # negative_vocab = [ 'mau', 'terrivel','inútil', 'ódio', ':(' ]
    #neutral_vocab = [ 'filme','o','som','estava','é','atores','fez','sabe','palavras','não' ]

    #def word_feats(sentence):
     #   return dict([(s, True) for s in sentence])
 
#    positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
 #   negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
  #  neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

  #  train_set = negative_features + positive_features + neutral_features

   # classifier = NaiveBayesClassifier.train(train_set)


    #neg = 0 
    #pos = 0
    #sentence = []
    ##for t in tokenize:
       # sentence = tokens.preprocess(t['text'])
        #for s in sentence:
           # classResult = classifier.classify( word_feats(s))
           # if classResult == 'neg':
           #     neg = neg + 1
           # if classResult == 'pos':
           #     pos = pos + 1



    #    terms_stop = [term for term in tokens.preprocess(t['text']) if term not in stop]
    #    count_all.update(terms_stop)
   #     neg = 0
   #     pos = 0
   # for word in words:
   #     
 #  
   # t = pos + neg 
   # print('Positive: ' + str(float(pos)/t*100))
 #   print('Negative: ' + str(float(neg)/t*100))
    

    #word_freq = [['Positivo', 90.82],['Negativo',9.18]]
    #labels, freq = zip(*word_freq)
    #data = {'data': freq, 'x': labels}
    #bar = vincent.Bar(data, iter_idx='x')
    #bar.to_json('term_freq-ciro-sentiments.json')



    #print(tweets_data[1]["text"])  
    #data1 = json.loads(data[1])

   # print(data1["text"])
    #identify_tokens = TokensIdentify()
  #  print(identify_tokens.preprocess(["text"]))
    #with open('data.jsonl', 'r') as f:
        #for line in f:
            #tweet = json.loads(line)
            #tokens = preprocess(tweet['text'])
            #print(tokens)
if __name__ == '__main__':
    app()