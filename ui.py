import streamlit as st


from main import LeadsGenerator


# Function to display comments using Streamlit
def display_comments(comments_list):
    st.subheader("Comments: ")
    st.write("---")

    for comment in comments_list:
        st.write(f"**Username:** {comment['username']}")
        st.write(f"**Comment:** {comment['comment']}")
        st.write("---")


def display_data(data):
    for i, d in enumerate(data):
        st.markdown(f'### Cluster {i+1}')
        st.markdown('**The usernames are:** \n* ' + '\n* '.join(d['users']))
        st.markdown('**The things they are most interested in are:** \n* ' + '\n* '.join(d['keywords']))

# Main function to run the app
def main():

    leads_generator = LeadsGenerator()
    # Lead generator example template code
    st.title('Reddit Lead Generator')

    subreddit_name = st.text_input('Please enter the subreddit name:', 'web development')
    while " " in subreddit_name:
        subreddit_name = subreddit_name.replace(" ", "+")

    if st.button('Fetch Leads'):
        topic_links_list, users_and_comments, cluster_keywords_and_users = leads_generator(subreddit_name)

        with st.expander("Related subreddits: "):
            leads = topic_links_list
            st.write('Leads from r/{}:'.format(subreddit_name))
            for lead in leads:
                st.write(lead)
    
        with st.expander("Users and their Comments: "):
            display_comments(users_and_comments)
        
        display_data(cluster_keywords_and_users)

if __name__=="__main__":
    main()