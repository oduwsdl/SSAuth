from bs4 import BeautifulSoup as bs
import sys
from bs4 import SoupStrainer as ss
import requests
from urllib.parse import urlencode
import string
import codecs
import re

# Function to generate encoded query url from a string
def generate_query_url(reuters_query):
    query_dict = {'blob': reuters_query}
    return ('https://reuters.com/search/news?' + urlencode(query_dict))

# Function to generate truncated query url without cutting off words from tweet_text
def generate_reuters_query(tweet_text):
    # Don't truncate if tweet is already less than 99 chars
    if len(tweet_text) < 126:
        reuters_query = tweet_text
    # Truncate the tweet
    else:
        reuters_query = tweet_text[:125]
        if tweet_text[125] not in string.whitespace:
            index = reuters_query.rfind(" ")
            reuters_query = reuters_query[:index]
    return generate_query_url(reuters_query)

# Function to get all links to fact check articles from a query url
def grab_links(query_url):
    # Make request, setup bs object
    search_results = ss('h3', class_='search-result-title')
    html = requests.get(query_url)
    html_text = html.text
    soup = bs(html_text, 'html.parser', parse_only=search_results)

    # Grab all links from results that are fact check articles
    list_of_links = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if '/article' in url:
            list_of_links.append('http://reuters.com' + url)

    return list_of_links

# Function to grab the verdict rating of a Reuters article given its url
def grab_rating(article_url):
    # Make request, setup bs object
    only_verdict = ss(class_=['Paragraph-paragraph-2Bgue ArticleBody-para-TD_9x', 'Headline-headline-2FXIq Headline-black-OogpV ArticleBody-heading-3h695'])
    html = requests.get(article_url)
    html_text = html.text
    soup = bs(html_text, 'html.parser', parse_only=only_verdict)
    # Search text for the verdict
    text = soup.get_text()
    verdict = re.search(r'\b\w*VERDICT\w*\b', text)
    if verdict:
        return verdict.group()[7:]
    return "No verdict found???"



def main(argv):
    # print('hello')
    # list_of_links = grab_links('https://www.reuters.com/search/news?sortBy=&dateRange=&blob=fake+tweet')
    # print(list_of_links)
    # print(generate_reuters_query('It’s time I confess; The Apollo 11 missions, which landed man for the first time on the moon, was staged, none of it was real.'))
    # print(grab_rating("https://www.reuters.com/article/idUSL1N2SN1UL"))
    try:
        f = codecs.open(sys.argv[1], 'r', 'utf-8"')
        query_str = f.read()
    except FileNotFoundError:
        print('Please provide a valid input file as an argument')
        sys.exit(1)
    except IndexError:
        print("Please provide a valid input file as an argument")
        sys.exit(1)
    query = generate_reuters_query(query_str)
    
    links = grab_links(query)

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
