from flask import Flask

app = Flask(__name__, static_folder="assets/static")
app.url_map.strict_slashes = False

from splotify import routes