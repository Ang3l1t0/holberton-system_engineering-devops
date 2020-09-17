#!/usr/bin/python3
""" Returns the number of subscribers (not active users, total subscribers) 
    for a given subreddit.
"""
import requests


URL = 'http://reddit.com/r/{}/about.json'


def number_of_subscribers(subreddit):
    """Get number of subscribers
    """
    headers = {'User-Agent': 'Angel'}
    response = requests.get(URL.format(subreddit), headers=headers)
    return response.json().get('data', {}).get('subscribers', 0)
