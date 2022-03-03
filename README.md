# Plotify
<b>Plotting spotify personal data using plotly.</b>

## What is Plotlify?
Ever wanted to know more about your listening activities on spotify? Your most listened tracks, favorite artists, etc? Well, it's so true that spotify itself gives you a summery at the end of the year, but I couldn't wait till the end of the year. Plotify is a micro web application that shows you your listening activities, favorite artists, most listened tracks and also your mood based of the songs you listen to.

First, You have to have the json file which spotify gives you after making a request, then plotify gets each song's audio analysis and plots your mood.

This [article](https://support.spotify.com/us/article/data-rights-and-privacy-settings/) shows you how you can get your spotify personal data.

## How can you personalize Plotify?
Simply by replacing <i> StreamingHistory0.json </i> with yours. Run streaming_history.py file to get audio features:
```
python streaming_history.py
```

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

