import tweepy as tp
import os
import sys

# env based import
from dev import *

env = get_creds(msg=False) # env & msg are eavailable as option parameters

if env == 'development':
    from temp_creds import *
elif env == 'production':
    from creds import *
else:
    print('''
        ** No enviroment API creds founds. **
        Enter Twitter API creds in creds.py for production
        OR
        temp_creds.py for dev env
        ''')
    sys.exit()

# auth
auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tp.API(auth)

# user
screenName = UNAME
user = api.get_user(screen_name = screenName)

# tweets
def cleantwts():
    while len(api.user_timeline(id = user.id, include_rts = True)) > 0:
        tweets = api.user_timeline(id = user.id, include_rts = True)
        for tweet in tweets:
            api.destroy_status(tweet.id)
            print('Deleting tweet: ', tweet.id)
    print('All tweets removed.')

# favs
def cleanfvs():
    while len(api.favorites(screenName)) > 0:
        favs = api.favorites(screenName)
        for like in favs:
            api.destroy_favorite(like.id)
            print('Deleting fav: ', like.id)
    print('All favs removed.')
        
# clean all
def cleanup():
    cleantwts()
    cleanfvs()

print("Welcome to Tweet cleaner 9.1 –– the power levels are OVER 9000!") # welcome message
# user input
try:
    uInput = input("Clean up tweets, favs or both? (t,f or b)\n")
except KeyboardInterrupt:
    print("\nExited.")
    sys.exit()
if uInput == 't' or uInput == 'T':
    try:
        cleantwts()
    except KeyboardInterrupt:
        print('\n\nExited.')
elif uInput == 'f' or uInput == 'F':
    try:
        cleanfvs()
    except KeyboardInterrupt:
        print('\n\nExited.')
elif uInput == 'b' or uInput == 'B':
    try:
        cleanup()
    except KeyboardInterrupt:
        print('\n\nExited.')
else:
    print('\n Type one of the options: t,f or b')