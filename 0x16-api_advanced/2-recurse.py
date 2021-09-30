#!/usr/bin/python3
"""
    Call to Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ Using Reddit API
        Ask for all the title of a given subreddit
    """
    hot_lists = []
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:app:v0.0.0 (by /u/Any_Manager_3702)"
    }
    params = {
        'after': after
    }
    req = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if req.status_code == 404:
        return(None)
    elif after is None:
        return

    response = req.json().get('data').get('children')

    for childrens in response:
        hot_list.append(childrens.get('data').get('title'))
    after = req.json().get('data').get('after')
    recurse(subreddit, hot_list=hot_list, after=after)
    return hot_list
