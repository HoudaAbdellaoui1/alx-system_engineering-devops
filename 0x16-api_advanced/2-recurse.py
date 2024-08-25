#!/usr/bin/python3
""" Get top 10 posts by subreddit from REDDIT API """

import requests
import sys

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of all hot articles for a given subreddit.
    If no results are found or the subreddit is invalid, returns None.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = (f'https://www.reddit.com/r/{subreddit}/hot.json')
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            if not posts:
                return hot_list if hot_list else None
            
            for post in posts:
                hot_list.append(post['data']['title'])
            
            # Check if there are more pages to fetch
            after = data['data'].get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
