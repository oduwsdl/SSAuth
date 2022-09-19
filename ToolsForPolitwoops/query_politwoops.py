import sys
import requests
import string
import codecs
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as ss
from urllib.parse import urlencode

# Will make a query to Politwoops for tweet passed as argument
# Returns a list containing all results found with the query
# This list may contain elements that have unexpected white space, characters, etc
def perform_query(tweet):
    # Soup Strainer to parse only tweet-text
    tweet_text_tag = 'tweet-text' # can be modified if site changes
    only_tweet_text = ss('p', class_=tweet_text_tag)
    # First part of URL for a query
    site = "https://projects.propublica.org/politwoops/index?utf8=%E2%9C%93&"
    # Creating the query string
    query_tweet = tweet[:50]
    mydict = {'q': query_tweet}
    qstr = urlencode(mydict)
    query = site + qstr
    url = requests.get(query)
    # Parse the results
    html_text = url.text
    soup = bs(html_text, 'html.parser', parse_only=only_tweet_text)
    tag = soup.p
    # Grab all results, if there are any
    results = []
    if(tag is None):
        print('No results found')
    elif(tag.next_sibling is None):
        results.append(tag.text)
    else:
        results.append(tag.text)
        for sibling in tag.next_siblings:
            # print(sibling.text)
            results.append(sibling.text)
    
    return results

# Filters and encodes a tweet into a version that can be compared
# Gets rid of whitespace, encodes text into ascii to get rid of noise that can affect comparison
# Returns filtered version of tweet
def filter_tweet(tweet):
    # Filter out noisy characters
    strip_string = string.whitespace + string.punctuation
    filtered = tweet.translate({ord(c): None for c in strip_string})
    # Encode text into ascii for consistent comparisons
    filtered = filtered.encode('ascii', errors = 'ignore')
    
    return filtered

# Will search tweet_list for tweet
# Utilizes filter_tweet for accurate comparison
# Returns True if tweet is found in tweet_list, False otherwise
def find_tweet(tweet, tweet_list):
    # Filter tweets
    search_tweet = filter_tweet(tweet)
    search_list = [filter_tweet(check_tweet) for check_tweet in tweet_list]
    
    # Do comparison
    return search_tweet in search_list

# Combines functionality of above functions
# Performs query and comparison, returns appropriate boolean
def query_politwoops(tweet):
    query_results = perform_query(tweet)
    return find_tweet(tweet, query_results)

def main(argv):
    if(len(sys.argv) != 2):
        print("Please provide only a supposed tweet as an argument")
        sys.exit(1)
    
    if query_politwoops(sys.argv[1]):
        print("That tweet was successfully queried on Politwoops")
    else:
        print("That tweet was not found on Politwoops")
    
if __name__ == "__main__":
    main(sys.argv[1:])