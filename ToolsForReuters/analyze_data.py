import sys
import json
import codecs

def main(argv):
    print('analyzing data')

    with codecs.open('dataset.json', 'r', 'utf-8') as f:
        data = json.load(f)

    total_articles = len(data['Reuters Articles'])
    reuters_pre_at_one = 0
    reuters_reciprocal_total = 0

    for article in data['Reuters Articles']:
        datapoint = data['Reuters Articles'][article]
        reuters_pre_at_one = reuters_pre_at_one + datapoint["Precision at 1"]
        reuters_reciprocal_total = reuters_reciprocal_total + datapoint["Reciprocal rank"]

    reuters_pre_rate = round(reuters_pre_at_one / total_articles, 4)
    reuters_reciprocal_rate = round(reuters_reciprocal_total / total_articles, 4)

    print('Average precision at 1 value: ' + str(reuters_pre_rate))
    print('Average reciprocal rank: ' + str(reuters_reciprocal_rate))

if __name__ == "__main__":
    main(sys.argv[1:])