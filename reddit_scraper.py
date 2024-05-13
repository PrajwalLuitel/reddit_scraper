import praw
import streamlit as st

# Initialize Praw with your Reddit credentials
reddit = praw.Reddit(
    client_id='2DtPhbSH-8UjkuhSSLA1Ng',
    client_secret='TV2Dt46SQQqSz3hEeIjMN2KdpWagqg',
    user_agent='ZestyclosePolicy9975'
)

# Function to scrape comments from a given subreddit link
def scrape_subreddit(subreddit_link):
    comments_list = []
    post_content = {}
    submission = reddit.submission(url=subreddit_link)
    
    post_content['title'] = submission.title
    post_content['score'] = submission.score
    post_content['body'] = submission.selftext

    # Assuming you want to scrape top-level comments only
    submission.comments.replace_more(limit=0)  # This line removes MoreComments objects
    for comment in submission.comments.list():
        comments_list.append({'username': comment.author.name, 'comment': comment.body})
    
    return post_content, comments_list

# Function to display comments using Streamlit
def display_comments(post_content, comments_list):
    st.subheader("Post: ")
    st.write(f"**Post Title:** {post_content['title']}")
    st.write(f"**Score:** {post_content['score']}")
    st.write(f"**Post Body:** {post_content['body']}")
    st.write("---")  # Separator line for post content
    st.subheader("Comments: ")
    st.write("---")

    for comment in comments_list:
        st.write(f"**Username:** {comment['username']}")
        st.write(f"**Comment:** {comment['comment']}")
        st.write("---")

# Main function to run the app
def main():
    st.title('Reddit Comments Scraper')
    
    # Input area for subreddit link
    subreddit_link = st.text_input('Enter the subreddit link:')
    
    if st.button('Scrape Comments'):
        if subreddit_link:
            post_content, comments_list = scrape_subreddit(subreddit_link)
            display_comments(post_content, comments_list)
        else:
            st.write("Please enter a valid subreddit link.")

if __name__ == "__main__":
    main()
