#API Key: GqlfdaQUbr5Ic9GLW2hiFUVD3
#API Secret: vQxEJ46vPh9BVinz02yB6fEXCvwrZXSqxxmdoMzmwo9WihDgh4
#Access token: 827998835569999876-g2v5tnrhuz0ab4uvdbhOFUh8pQZt7qo
#Access token secret: 49NpU9CefbcThL9y0Gw7XBWwUaxmqU7DDaeaO5zv75YAu

import tweepy
import sys

# Variables that contains the user credentials to access Twitter API
access_token = '827998835569999876-g2v5tnrhuz0ab4uvdbhOFUh8pQZt7qo'
access_token_secret = '49NpU9CefbcThL9y0Gw7XBWwUaxmqU7DDaeaO5zv75YAu'
consumer_key = 'GqlfdaQUbr5Ic9GLW2hiFUVD3'
consumer_secret = 'vQxEJ46vPh9BVinz02yB6fEXCvwrZXSqxxmdoMzmwo9WihDgh4'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)
# User name
name = str(sys.argv)[19:-2]
# Sample method, used to update a status
# api.update_status('All these tweets are generated using API!')

# Get the User object for twitter...
user = api.get_user(name)
print(user.followers_count)
