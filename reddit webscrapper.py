import praw
import csv

reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent')

subreddit = reddit.subreddit('your_subreddit_name')
posts = subreddit.hot(limit=1000)

with open('reddit_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'score', 'num_comments']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for post in posts:
        writer.writerow({'title': post.title,
                         'score': post.score,
                         'num_comments': post.num_comments})
