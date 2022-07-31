import sys, os
import json
import codecs
sys.path.append(os.path.realpath('..'))

from scraper.Google import googleSearch
from ToolsForSnopes.query_snopes import grab_rating as snopes_rating
from ToolsForReuters.query_reuters import grab_rating as reuters_rating

# Shortens a given text to 32 words (max word count for a google search)
def shorten_google_query(tweet):
    tweet_list = tweet.split()
    if len(tweet_list) < 32:
        return tweet
    shortened_tweet_list = tweet_list[:32]
    return ' '.join(shortened_tweet_list)

# Make a query to Google, returns full list of links from SERP
def make_google_query(tweet):
    serp = googleSearch(tweet)
    links = []
    for link in serp["links"]:
        links.append(link["link"])
    return links

# Filter to just sites that we can use to verify attribution (can be added to)
def filter_links(links_list):
    sites_we_want = ['twitter.com', 'snopes.com/fact-check', 'reuters.com/article']
    return [link for link in links_list if any(site in link for site in sites_we_want)] # i think this is cool


def main(argv):
    try:
        f = codecs.open(sys.argv[1], 'r', 'utf-8')
        query_str = f.read()
    except FileNotFoundError:
        print('Please provide a valid input file as an argument')
        sys.exit(1)
    except IndexError:
        print("Please provide a valid input file as an argument")
        sys.exit(1)
    links = make_google_query(query_str)
    links = filter_links(links)
    for link in links:
        if 'snopes.com/fact-check' in link:
            rating = snopes_rating(link)
            print("Snopes article found at URL: " + link)
            print("Truth rating in this article is " + rating)
        elif 'reuters.com/article' in link:
            rating = reuters_rating(link)
            print("Reuters article found at URL: " + link)
            print("Verdict found in this article is " + rating)
        elif 'twitter.com' in link:
            print("Tweet or related tweet potentially found on live web at URL " + link)


    


if __name__ == "__main__":
    main(sys.argv[1:])