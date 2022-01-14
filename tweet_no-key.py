#tweetを投稿
 
import tweepy
 
# 取得した各種キーを格納-----------------------------------------------------
consumer_key ="key"
consumer_secret ="key"
access_token="key"
access_token_secret ="key"
 
# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#-------------------------------------------------------------------------
# ツイートを投稿
api.update_status("投稿されてくれ～！")

#api.create_favotite("1481300588956889090")

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# the ID of the status 
#id = 1481300588956889090
# fetching the status 
#status = api.get_status(id)