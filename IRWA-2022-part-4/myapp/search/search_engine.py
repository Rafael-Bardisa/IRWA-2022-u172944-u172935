import os
import random

from myapp.search.algorithms import search_in_corpus
from myapp.search.load_corpus import load_corpus
from myapp.search.objects import ResultItem, Document


def build_demo_results(corpus: dict, search_id):
    """
    Helper method, just to demo the app
    :return: a list of demo docs sorted by ranking
    """
    res = []
    size = len(corpus)
    ll = list(corpus.values())
    for index in range(random.randint(0, 40)):
        item: Document = ll[random.randint(0, size)]
        res.append(ResultItem(item.id, item.title, item.description, item.doc_date,
                              "doc_details?id={}&search_id={}&param2=2".format(item.id, search_id), random.random()))

    for index, item in enumerate(corpus['Id']):
        # DF columns: 'Id' 'Tweet' 'Username' 'Date' 'Hashtags' 'Likes' 'Retweets' 'Url' 'Language'
        # TODO tambien en la de abajo
        res.append(Document(item.Id, item.Tweet, item.Tweet, item.Date,
                                "doc_details?id={}&search_id={}&param2=2".format(item.Id, search_id), random.random()))

    # simulate sort by ranking
    res.sort(key=lambda doc: doc.ranking, reverse=True)
    return res


class SearchEngine:
    """educational search engine"""

    def search(self, search_query, search_id, corpus):
        print("Search query:", search_query)

        results = []
        # TODO ##### your code here #####
        # results = build_demo_results(corpus, search_id)  # TODO replace with call to search algorithm

        results = [id for id, _ in search_in_corpus(search_query).items()]
        # TODO ##### your code here #####

        return results


if __name__ == '__main__':
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    file_path = path + "/tweets-data-who.json"

    # file_path = "../../tweets-data-who.json"
    corpus = load_corpus(file_path)
    print(SearchEngine.search("Risk", corpus,))
