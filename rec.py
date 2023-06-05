import tweepy
import csv

# Get your Twitter API credentials from https://developer.twitter.com/en/apps
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Create an OAuthHandler object
auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)

# Set the access token and secret
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# Set the output file name
output_file = "tweets.csv"

# Create a CSV writer object
csv_writer = csv.writer(open(output_file, "w"))

# Iterate over the tweets and write them to the CSV file
for tweet in tweepy.Cursor(api.search_tweets, q="keyword", lang="en", max_results=100).items():
    # Get the tweet fields
    text = tweet.text
    created_at = tweet.created_at
    user_screen_name = tweet.user.screen_name
    user_location = tweet.user.location
    user_followers_count = tweet.user.followers_count
    retweet_count = tweet.retweet_count
    favorite_count = tweet.favorite_count

    # Write the tweet fields to the CSV file
    csv_writer.writerow([created_at, text, user_screen_name, user_location, user_followers_count, retweet_count, favorite_count])

    # Wait for the rate limit to reset
    api.wait_on_rate_limit()



