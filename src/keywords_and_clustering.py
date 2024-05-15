from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
import nltk

import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download('stopwords')

class KeywordsIdentifier:
    def __call__(self, comments, num_keywords) -> Any:
        vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
        X = vectorizer.fit_transform(comments)
        keywords = vectorizer.get_feature_names_out()
        return keywords[:num_keywords]

class UserClustering:
    def __call__(self, user_comments, num_clusters, keywords) -> Any:
        usernames=[]
        comments=[]
        for comment_dict in user_comments:
            for key,value in comment_dict.items():
                if key=="username":
                    usernames.append(value)
                else:
                    comments.append(value)

        vectorizer = TfidfVectorizer(vocabulary=keywords, stop_words=stopwords.words('english'))
        X = vectorizer.fit_transform(comments)
        model = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=100, n_init=1)
        model.fit(X)
        order_centroids = model.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names_out()
        cluster_keywords = []
        for i in range(num_clusters):
            cluster_keywords.append([terms[ind] for ind in order_centroids[i, :10]])

        user_clusters = list(zip(usernames,model.labels_))
        return cluster_keywords, user_clusters

