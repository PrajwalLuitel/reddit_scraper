from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

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

        user_clusters = zip(usernames,model.labels_)
        return cluster_keywords, user_clusters


# comments_list = [
#     {'username':'user1', 'comment':'I love reading books about space and astronomy.'},
#     {'username':'user2', 'comment':'I am interested in cooking and trying out new recipes.'},
#     {'username':'user3', 'comment':'My hobbies include gardening and botany.'},
#     {'username':'user4', 'comment':'I am a tech enthusiast and love gadgets.'},
#     {'username':'user5', 'comment':'I enjoy outdoor activities like hiking and camping.'},
#     {'username':'user6', 'comment':'I am a movie buff and enjoy watching different genres.'},
#     {'username':'user7', 'comment':'I am into fashion and keep up with the latest trends.'},
#     {'username':'user8', 'comment':'I love playing and watching football.'},
#     {'username':'user9', 'comment':'I am a music lover and play the guitar.'},
#     {'username':'user10', 'comment':'I enjoy painting and visiting art galleries.'},
#     {'username':'user11', 'comment':'I love traveling and exploring new places.'},
#     {'username':'user12', 'comment':'I am interested in learning about history and ancient civilizations.'},
#     {'username':'user13', 'comment':'I enjoy doing DIY projects and crafts.'},
#     {'username':'user14', 'comment':'I am a fitness enthusiast and enjoy working out.'},
#     {'username':'user15', 'comment':'I love animals and enjoy learning about wildlife.'},
#     {'username':'user16', 'comment':'I am passionate about photography and love capturing moments.'},
#     {'username':'user17', 'comment':'I am a foodie and love trying out different cuisines.'},
#     {'username':'user18', 'comment':'I love reading novels, especially mystery and thriller genres.'},
#     {'username':'user19', 'comment':'I am a car enthusiast and love learning about different models.'},
#     {'username':'user20', 'comment':'I enjoy playing video games in my free time.'},
#     {'username':'user21', 'comment':'I am a nature lover and enjoy bird watching.'},
#     {'username':'user22', 'comment':'I love dancing and am learning salsa.'},
#     {'username':'user23', 'comment':'I am interested in politics and like to keep up with current affairs.'},
#     {'username':'user24', 'comment':'I enjoy baking and love making pastries.'},
#     {'username':'user25', 'comment':'I am a science enthusiast and love learning about new discoveries.'},
#     {'username':'user26', 'comment':'I love writing and aspire to publish my own book someday.'},
#     {'username':'user27', 'comment':'I am a sports fan and enjoy watching basketball.'},
#     {'username':'user28', 'comment':'I love listening to classical music and play the piano.'},
#     {'username':'user29', 'comment':'I am interested in sustainable living and practice zero waste.'},
#     {'username':'user30', 'comment':'I love studying languages and am currently learning Spanish.'},
#     {'username':'user31', 'comment':'I am a history buff and enjoy visiting museums.'},
#     {'username':'user32', 'comment':'I enjoy yoga and meditation for relaxation.'},
#     {'username':'user33', 'comment':'I am a bookworm and enjoy reading biographies.'},
#     {'username':'user34', 'comment':'I love watching documentaries, especially about nature and wildlife.'},
#     {'username':'user35', 'comment':'I am a tech geek and love coding.'},
#     {'username':'user36', 'comment':'I enjoy DIY crafts and love making handmade gifts.'},
#     {'username':'user37', 'comment':'I am a fitness enthusiast and love running.'},
#     {'username':'user38', 'comment':'I love watching theatre and enjoy musicals.'},
#     {'username':'user39', 'comment':'I am interested in astronomy and love stargazing.'},
#     {'username':'user40', 'comment':'I enjoy painting and love working with watercolors.'},
#     {'username':'user41', 'comment':'I am a movie buff and enjoy watching foreign films.'},
#     {'username':'user42', 'comment':'I love gardening and enjoy growing my own vegetables.'},
#     {'username':'user43', 'comment':'I am a music lover and enjoy playing the violin.'},
#     {'username':'user44', 'comment':'I love traveling and enjoy backpacking.'},
#     {'username':'user45', 'comment':'I am interested in fashion design and love creating my own clothes.'}
# ]


# # Identify keywords
# keywords = KeywordsIdentifier()([comment['comment'] for comment in comments_list], 70)
# print("Keywords:", keywords)

# # Cluster users
# clusters, user_clusters = UserClustering()(comments_list, 10, keywords)
# print("Clusters:", clusters)



# for el in user_clusters:
#     print(f"User and the cluster: {el}")