import json
import sys

def main(argv):
    with open('dataset.json') as f:
        data = json.load(f)

    snopes_found = 0
    google_with_site_found = 0
    google_without_site_found = 0
    total_snopes_rank = 0
    total_google_rank = 0
    total_google_with_site_rank = 0
    total_articles = len(data['Snopes Articles'])

    for article in data['Snopes Articles']:
        datapoint = data['Snopes Articles'][article]
        snopes_found = snopes_found + datapoint["Snopes query"]["Precision at 1"]
        total_snopes_rank = total_snopes_rank + datapoint["Snopes query"]["Reciprocal rank"]
        google_with_site_found = google_with_site_found + datapoint["Google query (site:snopes.com)"]["Precision at 1"]
        total_google_with_site_rank = total_google_with_site_rank + datapoint["Google query (site:snopes.com)"]["Reciprocal rank"]
        google_without_site_found = google_without_site_found + datapoint["Google query"]["Precision at 1"] 
        total_google_rank = total_google_rank + datapoint["Google query"]["Reciprocal rank"]



    snopes_precision_rate = round((snopes_found / total_articles), 4)
    google_with_precision_rate = round((google_with_site_found / total_articles), 4)
    google_without_precision_rate = round((google_without_site_found / total_articles), 4)
    snopes_MRR = round((total_snopes_rank / total_articles), 4)
    google_MRR = round((total_google_rank / total_articles), 4)
    google_with_site_MRR = round((total_google_with_site_rank / total_articles), 4)

    print("Rate that articles queried using Snopes were at position 1: " + str(snopes_precision_rate))
    print("Rate that articles queried using google without site were at position 1: " + str (google_without_precision_rate))
    print("Rate that articles queried using google with site were at position 1: " + str (google_with_precision_rate))
    print("Mean reciprocal rank for Snopes: " + str(snopes_MRR))
    print("Mean reciprocal rank for google: " + str(google_MRR))
    print("Mean reciprocal rank for google with site: " + str(google_with_site_MRR))

if __name__ == "__main__":
    main(sys.argv[1:])