#API Key: GqlfdaQUbr5Ic9GLW2hiFUVD3
#API Secret: vQxEJ46vPh9BVinz02yB6fEXCvwrZXSqxxmdoMzmwo9WihDgh4
#Access token: 827998835569999876-g2v5tnrhuz0ab4uvdbhOFUh8pQZt7qo
#Access token secret: 49NpU9CefbcThL9y0Gw7XBWwUaxmqU7DDaeaO5zv75YAu

import tweepy

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '827998835569999876-g2v5tnrhuz0ab4uvdbhOFUh8pQZt7qo'
ACCESS_SECRET = '49NpU9CefbcThL9y0Gw7XBWwUaxmqU7DDaeaO5zv75YAu'
CONSUMER_KEY = 'GqlfdaQUbr5Ic9GLW2hiFUVD3'
CONSUMER_SECRET = 'vQxEJ46vPh9BVinz02yB6fEXCvwrZXSqxxmdoMzmwo9WihDgh4'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)
            
# Search for latest tweets about "#nlproc"
twitter.search.tweets(q='#nlproc')