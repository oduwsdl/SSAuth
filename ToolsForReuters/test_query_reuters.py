from query_reuters import generate_reuters_query
from query_reuters import grab_links
from query_reuters import grab_rating

def test_grab_links():
    print('testing')
    tweet = "Lies lies we are fine here in SA no variant nothing. Unemployment rate is at 40%, petrol price at $2 a Litre. Poverty and unemployment are the major pandemics here not this covid thing..."
    query = generate_reuters_query(tweet)
    links = grab_links(query)
    assert(len(links) == 1)
    assert(links[0] == "http://reuters.com/article/idUSL1N2SN1UL")

def test_grab_rating():
    print('testing')
    url = "http://reuters.com/article/idUSL1N2SN1UL"
    assert(grab_rating(url) == "False")
