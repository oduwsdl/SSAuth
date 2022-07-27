from bs4 import BeautifulSoup as bs
import sys
from bs4 import SoupStrainer as ss
import requests
from urllib.parse import urlencode
import string
import codecs

# url = requests.get('https://www.reuters.com/search/news?sortBy=&dateRange=&blob=fake+tweet')
# html_text = url.text
# strainer = ss('h3', class_='search-result-title')
# soup = bs(html_text, 'html.parser', parse_only=strainer)
# for link in soup.find_all('a'):
#     print('reuters.com' + link.get('href'))

# Function to generate encoded query url from a string
def generate_query_url(reuters_query):
    query_dict = {'blob': reuters_query}
    return ('https://reuters.com/search/news?' + urlencode(query_dict))


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


def grab_links(query_url):
    search_results = ss('h3', class_='search-result-title')
    html = requests.get(query_url)
    html_text = html.text
    soup = bs(html_text, 'html.parser', parse_only=search_results)
    list_of_links = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if '/article' in url:
            list_of_links.append('http://reuters.com' + url)

    return list_of_links

def main(argv):
    # print('hello')
    # list_of_links = grab_links('https://www.reuters.com/search/news?sortBy=&dateRange=&blob=fake+tweet')
    # print(list_of_links)
    print(generate_reuters_query('It’s time I confess; The Apollo 11 missions, which landed man for the first time on the moon, was staged, none of it was real.'))


if __name__ == "__main__":
    main(sys.argv[1:])
