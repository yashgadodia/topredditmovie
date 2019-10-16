#goal: get graph of top movies and number of upvotes from a certain post on reddit

#install virtual env instance in new folder
#1) pip install virtualenv
#create the virtual environment
# 2) virtualenv mypython
#activate the virtual environment
# 3) source mypython/bin/activate
#to deactivate, $deactivate

#now u can install any dependencies in this environment

#####check if python is linked? brew install python ,brew link python,
#brew link --overwrite python, brew info python

import praw
import pprint
import sys
import random
import time
import pandas as pd
import matplotlib.pyplot as plt


##print('praw version', praw.__version__)


#my reddit personal info
reddit = praw.Reddit(client_id  = '',
                     client_secret  =  '',
                     username  =  '',
                     password  =  '',
                     user_agent  =  '')

#hot_posts = reddit.subreddit('Machine Learning').hot(limit=10)
#for post in hot_posts:
#    print(post.title)

##submission = reddit.submission(url='https://www.reddit.com/r/funny/comments/3g1jfi/buttons/')
##submission.comments.replace_more(limit=0)
##for top_level_comment in submission.comments:
##    for second_level_comment in top_level_comment.replies:
##        print(second_level_comment.body)

# get hottest posts from all subreddits
##hot_posts = reddit.subreddit('all').hot(limit=10)
##for post in hot_posts:
##    print(post.title)

##posts = []
##askreddit = reddit.subreddit('AskReddit')
##for post in askreddit.hot(limit = 10):
##    posts.append([post.title, post.score, post.id, post.subreddit, post.url,
##                 post.num_comments, post.selftext, post.created])
##posts = pd.DataFrame(posts, columns= ['title', 'score', 'id', 'subreddit',
##                                      'url', 'num_comments', 'body', 'created'])
####print(posts)
##
##posts.plot(kind = 'bar', x = 'score', y = 'num_comments', color = 'red')
####plt.show()

submission = reddit.submission(id='bzb6rn')
elemlist = []
submission.comments.replace_more(limit=0) #removes more comments objects from the forest
for top_level_comment in submission.comments:       
##        print(top_level_comment.body.split()[:4])
    elemlist.append([top_level_comment.body.split()[:4], top_level_comment.score])
    if len(elemlist) > 10:
        break
elemlist = pd.DataFrame(elemlist, columns = ['body', 'score'])

elemlist.plot(kind = 'bar', x = 'body', y = 'score', color = 'red')
plt.show()















##subreddit = reddit.subreddit('AskReddit')
####for submission in subreddit.top(limit=1):
####    print(submission.title, submission.id)
##topics_dict = { "title":[],
##                "score":[],
##                "id":[],
##                "url":[],
##                "comms_num": [],
##                "created": [],
##                "body":[] }
##
##top_subreddit = subreddit.top()
##for submission in top_subreddit:
##    topics_dict["title"].append(submission.title)
##    topics_dict["score"].append(submission.score)
##    topics_dict["id"].append(submission.id)
##    topics_dict["url"].append(submission.url)
##    topics_dict["comms_num"].append(submission.num_comments)
##    topics_dict["created"].append(submission.created)
##    topics_dict["body"].append(submission.selftext)
##
##topics_data = pd.DataFrame(topics_dict)
##
##print(topics_data)







