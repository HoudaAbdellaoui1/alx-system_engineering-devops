#!/usr/bin/python3
""" Gather subscribers count by subreddit from REDDIT API """

import requests
import sys


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = (f'https://www.reddit.com/r/{subreddit}/about.json')
    try:
        subs = requests.get(url, headers=headers, timeout=10,
                            allow_redirects=False)
        if subs.status_code == 200:
            subscribersCount = subs.json()['data']['subscribers']
            return subscribersCount
        else:
            return 0
    except requests.RequestException:
        # Return 0 if there's an error (e.g., network issue, invalid subreddit)
        return 0
