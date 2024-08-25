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

    try:
        subredditData = requests.get(url, headers=headers, timeout=10,
                                     params=params, allow_redirects=False)
        if subredditData.status_code == 200:
            data = subredditData.json()
            posts = data['data']['children']

            # If no posts are found, return None
            if not posts:
                print(None)
                return

            # Print the titles of the first 10 hot posts
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print('None')
