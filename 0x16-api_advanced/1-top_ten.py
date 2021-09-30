#!/usr/bin/python3
"""
    Call to Reddit API
"""
import requests


def top_ten(subreddit):
    """ Using Reddit API
        Ask for the number of sub for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:app:v0.0.0 (by /u/Any_Manager_3702)"
    }
    params = {
        "limit": 10
    }
    req = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if req.status_code == 404:
        print('None')
        return

    req = req.json().get('data').get('children')

    for childrens in req:
        print(childrens.get('data').get('title'))
