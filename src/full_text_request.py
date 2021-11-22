import tweepy as tp
import pandas as pd

key = 'ziiUVzU43qzWstnWHRtxZEGzD'
key_secret = 'toqDf9sRJY8orlcvbIkjzxXGuH1OZmg9KxL2gQfrPDd1wNup5o'
access_token = '1461895099181371393-LPKdxzJtA4X82FtCB6JrtKY4KSLAPp'
token_secret = 'OGsxXYA6bhGGhEPLAncBoe0Lq8B80daqKk3wvlbOBqMSe'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGDyVwEAAAAApAosMzkgGQqkiUOlYq6veTH9vhM%3DpU1svp5mleIR9Jx9iewoVve5MZVod5R1AqkkJKDzUpRg0Cgdi3'

#auth = tp.Client(bearer_token=bearer_token, consumer_key=key, consumer_secret=key_secret,access_token=access_token,access_token_secret=token_secret)
auth = tp.OAuthHandler(key, key_secret)
auth.set_access_token(access_token, token_secret)
api = tp.API(auth, wait_on_rate_limit=True)

cleaned_tw = pd.read_csv('../data/clean_tweets.csv')
texts = []
for id in cleaned_tw['id']:
    print(id)
    try:
        status = api.get_status(id, tweet_mode="extended")
    except Exception as e:
        text = ""
        texts.append(text)
        continue
    try:
        text = status.retweeted_status.full_text
    except AttributeError:  # Not a Retweet
        text = status.full_text
    texts.append(text)
cleaned_tw['full_text'] = texts
cleaned_tw = cleaned_tw.drop(columns=['text'])

cleaned_tw.to_csv('../../Eternals_Analysis_mine/data/extended_clean_tw.tsv', index = False, sep = '\t')