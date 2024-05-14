import streamlit as st

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


    # Lead generator example template code
    st.title('Reddit Lead Generator')

    subreddit_name = st.text_input('Enter the subreddit name:', 'web development')
    while " " in subreddit_name:
        subreddit_name = subreddit_name.replace(" ", "+")

    if st.button('Scrape Leads'):
        leads = scrape_subreddit(subreddit_name)
        st.write('Leads from r/{}:'.format(subreddit_name))
        for lead in leads:
            st.write(lead)