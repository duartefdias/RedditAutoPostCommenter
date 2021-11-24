import datetime
import logging
import os
import praw

import azure.functions as func

def bot_login():
	print("Logging in...")

	r = praw.Reddit(username = os.environ["reddit_username"],
				password = os.environ["password"],
				client_id = os.environ["client_id"],
				client_secret = os.environ["client_secret"],
				user_agent = "RedditAutoPostCommenter")

	print("Logged in!")

	return r

def get_last_posts(r, subreddit, limit):
    subreddit = r.subreddit(subreddit)
    posts = subreddit.new(limit=limit)
    return posts

def add_comment_to_post(r, post, comment):
    post.reply(comment)

def check_if_comment_exists(r, post, comment):
    for comment in post.comments.list():
        if comment.body == comment:
            return True
    return False


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    # Create an instance of the Reddit API
    r = bot_login()

    # Get the last 10 posts from the subreddit
    posts = get_last_posts(r, os.environ["subreddit"], 100)

    # Loop through the posts
    for post in posts:
        # If the post is not a self post
        if not post.is_self:
            # If the post does not already have a comment
            if not check_if_comment_exists(r, post, os.environ["comment"]):
                # Upvote post
                post.upvote()
                # Add the comment
                add_comment_to_post(r, post, os.environ["comment"])
