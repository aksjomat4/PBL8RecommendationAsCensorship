#! /usr/bin/python3

from re import sub
import praw
from praw.models import MoreComments
import pandas as pd
import datetime as dt
import time
import json

from praw.reddit import Comment
import logging

logging.basicConfig(level=logging.DEBUG)

#Put your own credentials. Tutorial: https://medium.com/swlh/scraping-reddit-using-python-57e61e322486
reddit = praw.Reddit(client_id='-91uRXCnlIGkRg', \
                     client_secret='Kk2ESnCHaADusoQ1HI948NdDODelVw', \
                     user_agent='reditScrapper', \
                     username='aksjomat4', \
                     password='AbCd123')

url = "https://www.reddit.com/r/PublicFreakout/comments/nhr1cy/exactly_12_hours_since_the_ceasefire_israeli/?sort=controversial"
#url = "https://www.reddit.com/r/pics/comments/l77fdv/twelve_years_ago_the_world_was_bankrupted_and/"
#url = "https://www.reddit.com/r/gifs/comments/hrpgzt/leaked_drone_footage_of_shackled_and_blindfolded/"

submission = reddit.submission(url=url)

begin = time.time()

#submission.comment_sort = "controversial"
submission.comments.replace_more(limit=None)
comment_queue = submission.comments[:]

l = []
while comment_queue:
    comment = comment_queue.pop(0)
    comment_queue.extend(comment.replies)
    d = comment.__dict__
    d.pop("_replies")
    d.pop("_submission")
    d.pop("_reddit")
    d["author"] = str(d["author"])
    d.pop("subreddit")
    l.append(d)

print(time.time() - begin)
print("  ".join([str(e.controversiality) for e in comment_queue]))

with open("data.json", "w") as f:
    json.dump(l, f, indent=4, sort_keys=True)

while comment_queue:
    comment = comment_queue.pop(0)
    print(comment.author, comment.body)
    try:
        comment_queue.extend(comment.replies)
    except AttributeError:
        pass
