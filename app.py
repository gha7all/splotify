from flask import Flask, render_template
import json
import plotly
import plotly.express as px
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chart_1')
def chart_1():
    df = pd.DataFrame({
        'Fruit': ['apples', 'oranges', 'bananas', 'apples', 'oranges', 'bananas'],
        'Amount': [4, 1, 2, 2, 4, 5],
        'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
    })

    fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = 'Fruits in north america'
    description = 'ghazal ghazal made an app'

    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


# if __name__ == '__main__':
#     app.run_server(debug=True)
