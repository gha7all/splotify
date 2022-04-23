# [Splotify](https://s-plotify.herokuapp.com/)
<b> Plotting spotify straming history by using plotly. </b>


## What is Splotlify?
Ever wanted to know more about your listening activities on spotify? Your most listened tracks, favorite artists, etc? Splotify is a micro web application that shows you your listening activities, favorite artists, most listened tracks and also your mood based of the songs you listen to.

First, You have to have the json file which spotify gives you ter making a request, then Splotify gets each song's audio analysis and plots your mood.

This [article](https://support.spotify.com/us/article/data-rights-and-privacy-settings/) shows you how you can get your spotify personal data.

## How to personalize Splotify?

Go to [spotify developer's dashboard](https://developer.spotify.com/dashboard/applications) create an app and add your CLIENT_ID and CLIENT_SECRET in ./config.py.

Replace the  <i> StreamingHistory0.json </i> file with yours. Run streaming_history.py file to get audio features:
```
python streaming_history.py
```
It takes a while to run because that's where the app gets data from API.

 Then enable flask virtual environment and run these commands:
```
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```
## Dependencies
* Flask
* Pandas
* Plotly
* Spotipy

## Demo
![](https://github.com/gha7all/Images/blob/master/preview.gif)
