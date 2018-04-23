from tweepy import Stream
from tweepy.streaming import StreamListener

class Colletor(StreamListener):
    
    def __init__(self):
        print('Coletando dados')
                             
    def getData(self, data):
        try:
            with open('tweets.json', 'a') as f:
                f.write(data)
        except Exception as e:
            print("Erro nos dados: {0}".format(e))
 
