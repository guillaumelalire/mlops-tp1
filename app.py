import joblib
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get("/predict")
async def root(size: int, nb_bedrooms: int, garden: int):
    model = joblib.load('models/regression.joblib')
    return model.predict([[size, nb_bedrooms, garden]])[0]

@app.get("/predict_song")
async def song_prediction(song_name: str):
    song_list = pd.read_csv('data/song_list.csv')
    song_index = song_list[song_list['track_name'].str.lower() == song_name.lower()].index
    song_features = song_list[['track_popularity', 'track_album_release_date', 'energy', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']]

    model = joblib.load('models/music_knn.joblib')
    distances, neighbours = model.kneighbors(song_features.loc[song_index], 11, return_distance=True)
    
    music_recommendations = song_list.iloc[neighbours[0]][['track_name', 'track_artist']]
    
    return music_recommendations[1:].T