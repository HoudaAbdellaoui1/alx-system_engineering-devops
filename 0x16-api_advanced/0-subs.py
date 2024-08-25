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
    getSubredditDataUrl = (f'https://www.reddit.com/r/{subreddit}/about.json')
    subredditData = requests.get(getSubredditDataUrl, headers=headers, timeout=10)
    if subredditData.status_code == 200:
        subscribersCount = subredditData.json()['data']['subscribers']
        return subscribersCount
    else:
        return 0
