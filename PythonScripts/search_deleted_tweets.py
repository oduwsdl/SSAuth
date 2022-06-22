import sys
import string
from check_user import check_username
from soup_test import get_tweet_list

def check_deleted_tweet(username, search_tweet):
    # If username doesn't exist, tweet cannot exist
    if not(check_username(username)):
        return False

    # Grab all deleted tweets from user
    deleted_tweets = get_tweet_list(username)

    # Check if tweet we are searching for exists
    return (search_tweet in deleted_tweets)
    

def main(argv):
    try:
        with open(sys.argv[2], 'r') as f:
            tweet = f.read()
    except FileNotFoundError:
        print('Please provide an input file that exists')
        sys.exit(1)
    
    tweet = tweet.translate({ord(c): None for c in string.whitespace})
    
    print(tweet)
    
    username = sys.argv[1]
    if(check_deleted_tweet(username, tweet)):
        print('That tweet does exist on Politwoops')
    else:
        print('That tweet does not exist on Politwoops')
        

if __name__ == "__main__":
    main(sys.argv[1:])