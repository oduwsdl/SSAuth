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
    print('hello')
    list_of_links = grab_links('https://www.reuters.com/search/news?sortBy=&dateRange=&blob=fake+tweet')
    print(list_of_links)

if __name__ == "__main__":
    main(sys.argv[1:])
