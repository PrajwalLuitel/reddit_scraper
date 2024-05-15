from typing import Any
from src.topic_link_identifier import TopicLinkIdentifier
from src.scraper import Scraper
from src.keywords_and_clustering import KeywordsIdentifier, UserClustering


class LeadsGenerator:
    def __call__(self,topic) -> Any:
        # Firstly, identify the subreddit links related to the user provided topic
        topic_links_list = TopicLinkIdentifier()(topic)
        
        # Now for each link in the list, the users and their comments are to be captured
        topic_urls = [topic['url'] for topic in topic_links_list]

        # Initializing the comments getter class
        comments_getter = Scraper()
        # A list to store users and their comments
        users_and_comments = []

        # Iterating to store the urls from the topics
        for url in topic_urls:
            try:
                users_and_comments += comments_getter(url)
            except Exception:
                pass

        # Now, Keywords from the comments are to be identified and users are to be clustered based upon their comments
        try:
            all_comments = [comment['comment'] for comment in users_and_comments]
        except KeyError:
            pass
        
        keywords = KeywordsIdentifier()(all_comments, len(all_comments)*5)

        clusters, user_clusters = UserClustering()(users_and_comments, len(keywords)*0.05, keywords)


        # Iterate over each cluster and store the data in the format as below:
        """
        [
        {'keywords':['kw1', 'kw2'], 'users':['user1','user3']},
        {'keywords':['kw3', 'kw4'], 'users':['user2','user5']},
        {'keywords':['kw5', 'kw6'], 'users':['user4']},
        ]
        """
        cluster_users = [[] for _ in clusters]
        for user, cluster_idx in user_clusters:
            cluster_users[cluster_idx].append(user)
        cluster_keywords_and_users = [{'keywords': clusters[i], 'users': cluster_users[i]} for i in range(len(clusters))]


        return topic_links_list, users_and_comments, cluster_keywords_and_users
        
