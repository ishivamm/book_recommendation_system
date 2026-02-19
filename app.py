import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

# ---------------------------
# Load Files
# ---------------------------

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

# ---------------------------
# Page Config
# ---------------------------

st.set_page_config(page_title="Book Recommender System", layout="wide")

st.title("📚 Book Recommender System")
st.write("Get personalized book recommendations!")

# ---------------------------
# Recommendation Function
# ---------------------------

def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    data = []

    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    return data

# ---------------------------
# Sidebar
# ---------------------------

st.sidebar.title("Navigation")
option = st.sidebar.radio("Select Option", ["Popular Books", "Recommend"])

# ---------------------------
# Popular Books Section
# ---------------------------

if option == "Popular Books":
    st.header("🔥 Top 50 Popular Books")

    cols = st.columns(5)

    for i in range(min(50, len(popular_df))):
        row = popular_df.iloc[i]   # ✅ position-based indexing

        with cols[i % 5]:
            st.image(row['Image-URL-M'])
            st.markdown(f"**{row['Book-Title']}**")
            st.caption(f"Author: {row['Book-Author']}")
            st.caption(f"Votes: {row['num_ratings']}")
            st.caption(f"Rating: {round(row['avg_rating'],2)}")


# ---------------------------
# Recommendation Section
# ---------------------------

if option == "Recommend":
    st.header("📖 Get Book Recommendations")

    selected_book = st.selectbox(
        "Type or Select a Book",
        pt.index.values
    )

    if st.button("Recommend"):
        recommendations = recommend(selected_book)

        cols = st.columns(5)

        for idx, book in enumerate(recommendations):
            with cols[idx]:
                st.image(book[2])
                st.markdown(f"**{book[0]}**")
                st.caption(f"Author: {book[1]}")
