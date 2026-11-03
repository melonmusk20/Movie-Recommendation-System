import streamlit as st
import pandas as pd
import requests
import pickle
import os

# Load movie data + similarity matrix
@st.cache_resource
def load_data():
    with open('movie_data.pkl', 'rb') as file:
        return pickle.load(file)


movies, cosine_sim = load_data()


# ------------------------- RECOMMENDATION FUNCTION -------------------------

def get_recommendations(title, cosine_sim=cosine_sim):
    matches = movies[movies['title'] == title]
    if matches.empty:
        return pd.DataFrame(columns=['title', 'movie_id'])

    idx = matches.index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    indices = [i[0] for i in sim_scores]

    return movies[['title', 'movie_id']].iloc[indices]


# ------------------------- POSTER FETCH FUNCTION -------------------------

def get_api_key():
    try:
        return st.secrets["TMDB_API_KEY"]
    except Exception:
        return os.environ.get("TMDB_API_KEY", "")


@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    api_key = get_api_key()
    if not api_key:
        return "https://via.placeholder.com/500x750?text=No+API+Key"
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'

    try:
        response = requests.get(
            url, 
            timeout=5,
            headers={"User-Agent": "Mozilla/5.0"}   # Important for TMDB
        )
        response.raise_for_status()
        data = response.json()

        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching poster for ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error"


# ------------------------- STREAMLIT UI -------------------------

st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button('Recommend'):
    recommendations = get_recommendations(selected_movie)
    st.write("### Top 10 Recommended Movies")

    # Display posters in 2 rows × 5 columns
    for i in range(0, 10, 5):
        cols = st.columns(5)
        for col, j in zip(cols, range(i, i + 5)):
            if j < len(recommendations):
                movie_title = recommendations.iloc[j]['title']
                movie_id = recommendations.iloc[j]['movie_id']
                poster_url = fetch_poster(movie_id)

                with col:
                    st.image(poster_url, width=130)
                    st.write(movie_title)
