#!/usr/bin/python3
"""request subscribers number of reddit"""
import requests


def number_of_subscribers(subreddit):
    """return number of subscribers"""
    url = "https://www.reddit.com/r/{}/.json".format(subreddit)
    head = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    res = requests.get(url.format(subreddit),
                        headers=head, allow_redirects=False)
    if res.status_code == 404:
        return 0
    sus = res.json().get("data")
    return sus.get("suscribers")
