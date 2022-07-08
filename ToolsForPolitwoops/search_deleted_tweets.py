import sys
import string
from check_user import check_username
from get_tweets import get_tweet_list

def check_deleted_tweet(username, search_tweet):
    # If username doesn't exist, tweet cannot exist
    if not(check_username(username)):
        return False

    strip_string = string.whitespace + string.punctuation
    # Grab all deleted tweets from user
    deleted_tweets = get_tweet_list(username)
    # Filter search_tweet
    filter_tweet = search_tweet.translate({ord(c): None for c in strip_string})
    filter_tweet = filter_tweet.encode('ascii', errors = 'ignore')
    # Check if tweet we are searching for exists
    return (filter_tweet in deleted_tweets)
    

def main(argv):
    # Validate command line arguments
    if(len(sys.argv) != 3):
        print("Incorrect number of arguments; please provide one username and one input file, in that order")
        sys.exit(1)
    if(not check_username(str(sys.argv[1]))):
        print('This user does not have deleted tweets archived on Politwoops')
        sys.exit(2)
    # Open input file
    try:
        with open(sys.argv[2], 'r') as f:
            tweet = f.read()
    except FileNotFoundError:
        print('Please provide an input file that exists')
        sys.exit(3)
    
    # For debugging
    print(tweet)
    
    # Check whether or not the tweet exists
    username = sys.argv[1]
    if(check_deleted_tweet(username, tweet)):
        print('That tweet does exist on Politwoops')
    else:
        print('That tweet does not exist on Politwoops')
        

if __name__ == "__main__":
    main(sys.argv[1:])