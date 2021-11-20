Terminologies:
1.  Single/Double Annotation:  
    single: The cell in the column for the sentiment analysis should contain one of positive/neutral/negative.
2.  open coding:  
    Observed data and phenomenon that are attached during qualitative data analysis.  
    Fix an topic by observing certain amount of data

Collection Step:
1. Filtered out retweets, included only english language
2. used v1.1 for calling Twitter API (Elevated)
3. Key word: #Eternals
4. Parameters for API:
    https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets
5. tweepy.Client document
    https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent  
    example:    
    https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9
6. cleaning:  
    removed https in text  
    removed duplicated cleaned text  
    removed duplicated authors  
    1500 tweets -> 1114 tweets  

Authentication:
Twitter currently does not expire tokens
2v authoriaztion uses API keys and key secret to get bearer code only. Use Client to traverse data
1.1v (Elevated) uses all keys and tokens
1.  API Key:
    ziiUVzU43qzWstnWHRtxZEGzD
    API Key Secret
    toqDf9sRJY8orlcvbIkjzxXGuH1OZmg9KxL2gQfrPDd1wNup5o
    Bearer Token:
    AAAAAAAAAAAAAAAAAAAAAGDyVwEAAAAApAosMzkgGQqkiUOlYq6veTH9vhM%3DpU1svp5mleIR9Jx9iewoVve5MZVod5R1AqkkJKDzUpRg0Cgdi3
2.  Access token: (read only permissions)
    1461895099181371393-LPKdxzJtA4X82FtCB6JrtKY4KSLAPp
    Access token secret:
    OGsxXYA6bhGGhEPLAncBoe0Lq8B80daqKk3wvlbOBqMSe