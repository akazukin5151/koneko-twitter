import shutil

import funcy
import requests
from twitter_scraper import get_tweets


class APIHandler:
    @funcy.retry(tries=3, errors=ConnectionError)
    def all_tweets(self, user) -> 'Json':
        return get_tweets(user, pages=1)

    @funcy.retry(tries=3, errors=ConnectionError)
    def user_pic_tweets(self, user) -> 'Json':
        return [tweet for tweet in self.all_tweets(user)
                if not tweet['isPinned']
                and not tweet['isRetweet']
                and tweet['entries']['photos']]

    @funcy.retry(tries=3, errors=ConnectionError)
    def all_user_tweets(self, user) -> 'Json':
        return [tweet for tweet in self.all_tweets(user)]

    # Download
    @funcy.retry(tries=3, errors=ConnectionError)
    def protected_download(self, url, path, name) -> 'IO':
        r = requests.get(url, stream=True)
        with open(path / name, 'wb') as f:
            shutil.copyfileobj(r.raw, f)


myapi = APIHandler()
