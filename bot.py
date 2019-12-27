from twython import Twython
import random
import time

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

viewed = []
while True:
    try:
         results = twitter.cursor(twitter.search, q="maxh76")
         for result in results:
             name = result['user']
             screen_name = name['screen_name']
             tweet = result['text']
             id = result['id']
             if screen_name == 'maxh76' id not in viewed:
                 print(tweet)
                 viewed.append(id)
                 messages = ["max bad!", "max bad.", "max bad?", "max bad!"]
                 message = random.choice(messages) + " @" + screen_name
                 result = twitter.update_status(status=message, in_reply_to_status_id=id)
                 print(message)
    except:
        print("no more tweets")
        time.sleep(30)

