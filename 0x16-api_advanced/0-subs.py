#!/usr/bin/python3
"""
    Call to Reddit API
"""
import requests

def number_of_subscribers(subreddit):
    """ Using Reddit API
        Ask for the number of sub for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:fm1btuY2xWEYYcV2LIwyKw:v0.0.0 (by /u/Any_Manager_3702)"
    }
    req = requests.get(url, headers=headers, allow_redirects=False)
    return 0 if req.status_code == 404 else req.json().get("data").get("subscribers")
