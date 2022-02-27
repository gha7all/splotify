import datetime
import requests
from requests.api import head
import spotipy
import pandas as pd
import spotipy.util as util
import json
from config import *


def get_token(user, client_id, client_secret, redirect_uri, scope):

    token = util.prompt_for_user_token(
        user, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

    return token


def get_streamings(path):
    with open(path, 'r', encoding='UTF-8') as json_file:
        dict_json = json.load(json_file)
    history = pd.DataFrame.from_dict(dict_json, orient='columns')
    history.reset_index(level=0, inplace=True)

    return history


def get_id(track_info, token, artist):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer ' + token,
    }
    track_name = track_info.split('___')[0]
    params = [('q', track_name), ('type', 'track')]
    artist = track_info.split('___')[-1]
    if artist:
        params.append(('artist', artist))

    try:
        response = requests.get(
            'https://api.spotify.com/v1/search', headers=headers, params=params, timeout=5)
        json = response.json()
        first_result = json['tracks']['items'][0]
        results = json['tracks']['items']

        if artist:
            for result in results:
                if artist.strip() == result['artists'][0]['name'].strip():
                    track_id = result['id']
        track_id = first_result['id']

        return track_id
    except:
        return None


def get_features(track_id, token):
    sp = spotipy.Spotify(auth=token)
    try:
        features = sp.audio_features([track_id])
        return features[0]
    except:
        return None


def append_features(token):
    streamings = get_streamings(path)
    unique_tracks = streamings.drop_duplicates(
        subset=['trackName', 'artistName'], keep='first')

    all_features = {}
    for track in unique_tracks['trackName']:
        artist = unique_tracks.loc[unique_tracks['trackName']
                                   == track, 'artistName'].values[0]
        track_id = get_id(track, token, artist)
        features = get_features(track_id, token)
        if features:
            all_features[track] = features

    final_features = []
    for track_name, features in all_features.items():
        final_features.append({'name': track_name, **features})

    history_features = pd.DataFrame(final_features)
    return history_features


token = get_token(user=user, client_id=client_id,
                  client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

df = append_features(token)
df.to_csv('streaming_audio_features_new.csv')