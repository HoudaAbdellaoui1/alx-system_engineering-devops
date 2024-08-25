#!/usr/bin/python3
""" Get top 10 posts by subreddit from REDDIT API """

import requests

def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit..
    If not a valid subreddit, print None.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = (f'https://www.reddit.com/r/{subreddit}/hot.json')
    params = {'limit': 10}
    subredditData = requests.get(url, headers=headers, timeout=10, params= params)
    if subredditData.status_code == 200:
        hotPosts = subredditData.json()['data']['children']
        for post in hotPosts:
            print(post['data']['title'])
    else:
        print('None')
