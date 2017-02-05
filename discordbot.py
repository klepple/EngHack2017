import discord
import asyncio
import sys
import requests
import requests.auth
import tweepy
import sys

def checkRedditLink(name):
    #name = str(sys.argv)[18:-2]
    client_auth = requests.auth.HTTPBasicAuth('bq6xNnLFIVrAHw', 'Xmju_5JnWLnZM-nr4vyej9seXE4')
    post_data = {"grant_type": "password", "username": "enghack_script", "password": "ayy_lmao"}
    headers = {"User-Agent": "enghack_script/0.1 by enghack_script"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    accesstoken = response.text[18:45]
    headers = {"Authorization": "bearer " + accesstoken, "User-Agent": "enghack_script/0.1 by enghack_script"}
    response = requests.get("https://oauth.reddit.com/user/" + name + "/about/.json", headers=headers)
    response.json()
    #These find the comment and link karma.
    return (response.text[response.text.index("link_karma") + 13:response.text.index(", \"comment")])

def checkRedditComment(name):
    #name = str(sys.argv)[18:-2]
    client_auth = requests.auth.HTTPBasicAuth('bq6xNnLFIVrAHw', 'Xmju_5JnWLnZM-nr4vyej9seXE4')
    post_data = {"grant_type": "password", "username": "enghack_script", "password": "ayy_lmao"}
    headers = {"User-Agent": "enghack_script/0.1 by enghack_script"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    accesstoken = response.text[18:45]
    headers = {"Authorization": "bearer " + accesstoken, "User-Agent": "enghack_script/0.1 by enghack_script"}
    response = requests.get("https://oauth.reddit.com/user/" + name + "/about/.json", headers=headers)
    response.json()
    #These find the comment and link karma.
    return (response.text[response.text.index("comment_karma") + 16:response.text.index(", \"is_gold")])

def checkRedditKarma(name):
    #name = str(sys.argv)[18:-2]
    client_auth = requests.auth.HTTPBasicAuth('bq6xNnLFIVrAHw', 'Xmju_5JnWLnZM-nr4vyej9seXE4')
    post_data = {"grant_type": "password", "username": "enghack_script", "password": "ayy_lmao"}
    headers = {"User-Agent": "enghack_script/0.1 by enghack_script"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    accesstoken = response.text[18:45]
    headers = {"Authorization": "bearer " + accesstoken, "User-Agent": "enghack_script/0.1 by enghack_script"}
    response = requests.get("https://oauth.reddit.com/user/" + name + "/about/.json", headers=headers)
    response.json()
    #These find the comment and link karma.
    try:
        lkarma = (response.text[response.text.index("link_karma") + 13:response.text.index(", \"comment")])
        lkarma = int(lkarma)
        ckarma = (response.text[response.text.index("comment_karma") + 16:response.text.index(", \"is_gold")])
        ckarma = int(ckarma)
        return lkarma + ckarma
    else:
        return "failed"


def checkTwitter(name):
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
    #name = str(sys.argv)[19:-2]
    # Sample method, used to update a status
    # api.update_status('All these tweets are generated using API!')

    # Get the User object for twitter...
    user = api.get_user(name)
    return str(user.followers_count)

# start of discord implementation
client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    elif message.content.startswith('!help'):
        msg = "Commands: !help, !checkredditlinkkarma [name], !checkredditcommentkarma [name], !checkredditkarma [name], !checktwitter [name]"
        await client.send_message(message.author.server, msg)
 
    if message.content.startswith('!checkredditlinkkarma'):
        if ' ' in message.content:
            name = message.content[message.content.index(' ') + 1:]
            msg = name + ' has ' + checkRedditLink(name) + ' link karma'
        else:
            msg = 'No valid name.'
        await client.send_message(message.author.server, msg)

    elif message.content.startswith('!checkredditcommentkarma'):
        if ' ' in message.content:
            name = message.content[message.content.index(' ') + 1:]
            msg = name + ' has ' + checkRedditComment(name) + ' comment karma'
        else:
            msg = 'No valid name.'
        await client.send_message(message.author.server, msg)

    elif message.content.startswith('!checkredditkarma'):
        if ' ' in message.content:
            name = (message.content[message.content.index(' ') + 1:])
            if(checkRedditKarma(name) == "failed"):
                return
            points = str(checkRedditKarma(name))
            msg = name + ' has ' + points + ' total karma'
        else:
            msg = 'No valid name.'
        await client.send_message(message.author.server, msg)

    elif message.content.startswith('!checktwitter'):
        if ' ' in message.content:
            name = message.content[message.content.index(' ') + 1:]
            msg = name + " has " + checkTwitter(name) + " followers."
        else:
            msg = 'No valid name.'
        await client.send_message(message.author.server, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('Mjc3NjY1ODYyMTgwNDA1MjU4.C3hZQQ.nen8MwDG4blkX9WvUnqh7fUIkBU')