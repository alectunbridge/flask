from flask import (
    Flask,
    render_template,
    request,
    Response)

import requests
from OSGridConverter import latlong2grid


# Create the application instance
app = Flask(__name__, template_folder="templates")


# Create a URL route in our application for "/"
@app.route('/')
def home():
    resp = Response(response=render_template('home.json', gridRef=convert(request.args.get('latitude'), request.args.get('longitude'))),
                    status=200,
                    mimetype="application/json")
    return resp


def convert(latitude, longitude):
    grid = latlong2grid(float(latitude), float(longitude))

    return str(grid)[0:2] + str(grid.E)[1:-2] + str(grid.N)[1:-2]


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
