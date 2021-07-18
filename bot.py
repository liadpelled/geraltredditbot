import praw
import pdb
import re
import os

# Creating Reddit instance
reddit = praw.Reddit('bot1')

# Keeping track of 
if not os.path.isfile('posts_replied_to.txt'):
    posts_replied_to = []

else:
    with open('posts_replied_to.txt', 'r') as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split('\n')
        posts_replied_to = list(filter(None, posts_replied_to))


subreddit = reddit.subreddit('pythonforengineers')

# Getting the top 5 hot posts
for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search('portal', submission.title, re.IGNORECASE):
            submission.reply('GeraltBot says: Hrrrgh, I hate portals.')
            print('GeraltBot is replying to: ', submission.title)
            posts_replied_to.append(submission.id)

with open('posts_replied_to.txt', 'w') as f:
    for post_id in posts_replied_to:
        f.write(post_id + '\n')