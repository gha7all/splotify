from splotify import app
from flask import render_template
import json
import plotly
import plotly.express as px
import pandas as pd
import json


colors = px.colors.qualitative.Pastel

with open('splotify/dataset/StreamingHistory0.json') as json_file:
    dict_json = json.load(json_file)
history = pd.DataFrame.from_dict(dict_json, orient='columns')
history.reset_index(level=0, inplace=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/top_artists')
def top_artists():
    top_artists_df = history.groupby(['artistName'], as_index=False).agg(
        {'trackName': 'count'}).sort_values(by='trackName', ascending=False).head(11)

    fig = px.bar(top_artists_df, x=top_artists_df['artistName'], y=top_artists_df['trackName'], labels={
                 'artistName': 'Artist', 'trackName': 'Times listened'}, color_continuous_scale=colors[2])

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('top_artists.html', graphJSON=graphJSON)


@app.route('/artists')
def artists():
    artists_df = history.groupby(['artistName'], as_index=False).agg(
        {'trackName': 'count'}).sort_values(by='trackName', ascending=False).head(11)

    artists_names = list(artists_df['artistName'])
    return render_template('artists_list.html', artists_names=artists_names)


@app.route('/tracks/<name>', methods=['GET'])
def tracks(name):
    tracks = list(history[history['artistName'] == name]['trackName'].unique())
    return render_template('tracks.html', name=name, tracks=tracks)


@app.route('/top_tracks')
@app.route('/top_tracks/')
def top_tracks():
    top_tracks_df = history.groupby(['trackName'], as_index=False).size(
    ).sort_values(by='size', ascending=False).head(10)

    fig = px.pie(top_tracks_df,
                 names=top_tracks_df['trackName'], values=top_tracks_df['size'], color_discrete_sequence=colors[0:10])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('top_tracks.html', graphJSON=graphJSON)


@app.route('/listening_activity/')
def listening_activity():
    history['secPlayed'] = history['msPlayed']/1000
    history['endTime'] = pd.to_datetime(history['endTime'])
    history['date'] = history['endTime'].dt.date
    history['time'] = history['endTime'].dt.time
    history['hour'] = history['endTime'].dt.hour

    avg_per_day = history.groupby(['date'], as_index=False)[
        'secPlayed'].agg({'avgPlayed': 'mean'})

    fig = px.line(
        x=avg_per_day['date'], y=avg_per_day['avgPlayed'])
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Average Time Of Listening (Second)')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('listening_activity.html', graphJSON=graphJSON)
