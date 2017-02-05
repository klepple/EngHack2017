import sys
import requests
import requests.auth
name = str(sys.argv)[18:-2]
client_auth = requests.auth.HTTPBasicAuth('bq6xNnLFIVrAHw', 'Xmju_5JnWLnZM-nr4vyej9seXE4')
post_data = {"grant_type": "password", "username": "enghack_script", "password": "ayy_lmao"}
headers = {"User-Agent": "enghack_script/0.1 by enghack_script"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
accesstoken = response.text[18:45]
headers = {"Authorization": "bearer " + accesstoken, "User-Agent": "enghack_script/0.1 by enghack_script"}
response = requests.get("https://oauth.reddit.com/user/" + name + "/about/.json", headers=headers)
response.json()
#These find the comment and link karma.

print(response.text[response.text.index("link_karma") + 13:response.text.index(", \"comment")])
print(response.text[response.text.index("comment_karma") + 16:response.text.index(", \"is_gold")])


#username : enghack_script
#password : ayy_lmao
#id : bq6xNnLFIVrAHw
#secret : Xmju_5JnWLnZM-nr4vyej9seXE4

