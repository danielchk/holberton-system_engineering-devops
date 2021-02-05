#!/usr/bin/python3
"""Get request to reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=1):
    """Query hot post with recursive function"""
    base_url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {"User-Agent":
               "linux:0x16.api.advanced:v1.0.0 (by /u/danielchk)"}
    par = {'limit': 100, 'after': after}
    r = requests.get(base_url, headers=headers,
                     allow_redirects=False, params=par)
    j = r.json()
    if j.get('error', 200) == 404:
        return None
    if after is None:
        return hot_list
    l = j.get('data').get('children')
    for dic in l:
        hot_list.append(dic.get('data').get('title'))
    p = j.get('data').get('after')
    return recurse(subreddit, hot_list, p)
