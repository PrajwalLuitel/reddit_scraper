import praw

# local import
from keys import CLIENT_ID, CLIENT_SECRET, USER_AGENT



class Scraper:
    def __init__(self) -> None:
        # Reddit object initialized with praw
        self.reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT
            )

    def __call__(self, subreddit_link) -> tuple[dict, list]:
        # A list to store all the content of the comments
        comments_list = []

        try:
            submission = self.reddit.submission(url=subreddit_link)
        except Exception:
            pass

        # scraping only the top level comments from the subreddit
        submission.comments.replace_more(limit=0)
        # Creating a list of dictionaries for all the comments
        for comment in submission.comments.list():
            username = comment.author.name if comment.author else "N/A"
            comments_list.append({'username': username, 'comment': comment.body})
        
        # returning the post and the comments
        return comments_list
        
