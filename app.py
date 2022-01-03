from flask import Flask, render_template
import json
import plotly
import plotly.express as px
import pandas as pd
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/top_artists')
def top_artists():
   with open('dataset/StreamingHistory0.json') as json_file:
      dict_json = json.load(json_file)
   history = pd.DataFrame.from_dict(dict_json, orient='columns')
   history.reset_index(level=0, inplace=True)

   df = history.groupby(['artistName'], as_index=False).agg(
       {'trackName': 'count'}).sort_values(by='trackName', ascending=False).head(11)

   fig = px.bar(df, x=df['artistName'], y=df['trackName'])

   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   header = 'Fruits in north america'
   description = 'ghazal ghazal made an app'

   return render_template('top_artists.html', graphJSON=graphJSON, header=header, description=description)


#  @app.route('/piechart')
#  def piechart():
#     return render_template('piechart.html', graphJSON=graphJSON, header=header, description=description)


# if __name__ == '__main__':
#     app.run_server(debug=True)
