from bs4 import BeautifulSoup as bs
import sys
from bs4 import SoupStrainer as ss
import requests
from urllib.parse import urlencode
import string
import codecs

# Function to grab all links from a query url that are fact checks
def grab_links(query_url):
    # Make request, setup bs object
    link_class_tag = "link" # can be changed if site changes
    only_links = ss('a', class_=link_class_tag)
    html = requests.get(query_url)
    html_text = html.text
    soup = bs(html_text, "html.parser", parse_only=only_links)
    # Create list with links to all fact check articles found
    list_of_links = []
    fact_check_url = 'https://www.snopes.com/fact-check/'
    for link in soup.find_all('a'):
        url = link.get('href')
        if url[:34] == fact_check_url:
            list_of_links.append(url)
    
    return list_of_links

# Given a url for a fact check article, returns the truth rating from it
def grab_rating(article_url):
    # Make request, setup bs object
    rating_img_class_tags = ['figure-image img-responsive img-fluid w-100 Media--image', 'figure-image img-responsive img-fluid w-100'] # can be changed if site changes
    rating_strainer = ss(class_= rating_img_class_tags)
    html = requests.get(article_url)
    html_text = html.text
    soup = bs(html_text, 'html.parser', parse_only = rating_strainer)
    # Grab and return the truth rating from the article
    tag = soup.img
    return tag.get('alt')

# Function to generate encoded query url from a string
def generate_query_url(snopes_query):
    query_dict = {'s': snopes_query}
    return ('https://www.snopes.com/?' + urlencode(query_dict))

def generate_snopes_query(tweet_text):
    # Don't truncate if tweet is already less than 99 chars
    if len(tweet_text) < 99:
        snopes_query = tweet_text
    # Truncate the tweet
    else:
        snopes_query = tweet_text[:99]
        if tweet_text[99] not in string.whitespace:
            index = snopes_query.rfind(" ")
            snopes_query = snopes_query[:index]
    # Return query as a url
    return generate_query_url(snopes_query)

def main(argv):
    # Open input file
    try:
        f = codecs.open(sys.argv[1], 'r', 'utf-8"')
        query_str = f.read()
    except FileNotFoundError:
        print('Please provide a valid input file as an argument')
        sys.exit(1)
    except IndexError:
        print("Please provide a valid input file as an argument")
        sys.exit(1)
    query = generate_snopes_query(query_str)
    # Grab all links from query
    links = grab_links(query)
    # Output url and rating of every article found
    if len(links) == 0:
        print('No articles queried')
    elif len(links) == 1:
        print('Article found at URL: ' + links[0])
        print("Truth rating: " + grab_rating(links[0]))
    else:
        print('Multiple articles found: ')
        for link in links:
            print('Article queried: ' + link)
            print('Truth rating: ' + grab_rating(link))


if __name__ == "__main__":
    main(sys.argv[1:])