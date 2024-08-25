#!/usr/bin/python3
""" Gather subscribers count by subreddit from REDDIT API """

import requests



def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }
    try:
        subs = requests.get(url, headers=headers, allow_redirects=False)
        if subs.status_code == 200:
            subscribersCount = subs.json().get('data')
            return subscribersCount.get('subscribers')
        else:
            return 0
    except requests.RequestException:
        return 0
