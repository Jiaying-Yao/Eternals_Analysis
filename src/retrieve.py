import pandas as pd
import tweepy as tp

key = 'ziiUVzU43qzWstnWHRtxZEGzD'
key_secret = 'toqDf9sRJY8orlcvbIkjzxXGuH1OZmg9KxL2gQfrPDd1wNup5o'
access_token = '1461895099181371393-LPKdxzJtA4X82FtCB6JrtKY4KSLAPp'
token_secret = 'OGsxXYA6bhGGhEPLAncBoe0Lq8B80daqKk3wvlbOBqMSe'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGDyVwEAAAAApAosMzkgGQqkiUOlYq6veTH9vhM%3DpU1svp5mleIR9Jx9iewoVve5MZVod5R1AqkkJKDzUpRg0Cgdi3'

#auth = tp.Client(bearer_token=bearer_token, consumer_key=key, consumer_secret=key_secret,access_token=access_token,access_token_secret=token_secret)
auth = tp.OAuthHandler(key, key_secret)
auth.set_access_token(access_token, token_secret)
api = tp.API(auth, wait_on_rate_limit=True)


#tweet_fields = ['id','lang','text']
#user_fields = ['created_at', 'username']
#place_fields = ['country']

#tweets = auth.search_recent_tweets(query='#Eternals -is:retweet', max_results=10, tweet_fields=tweet_fields, user_fields=user_fields, place_fields=place_fields)
#tweets_list = [[tweet.id, tweet.lang, tweet.text, tweet.created_at, tweet.username, tweet.country] for tweet in tweets.data]
#tweets_df = pd.DataFrame(data=tweets_list, columns=['id','language','text','created_at','author', 'country'])
#tweets = tp.Cursor(api.search_tweets, q='#Eternals -filter:retweets', lang='en', result_type='recent',until = '2021-11-19').items(800)
#tweets2 = tp.Cursor(api.search_tweets, q='#Eternals -filter:retweets', lang='en', result_type='recent',until = '2021-11-20').items(500)
tweets3 = tp.Cursor(api.search_tweets, q='#Eternals -filter:retweets', lang='en', result_type='recent').items(200)
tweets_list = [[tweet.id, tweet.text, tweet.created_at, tweet.user.name, tweet.user.location] for tweet in tweets3]
tweets_df = pd.DataFrame(data=tweets_list, columns=['id','text','created_at','author', 'location'])
tweets_df.to_csv('../data/tweets.csv', mode='a', header=False)