import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key = 'ytIKCBZJKtzjoMrrFy4G4bSQf'
consumer_secret = 'hkzhs0u3If1dhpguWESikugGOqxI0RAwLhbrJstYjekWwPzBNJ'

access_token = '401994600-7v775e06y3g6Q8nZlqOUNqy6LHFxBbDK1hY7R8Wk'
access_token_secret = 'miTFABxXH3lNmEMdtnCXI0JfxoTxtIkoiOt78SgvsxUUZ'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.search('Trump')

i = 0
for tweet in tweepy.Cursor(api.search,
                           q="google",
                           count=1,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
    print(tweet.text)

    wiki = TextBlob(tweet.text)
    print("      " + wiki.sentiment.polarity)
    