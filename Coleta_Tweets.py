# -*- coding: utf-8 -*-
import json
import sys
import time
import pymongo
import re
import string
from tweepy import Stream
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

"""consumer_Key = "rPQLXBYOnk3TbKgzX2Qe8TfJx"
consumer_Secret = "t31Pi0v4lJfMaZ4H9csEqt2uUwotiTDLC7waxHAnAWtHA3Uf3A"
access_Token = "805224390954782720-eLwQWp5C7ncpmgqUKWvZ72Y1hdgtjYE"
access_Secret = "RdSsAiXmSRh1lEMeMLX0lBUdnocH73P0aEZnuRgBWtUJ8" """

consumer_Key = "QfJBnPZnqMnitJDNloKHlUYrj"
consumer_Secret = "TMj5MrWH3RTAKsEQTJpdoMulwNoavdXBqz29jTF63EW2Dztu0y"
access_Token = "805224390954782720-GmcPxKCsdO5tiQbphzJFy9YUcwwlpeP"
access_Secret = "ACC7umWQUG50nj0cCiaJzgYiiMfepq4lcO6Coejwn8CAG"

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [emoticons_str, r'<[^>]+>',  # HTML tags
             r'(?:@[\w_]+)',  # @-mentions
             r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
             r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
             r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
             r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
             r'(?:[\w_]+)',  # other words
             r'(?:\S)']  # anything else


Words_to_Track = ['Natal','felicidade','amor','paz','alegria','árvore','família','união',
                  'champagne','luz','trenó','presentes','beijos','abraços','renas',
                  'papai noel','saco de presentes',
                  'bebedeira','festa de fim de ano','fim de ano','sexo','camisinha','suruba',
                  'ano novo', 'dinheiro']
Qtd_id = 1


tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def process(text: object, tokenizer: object = TweetTokenizer(), stopwords: object = []):
    """Process the text of a tweet:
    - Lowercase
    - Tokenize
    - Stopword removal
    - Digits removal

    Return: list of strings
    """

    text = text.lower()
    tokens = tokenizer.tokenize(text)

    # If we want to normalize contraction, uncomment this

    # tokens = normalize_contractions(tokens)

    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit()]


class StdOutListener(StreamListener):
    def on_data(self, testdata2):
        # Retrieving the details like Id, tweeted text and created at.
        global Qtd_id
        tweet = json.loads(testdata2)
        try:
            #with open("c:\\Users\\Marcelo\\Documents\\noSQL-twt.json",'a') as file:
                #file.write(testdata2)
            created_at = tweet["created_at"]
            lingua = tweet["lang"]
            dt = time.strptime(created_at,'%a %b %d %H:%M:%S +0000 %Y')
            dia = dt.tm_mday
            mes = dt.tm_mon
            ano = dt.tm_year
            hora = dt.tm_hour
            id_str = tweet['id_str']
            #text = preprocess(tweet['text'])
            tokens = process(text=tweet.get('text', ''),
                             tokenizer=tweet_tokenizer,
                             stopwords=stopword_list)
            obj = {'created_at':dt, 'id_str': id_str, 'text': tokens, 'language': lingua}
            tweetind = collection.insert_one(obj).inserted_id
            Qtd_id += 1
            print("id: %d" % Qtd_id)
            #print (hora)
            #print ("dia:%d" % dia)
            #print ("mes:%d" % mes)
            print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", dt))

            return True

        except BaseException as e:

            sys.stderr.write("Error on_data: {}\n".format(e))

            time.sleep(15)

        return True

    def on_error(self, status):
        print(status)



if __name__ == '__main__':


    tweet_tokenizer = TweetTokenizer()
    punct = list(string.punctuation)
    stopword_list = stopwords.words('portuguese') + punct + ['rt', 'via']

    # Below code  is for making connection with mongoDB
    client = pymongo.MongoClient('localhost', 27017)
    db = client.tweet_database
    print("db name = %s" % db.name)
    collection = db.tweet_mega
    print("db Collection name = %s" % db.collection)

    # This handles Twitter authetification and the connection to Twitter Streaming AP
    l = StdOutListener()
    auth = OAuthHandler(consumer_Key, consumer_Secret)
    auth.set_access_token(access_Token, access_Secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data
    stream.filter(track=Words_to_Track)