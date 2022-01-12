import datetime
import requests
from requests.api import head
import spotipy
import pandas as pd
import spotipy.util as util
import ast


def get_token(user, client_id, client_secret, redirect_url, scope):

    token = util.prompt_for_user_token(
        user, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_url)

    return token


def api_id(track_info, token, artist):
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
            'https://api.spotify.com/v1/search', headers=headers, timeout=5)
        json = response.json()
        results = json['tracks']['items']
        first_result = json['tracks']['items'][0]
        # check whether the found artist is the right one
        if artist:
            for result in results:
                if artist.strip() == result['artists'][0]['name'].strip():
                    track_id = result['id']
        track_id = first_result['id']
        return track_id

    except:
        return None
