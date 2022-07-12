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

def main(argv):
    print('I have started')
    url = "https://www.snopes.com/?s=i+guess+we+finally+ran+out+of+microchips"
    soup = grab_links(url)

    list_of_links = grab_links(url)

    print(list_of_links)

    follow_link = requests.get(list_of_links[0])
    follow_link_html = follow_link.text
    follow_soup = bs(follow_link_html, 'html.parser')
    print(follow_soup.prettify())




if __name__ == "__main__":
    main(sys.argv[1:])