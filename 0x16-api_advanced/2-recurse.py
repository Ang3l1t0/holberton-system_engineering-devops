#!/usr/bin/python3
"""returns a list containing the titles of all hot articles for a given subreddit"""
import requests


URL = 'http://reddit.com/r/{}/hot.json'


def recurse(subreddit, hot_list=[]):
    """Get all hot posts"""
    headers = {'User-Agent': 'Angel'}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return hot_list
        response = requests.get(URL.format(subreddit),
                                headers=headers, params=params)
        if response.status_code != 200:
            return None
        data = response.json().get('data', {})
        after = data.get('after', 'STOP')
        if not after:
            after = "STOP"
        hot_list = hot_list + [post.get('data', {}).get('title')
                            for post in data.get('children', [])]
        return recurse(subreddit, hot_list, after)
