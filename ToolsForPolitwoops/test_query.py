# -*- coding: utf-8 -*-

from query_politwoops import query_politwoops


def test_query():
    query_tweet = "Glad to see the Easley Fire Deparment is showcasing their new US flag that I was honored to have flown for them over the Capitol. I’m thankful for these brave men and women who serve our community daily! https://t.co/C696pEVV9t"
    assert(query_politwoops(query_tweet))
    print("The test passed")