# import necessary libraries
import os
from flask import (
    Flask,
    json,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .models import Pet
#from  .models import Tours, Cities


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/bandmiles/<band>")
def bandmiles(band):
    # results = db.session.query(Pet.name, Pet.lat, Pet.lon).all()
    #result = db.session.query(Tours).all()

    # hover_text = [result[0] for result in results]
    # lat = [result[1] for result in results]
    # lon = [result[2] for result in results]

    # pet_data = [{
    #     "type": "scattergeo",
    #     "locationmode": "USA-states",
    #     "lat": lat,
    #     "lon": lon,
    #     "text": hover_text,
    #     "hoverinfo": "text",
    #     "marker": {
    #         "size": 15,
    #         "line": {
    #             "color": "rgb(8,8,8)",
    #             "width": 1
    #         },
    #     }
    # }]

    sample_data = [{
        'name': band,
        'date': '2021-07-17'
    }]

    return jsonify(sample_data)

@app.route("/api/bandyear/<band>/<year>")
def bandyearloc(band, year):

    output_data = [
        {
            'band': band,
            'year': year
        }
    ]
    return jsonify(output_data)




if __name__ == "__main__":
    app.run()
