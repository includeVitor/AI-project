from tweepy import Stream
from tweepy.streaming import StreamListener


class DataCollector(StreamListener):

    def on_data(self, data):
        try:
            with open('data-class.jsonl', 'a') as f:
                f.write(data)
                return True
        except Exception as e:
            print(e)
        return True

    def on_error(self, status):
        print(status)
        return True
        

