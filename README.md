# SSAuth

## Tools to Query For Evidence of Tweet Misattribution on the Web

These tools were developed in service of the "Did They Really Say That?" project, which focuses on establishing the authenticity of a screenshot of a social media post.
Currently, there are tools to query for evidence of tweet attribution from the sites Snopes, Reuters, and Politwoops. There is also a tool to query Google for evidence from those sites.
All tools accept the full body of a tweet as a command line argument to construct the query. 
Any evidence found is also scraped for a "truth value" that can be used in determining the veracity of the given tweet.

### Politwoops

The Politwoops script will construct a query to the Politwoops search engine, and determine if any of the results of the query matches the original tweet.
#### Usage
The following is an example of a query for a deleted Donald Trump tweet that is found on Politwoops.
```
$ python3 query_politwoops.py "China steals United States Navy research drone in international waters - rips it out of water and takes it to China in unpresidented act."
That tweet was successfully queried on Politwoops.
```

### Snopes/Reuters
The Snopes and Reuters scripts function in much the same way. They will both construct queries to their respective native search engines and return the URLs of any articles found, as well as the truth rating described in that article.
#### Usage
The following is an example of a query for a fake tweet that has an associated fact-check article on Snopes.
```
python3 query_snopes.py "China steals United States Navy research drone in international waters - rips it out of water and takes it to China in unpresidented act."
Article found at URL: https://www.snopes.com/fact-check/trump-sends-unpresidented-tweet/
Truth Rating: True
```

### Google
The Google script will construct a Google query and scrape any results from the sites that we curently support.
#### Usage
The following is an example of a query for a fake tweet that has related fact-check articles on both Snopes and Reuters.
```
python3 query_google.py "I think most Americans would agree that I'm a level-headed individual, not a man who's prone to indulging in conspiracy theories. I've certainly had a fair number directed at me. But has anyone checked to make sure Donald Trump doesn't have a Russian birth certificate?"
Reuters article found at URL: https://www.reuters.com/article/factcheck-obamatweet-notreal/fact-check-fabricated-obama-tweet-about-trump-and-birth-certificate-was-created-as-satire-idUSL2N2W31AK
Verdict found in this article is Satire
Snopes article found at URL: https://www.snopes.com/fact-check/fake-obama-tweet/
Truth rating in this article is False
```

## Ground Truth Dataset of Tweets with Evidence of Attribution on the Web
A ground truth dataset containing 30 tweets with associated articles on Snopes.com was also constructed for this project in order to evaluate the efficacy of our tools.
Each entry contains the body of the tweet, the URL of the Snopes article, live and archived query URLs for queries as constructed by the script, and MRR and P@1 values measuring how those queries performed in finding the Snopes article.
This dataset should be added to in the future with more tweets with evidence from a wider variety of sources. 
