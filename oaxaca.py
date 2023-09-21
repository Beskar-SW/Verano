from flask import Flask, request, session, jsonify, redirect, url_for
import pymongo
import googlemaps
from flask_cors import CORS, cross_origin
import RecomendacionLugares
import RecomendacionPopularidad
import redis

app = Flask(__name__)

# Allow access from all origins (not recommended for production)
CORS(app)

gmaps = googlemaps.Client(key='AIzaSyCNxskQfyk-DlciRoujJdSohkctZ73BSBA')
db = pymongo.MongoClient("mongodb+srv://mongoroot:mongopass999@mongodb-cluster.c7fujla.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")["App"]

@app.route("/login", methods=["POST"])
def index():
    data = request.json
    usuario = data["usuario"]
    password = data["password"]

    collection = db["usuarios"]
    usuario = collection.find_one({"usuario": usuario, "password": password})

    if usuario:
        session["usuario"] = usuario["usuario"]
        return jsonify({"status": "success"}), 200, {'Access-Control-Allow-Origin': '*'}
    else:
        return jsonify({"status": "failed"}), 401, {'Access-Control-Allow-Origin': '*'}

@cross_origin()
@app.route('/search_place', methods=['POST'])
def search_place():

    data = request.json
    print(data)
    lat = data["lat"]
    lng = data["lng"]
    keyword = data["keyword"]

    session["lat"] = lat
    session["lng"] = lng

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

@cross_origin()
@app.route('/recomendaciones', methods=['POST'])
def recomendaciones():

    recomendacion = RecomendacionLugares.RecomendacionLugares()
    user = str(session.get("usuario"))
    
    boleano = recomendacion.client.exists(user)

    if not boleano:
        redirect(url_for('recomendaciones2'))

    recomendaciones_usuario = recomendacion.generar_recomendaciones(user, num_recomendaciones=5)

    lista = []
    for i in range(len(recomendaciones_usuario)):
        # get info from gmaps
        place_info = gmaps.find_place(
            input=recomendaciones_usuario[i],
            input_type="textquery",
            fields=['geometry', 'name', 'geometry/location/lng', 
            'geometry/location/lat', 'types', 'rating',
            "formatted_address"],
            language="es-MX",
            location_bias=f"""circle:5000@{session.get("lat")},{session.get("lng")}"""
        )

        place_info = place_info["candidates"][0]
        lista.append(place_info)

    return jsonify(lista), 200, {'Access-Control-Allow-Origin': '*'}
        
@cross_origin()
@app.route('/recomendaciones_new', methods=['POST'])
def recomendaciones2():
    recomendador = RecomendacionPopularidad.RecomendacionPopularidad()
    num_recomendaciones = 5
    recomendaciones = recomendador.recomendacion_popularidad(num_recomendaciones)
    recomendaciones = recomendador.recomendacion_popularidad_aleatoria(num_recomendaciones)
    
    lista = []
    for i in range(len(recomendaciones)):
        # get info from gmaps
        place_info = gmaps.find_place(
            input=recomendaciones[i],
            input_type="textquery",
            fields=['geometry', 'name', 'geometry/location/lng', 
            'geometry/location/lat', 'types', 'rating',
            "formatted_address"],
            language="es-MX",
            location_bias=f"""circle:5000@{session.get("lat")},{session.get("lng")}"""
        )

        place_info = place_info["candidates"][0]
        lista.append(place_info)

    return jsonify(lista), 200, {'Access-Control-Allow-Origin': '*'}


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)