from plotify import app
from flask import render_template, abort
import json
import plotly
import plotly.express as px
import pandas as pd
import json


colors = px.colors.qualitative.Plotly


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/top_artists')
def top_artists():
    with open('plotify/dataset/StreamingHistory0.json') as json_file:
        dict_json = json.load(json_file)
    history = pd.DataFrame.from_dict(dict_json, orient='columns')
    history.reset_index(level=0, inplace=True)

    df = history.groupby(['artistName'], as_index=False).agg(
        {'trackName': 'count'}).sort_values(by='trackName', ascending=False).head(11)

    fig = px.bar(df, x=df['artistName'], y=df['trackName'], labels={
                 'artistName': 'Artist', 'trackName': 'Times listened'}, color_discrete_sequence=colors[2:4])

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = 'My Top Artists'
    description = ''

    return render_template('top_artists.html', graphJSON=graphJSON, header=header, description=description)


@app.route('/artists')
def artists():
    with open('plotify/dataset/StreamingHistory0.json') as json_file:
        dict_json = json.load(json_file)
    history = pd.DataFrame.from_dict(dict_json, orient='columns')
    history.reset_index(level=0, inplace=True)
    df = history.groupby(['artistName'], as_index=False).agg(
        {'trackName': 'count'}).sort_values(by='trackName', ascending=False).head(11)

    artists_names = list(df['artistName'])
    return render_template('artists_list.html', artists_names=artists_names)


@app.route('/top_tracks/<name>', methods=['GET'])
def top_tracks(name):
    with open('plotify/dataset/StreamingHistory0.json') as json_file:
        dict_json = json.load(json_file)
    history = pd.DataFrame.from_dict(dict_json, orient='columns')
    history.reset_index(level=0, inplace=True)

    tracks = list(history[history['artistName'] == name]['trackName'].unique())
    return render_template('top_tracks.html', name=name, tracks=tracks)
