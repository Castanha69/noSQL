import operator
import string
import pymongo
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk import bigrams
from collections import Counter

def process(text: object, tokenizer: object = TweetTokenizer(), stopwords: object = []):
    #Process the text of a tweet:
    #- Lowercase
    #- Tokenize
    #- Stopword removal
    #- Digits removal

    #Return: list of strings


    text = text.lower()
    tokens = tokenizer.tokenize(text)

    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit()]


if __name__ == '__main__':

    tweet_tokenizer = TweetTokenizer()
    punct = list(string.punctuation)
    stopword_list = stopwords.words('portuguese') + punct + ['rt', 'via']

    client = pymongo.MongoClient('localhost', 27017)
    db = client.tweet_database
    collection = db.tweet_collection

    count_all = Counter()


    tweets_iterator = collection.find()
    for tweet in tweets_iterator:
        # Create a list with all the terms

        tokens = process(text=tweet.get('text', ''),
                         tokenizer=tweet_tokenizer,
                         stopwords=stopword_list)

        terms_all = [term for term in tokens]
        terms_bigram = bigrams(terms_all)
        # Update the counter
        count_all.update(terms_bigram)


    print(count_all.most_common(300))
