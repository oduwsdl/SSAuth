from query_snopes import generate_snopes_query
from query_snopes import grab_links
from query_snopes import grab_rating

def test_grab_links():
    tweet = "There is nothing that I would want more for our Country than true FREEDOM OF THE PRESS. The fact is that the Press is FREE to write and say anything it wants, but much of what it says is FAKE NEWS, pushing a political agenda or just plain trying to hurt people. HONESTY WINS!"
    query = generate_snopes_query(tweet)
    list_of_links = grab_links(query)
    assert(len(list_of_links) == 0)
    assert(list_of_links[0] == "https://www.snopes.com/fact-check/trump-tweet-echo-mein-kampf/")

def test_grab_rating():
    test_url = "https://www.snopes.com/fact-check/trump-tweet-echo-mein-kampf/"
    assert(grab_rating(test_url) == "Correct Attribution")