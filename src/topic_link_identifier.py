import praw

# local import
from keys import CLIENT_ID, CLIENT_SECRET, USER_AGENT


class TopicLinkIdentifier:
    def __init__(self) -> None:
        self.reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT
        )


    def __call__(self, subreddit_name:str) -> list:
        try:
            # Initializing subreddit
            subreddit = self.reddit.subreddit(subreddit_name)
            # A list to store all the topics and the information
            topics = []
            for post in subreddit.hot(limit=30):  # Limit can be set to optimize the content
                # a dictionary to store information of a topic
                topic = {
                    'title': post.title,
                    'url': post.url,
                    'author': post.author.name,
                    'score': post.score
                }
                topics.append(topic)
        except Exception:
            # Error message for exception
            topics.append("Sorry!! Unable to fetch leads. . . . .   :( ")
        
        # returning the list of topics
        return topics
