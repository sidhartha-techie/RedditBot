import praw
import pdb
import re
import os
import time

var_context_praw = None #replace None with the context name in praw.ini file
var_subreddit == None #replace None with the subreddit name

reddit = praw.Reddit(var_context_praw)
subreddit = reddit.subreddit(var_subreddit)

#following code checks for submissions in the sureddit, use this for test, otherwise comment these out
for submission in subreddit.new(limit=10):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
    

if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []
else:
    with open("comments_replied_to.txt", "r") as f:
       comments_replied_to = f.read()
       comments_replied_to = comments_replied_to.split("\n")
       comments_replied_to = list(filter(None, comments_replied_to))


#for submission in subreddit.hot(limit=5):
#    #print(submission.title)
#

def start_magic():
    while True:
        print("here")
        try:
            comment_stream = subreddit.stream.comments(skip_existing=True)
            for comment in comment_stream:
                if comment.id not in comments_replied_to:
                    #your logic
                    comment.reply("comment bot")
                    print("Bot replying to : ", comment.body)
        except Exception as e:
            print(e)
            time.sleep(9)
            continue
start_magic()

# Write our updated list back to the file
with open("comments_replied_to.txt", "w") as f:
    for post_id in comments_replied_to:
        f.write(post_id + "\n")