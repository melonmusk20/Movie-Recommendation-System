# Movie Recommendation System

This project is a movie recommendation system built with Streamlit and powered by a machine learning model. It recommends movies based on a selected title using cosine similarity and displays movie posters fetched from the TMDB API.

Display the top 10 recommendations based on your selected movie on Streamlit, with posters of the movies


Download the datasets from here: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

PKL file for reference: https://drive.google.com/file/d/1wcVhYPEsU1iTp4ZUmjQZW2T9EAbleMyB/view?usp=sharing


# Overview

The movie recommendation system helps users discover movies similar to their favorites. By selecting a movie from the list, users receive a list of the top 10 recommended movies along with their posters. This project leverages machine learning techniques to analyze the features of movies and find similarities between them. It uses the TMDB API to fetch and display movie posters, enhancing the user experience by providing visual context for the recommendations. The system is built with Streamlit, providing an interactive and user-friendly interface for users to explore movie recommendations easily.


# Usage

Run the Streamlit app:

streamlit run app.py
Open your web browser and go to http://localhost:8501.

Select a movie from the dropdown list and click "Recommend" to get the top 10 recommended movies along with their posters

# Model

The dataset used for this project contains information about movies, including their titles and IDs. It is processed and stored in movie_data.pkl . The dataset is used to calculate the cosine similarity between movies. The model for recommending movies is based on cosine similarity. Cosine similarity is used to measure the similarity between movie titles. The model computes the similarity scores and suggests the top 10 similar movies based on the selected movie title.

# Results

The system provides the top 10 recommended movies for any selected movie title. It also fetches and displays the posters of these recommended movies using the TMDB API.

<img width="595" height="842" alt="image" src="https://github.com/user-attachments/assets/5ed54c1c-8833-468d-a3dc-1554b3e08a04" />




