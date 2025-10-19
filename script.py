'''
import streamlit as st
import requests

# Title
st.title("My First Streamlit App")

# Simple text
st.write("This app fetches data from the web!")

# Add a button
if st.button("Get Random Fact"):
    # Fetch data from a free API
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    data = response.json()
    st.success(data["text"])

# Input field
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! 👋")

# Display some data
st.subheader("Quick Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.write("---")
st.caption("Built with Streamlit")


'''

import streamlit as st
import pandas as pd
import praw

st.set_page_config(page_title="Reddit Demo", layout="wide")
st.title("Reddit Scraper (Streamlit + PRAW)")

# Read secrets
creds = st.secrets["reddit"]
reddit = praw.Reddit(
    client_id=creds["client_id"],
    client_secret=creds["client_secret"],
    username=creds["username"],
    password=creds["password"],
    user_agent=creds["user_agent"],
)

@st.cache_data(ttl=300)
def fetch_posts(subreddit_name: str, limit: int = 25):
    sub = reddit.subreddit(subreddit_name)
    rows = []
    for s in sub.hot(limit=limit):
        rows.append({
            "id": s.id,
            "title": s.title,
            "score": s.score,
            "num_comments": s.num_comments,
            "url": s.url,
            "created_utc": s.created_utc,
            "author": str(s.author),
        })
    return pd.DataFrame(rows)

col1, col2 = st.columns([1,2])
with col1:
    sub_name = st.text_input("Subreddit", value="technology")
    limit = st.slider("How many posts?", 5, 100, 25)
    go = st.button("Fetch")

if go:
    try:
        df = fetch_posts(sub_name, limit)
        st.success(f"Fetched {len(df)} posts from r/{sub_name}")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error: {e}")
        st.code(str(e))


