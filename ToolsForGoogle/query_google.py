import sys
import json
import codecs
from scraper.Google import googleSearch

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
    print(filter_links(links))


    


if __name__ == "__main__":
    main(sys.argv[1:])