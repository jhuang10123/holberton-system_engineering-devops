#!/usr/bin/python3
"""
queries the Reddit API and returns the top 10
posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        req = requests.get(
            url, allow_redirects=False, headers={
                'User-Agent': 'Jennifer12345'},
            params={'limit': 10})

        # getting data children from 'data' of req.json()
        children = req.json().get('data').get('children')
        # loop through list of dict and print out value of 'title' for each
        for child in children:
            print(child.get('data').get('title'))
    except:
        print(None)
