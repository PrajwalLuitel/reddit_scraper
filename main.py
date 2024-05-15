from typing import Any
from topic_link_identifier import TopicLinkIdentifier
from src.scraper import Scraper
from src.keywords_and_clustering import KeywordsIdentifier, UserClustering


class LeadsGenerator:
    def __init__(self) -> None:
        pass

    def __call__(self,topic) -> Any:
        # Firstly, identify the subreddit links related to the user provided topic
        topic_links_list = TopicLinkIdentifier()(topic)
        
        # Now for each link in the list, the users and their comments are to be captured
        topic_urls = [topic['url'] for topic in topic_links_list]

        comments_getter = Scraper()

        users_and_comments = []

        for url in topic_urls:
            users_and_comments += comments_getter(url)
        
        # Now, Keywords from the comments are to be identified and users are to be clustered based upon their comments
        keywords = KeywordsIdentifier()([comment['comment'] for comment in users_and_comments], 70)

        clusters, user_clusters = UserClustering()(users_and_comments, 10, keywords)



