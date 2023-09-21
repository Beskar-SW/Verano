from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory, jsonify
import pymongo
import googlemaps
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# Allow access from all origins (not recommended for production)
CORS(app)

gmaps = googlemaps.Client(key='AIzaSyCNxskQfyk-DlciRoujJdSohkctZ73BSBA')

@app.route("/")
def index():
    return "Hola"

@app.route('/search_place', methods=['GET', 'POST'])
@cross_origin()
def search_place():

    data = request.json
    print(data)
    lat = data["lat"]
    lng = data["lng"]
    keyword = data["keyword"]

    # place_info = gmaps.find_place(
    #     input=keyword,
    #     input_type="textquery",
    #     fields=['geometry', 'name', 'geometry/location/lng', 
    #     'geometry/location/lat', 'types', 'rating',
    #     "formatted_address"],
    #     language="es-MX",
    #     location_bias=f"""circle:5000@{lat},{lng}"""
    # )

    place_info = gmaps.places(
        query=keyword,
        location=(lat,lng),
        radius=5000,
        language="es-MX"
    )

    place_info = place_info["results"]

    return jsonify(place_info), 200, {'Access-Control-Allow-Origin': '*'}


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)