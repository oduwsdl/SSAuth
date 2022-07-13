from bs4 import BeautifulSoup as bs
import sys
from bs4 import SoupStrainer as ss
import requests

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

def main(argv):
    print('I have started')
    url = "https://www.snopes.com/?s=i+guess+we+finally+ran+out+of+microchips"
    soup = grab_links(url)

    list_of_links = grab_links(url)

    print(list_of_links)

    article_url = list_of_links[0]
    print(grab_rating(article_url))




if __name__ == "__main__":
    main(sys.argv[1:])