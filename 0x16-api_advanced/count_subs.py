#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    '''A function that gets the total number of subscribers from reddit api'''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) \
        Gecko/20100101 Firefox/73.0"
    }

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 404:
        return 0
    return response.json().get('data').get('subscribers')
