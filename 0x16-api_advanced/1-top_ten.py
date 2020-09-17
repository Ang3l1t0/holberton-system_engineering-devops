#!/usr/bin/python3
"""prints the titles of the first 10 hot posts"""
import requests


URL = 'http://reddit.com/r/{}/hot.json'


def top_ten(subreddit):
    """Get top 10 hot posts"""
    headers = {'User-Agent': 'Angel'}
    size_q = {'limit': 10}
    responsable = requests.get(URL.format(
        subreddit), params=size_q, headers=headers)
    children = responsable.json().get("data", {}).get("children", None)

    if children:
        for topic in children:
            print(topic.get("data").get("title"))
    else:
        print("None")
