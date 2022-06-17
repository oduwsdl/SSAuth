# -*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as ss
from check_user import check_username


# Given a valid username, returns a list of all deleted tweets tracked on Politwoops as strings
def get_tweet_list(username):
    # List to hold tweet texts
    tweet_list = []
    # Soup Strainer to parse only tweet-text
    only_tweet_text = ss('p', class_='tweet-text')
    # Store argument for username
    username = str(sys.argv[1])
    
    # Make request for first page of tweets
    page_num = 1
    url = requests.get('https://projects.propublica.org/politwoops/user/' + username + '?page=' + str(page_num))
    html_text = url.text
    soup = bs(html_text, 'html.parser', parse_only=only_tweet_text)
    tag = soup.p
        
    # Loop while tag is valid; page_num refers to page with tweets on it
    while(not(tag is None)):
        # Add tweets on page to list
        for sibling in tag.next_siblings:
            tweet_list.append(sibling.text)
    
        # Make request for next page of tweets
        page_num += 1
        url = requests.get('https://projects.propublica.org/politwoops/user/' + username + '?page=' + str(page_num))
        html_text = url.text
        soup = bs(html_text, 'html.parser', parse_only=only_tweet_text)
        tag = soup.p

    # Get rid of duplicates as there are a lot (usually doubles size of the list)
    tweet_list = list(dict.fromkeys(tweet_list))
    # Get rid of extra newline characters in the tweet
    tweet_list = [tweet.replace('\n', '') for tweet in tweet_list]
    
    return tweet_list

def main(argv):
    
    # Validate command line arguments
    if(len(sys.argv) != 2):
        print("Incorrect number of arguments; please provide one username")
        sys.exit(1)
    if(not check_username(str(sys.argv[1]))):
        print('This user does not have deleted tweets archived on Politwoops')
        sys.exit(2)
        
    username = sys.argv[1]
        
    tweet_list = get_tweet_list(username)
    
    # # List to hold tweet texts
    # tweet_list = []
    # # Soup Strainer to parse only tweet-text
    # only_tweet_text = ss('p', class_='tweet-text')
    # # Store argument for username
    # username = str(sys.argv[1])
    
    # # Make request for first page of tweets
    # page_num = 1
    # url = requests.get('https://projects.propublica.org/politwoops/user/' + username + '?page=' + str(page_num))
    # html_text = url.text
    # soup = bs(html_text, 'html.parser', parse_only=only_tweet_text)
    # tag = soup.p
        
    # # Loop while tag is valid; page_num refers to page with tweets on it
    # while(not(tag is None)):
    #     # Add tweets on page to list
    #     for sibling in tag.next_siblings:
    #         tweet_list.append(sibling.text)
    
    #     # Make request for next page of tweets
    #     page_num += 1
    #     url = requests.get('https://projects.propublica.org/politwoops/user/' + username + '?page=' + str(page_num))
    #     html_text = url.text
    #     soup = bs(html_text, 'html.parser', parse_only=only_tweet_text)
    #     tag = soup.p

    # # Get rid of duplicates as there are a lot (usually doubles size of the list)
    # tweet_list = list(dict.fromkeys(tweet_list))
    # # Get rid of extra newline characters in the tweet
    # tweet_list = [tweet.replace('\n', '') for tweet in tweet_list]
        
    # Print tweets
    for tweet in tweet_list:
        print(tweet)
        

if __name__ == "__main__":
    main(sys.argv[1:])