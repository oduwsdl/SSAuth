from bs4 import BeautifulSoup as bs
import sys
from bs4 import SoupStrainer as ss
import requests
from urllib.parse import urlencode

def grab_links(query_url):
    # Setup bs object
    only_links = ss('a', class_="link")
    html = requests.get(query_url)
    html_text = html.text
    soup = bs(html_text, "html.parser", parse_only=only_links)
    list_of_links = []
    for link in soup.find_all('a'):
        list_of_links.append(link.get('href'))
    
    return list_of_links

def grab_rating(article_url):
    print('grabbing rating')
    rating_strainer = ss(class_ = 'figure-image img-responsive img-fluid w-100 Media--image')
    html = requests.get(article_url)
    html_text = html.text
    soup = bs(html_text, 'html.parser', parse_only = rating_strainer)
    tag = soup.img
    return tag.get('alt')

def generate_query_url(snopes_query):
    query_dict = {'s': snopes_query}
    print(urlencode(query_dict))
    return ('?' + urlencode(query_dict))

def main(argv):
    print('I have started')
    query_str = 'I guess we ran out of microchips'
    snopes_url = "https://www.snopes.com/"
    query = snopes_url + generate_query_url(query_str)
    print(query)

    list_of_links = grab_links(query)

    print(list_of_links)

    article_url = list_of_links[0]
    print(grab_rating(article_url))




if __name__ == "__main__":
    main(sys.argv[1:])