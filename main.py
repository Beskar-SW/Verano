from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from flask_session import Session
from flask_fontawesome import FontAwesome
from flask_wtf import FlaskForm

import pymongo
from bson.objectid import ObjectId

from dotenv import load_dotenv
import sys
import os
import re
import datetime
import uuid

from model import Model

if not load_dotenv():
    print("No se pudo cargar el archivo .env")
    sys.exit()

app = Flask(__name__)
bootstrap = Bootstrap(app)
fa = FontAwesome(app)

professors = [
    {
        'id': 1,
        'name': 'Severus Snape',
        'email': 'snape@hogwarts.edu',
        'password': 'snape123'
    },
    {
        'id': 2,
        'name': 'Minerva McGonagall',
        'email': 'mcgonagall@hogwarts.edu',
        'password': 'mcgonagall123'
    },
    {
        'id': 3,
        'name': 'Albus Dumbledore',
        'email': 'dumbledore@hogwarts.edu',
        'password': 'dumbledore123'
    },
    {
        'id': 4,
        'name': 'Pomona Sprout',
        'email': 'sprout@hogwarts.edu',
        'password': 'sprout123'
    },
    {
        'id': 5,
        'name': 'Remus Lupin',
        'email': 'lupin@hogwarts.edu',
        'password': 'lupin123'
    },
    {
        'id': 6,
        'name': 'Rubeus Hagrid',
        'email': 'hagrid@hogwarts.edu',
        'password': 'hagrid123'
    },
    {
        'id': 7,
        'name': 'Filius Flitwick',
        'email': 'flitwick@hogwarts.edu',
        'password': 'flitwick123'
    },
    {
        'id': 8,
        'name': 'Sybill Trelawney',
        'email': 'trelawney@hogwarts.edu',
        'password': 'trelawney123'
    },
    {
        'id': 9,
        'name': 'Horace Slughorn',
        'email': 'slughorn@hogwarts.edu',
        'password': 'slughorn123'
    },
    {
        'id': 10,
        'name': 'Gilderoy Lockhart',
        'email': 'lockhart@hogwarts.edu',
        'password': 'lockhart123'
    }
]

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_USE_SSL'] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

mail = Mail(app)
Session(app)

db = pymongo.MongoClient(os.getenv("MONGO_URI"))["Verano"]

@app.route('/')
def index():
    return redirect(url_for('profesores_login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    default = True
    if request.method == "POST":
        data = request.form
        email = data['email']
        password = data['password']
        estudiantes_collection = db["Estudiantes"]
        estudiante = estudiantes_collection.find_one({"correo": email})
    
        if estudiante and check_password_hash(estudiante['contraseña'], password):
            session["user"] = estudiante['_id']
            # Message("Nueva sesión iniciada", sender=os.getenv("MAIL_USERNAME"), recipients=[estudiante['correo']]).send(mail)
            msg = Message("Nueva sesión iniciada", sender=os.getenv("MAIL_USERNAME"), recipients=["johan.franco147@gmail.com"])
            msg.html = f"""
            <h1>Se ha iniciado sesión en su cuenta</h1>
            <p>Se ha iniciado sesión en su cuenta desde la dirección IP: <b>{request.remote_addr}</b></p>
            <ul>
                <li>Info: <b>{request.user_agent}</b></li>
                <li>Fecha: <b>{datetime.datetime.now()}</b></li>
            </ul>
            <p>Si no ha iniciado sesión, por favor, contactenos en el siguiente correo: {os.getenv("MAIL_USERNAME")}<b>
            <p>Si usted ha iniciado sesión, ignore este mensaje</p>
            <p>Atentamente, el equipo de Verano</p>
            """
            mail.send(msg)
            flash("Logged in successfully!", category='success')
            return redirect(url_for('user', user=estudiante['_id']))
        else:
            return redirect(url_for('login'))

    elif request.method == "GET":
        return render_template('login.html', default=default)
    
@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for('index'))

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    default = False
    if request.method == "POST":
        data = request.form
        print(data)
        nombre = data.get('fullName', "")
        correo = data.get('email', "")
        contraseña = data.get('password', "")
        confirmar_contraseña = data.get('confirmPassword', "")
        nc = data.get('studentNumber', "")
        carrera = "ISC"

        if re.match(r'^\w+([.-]?\w+)*@itz.edu.mx$', correo) is None:
            return redirect(url_for('registro'))
        
        if re.match( r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,}$', contraseña) is None:
            return redirect(url_for('registro'))
        
        if re.match(r'^[0-9]{8}$', nc) is None:
            return redirect(url_for('registro'))
        
        if contraseña != confirmar_contraseña:
            return redirect(url_for('registro'))

        estudiante = {
            "nombre": nombre,
            "correo": correo,
            "contraseña": generate_password_hash(contraseña),
            "nc": nc,
            "carrera": carrera
        }
        estudiantes_collection = db["Estudiantes"]

        if estudiantes_collection.find_one({"correo": correo}) is not None:
            # print(estudiantes_collection.find_one({"correo": correo}))
            print("\033[33mCorreo ya registrado\033[0m")
            return redirect(url_for('registro'))

        estudiantes_collection.insert_one(estudiante)

        return redirect(url_for('login'))
    
    elif request.method == "GET":
        return render_template('login.html', default=default)

@app.route('/user/<user>')
def user(user):

    if str(session.get("user")) == user:
        estudiantes_collection = db["Estudiantes"]
        estudiante = estudiantes_collection.find_one({"_id": session.get("user")})
        return render_template('user.html', estudiante=estudiante, profesores=professors)
    else:
        return redirect(url_for('login'))

@app.route('/documents', methods=['POST'])
def documents():
    document = request.files.get('file', "")
    profesor = request.form.get('profesor', "")
    proyecto = request.form.get('proyecto', "")
    idStudent = session.get("user")
    saveAs = str(idStudent) + "_" + str(uuid.uuid4()) + "_" + document.filename
    document.save(os.path.join(os.path.dirname(__file__), 'static', 'documents', saveAs))
    estudiante_profesor_collection = db["Estudiante_Profesor"]
    estudiante_profesor_collection.insert_one({
        "estudiante": session.get("user"),
        "profesor": profesor,
        "documento": document.filename,
        "proyecto": proyecto,
        "path": saveAs,
        "status": "Pendiente"
    })

    return redirect(url_for('user', user=session.get("user")))

@app.route('/profesores')
def profesores():
    return redirect(url_for('profesores_login'))

@app.route('/profesores/login', methods=['GET', 'POST'])
def profesores_login():
    if request.method == "POST":
        data = request.form
        email = data['email']
        password = data['password']
        # profesores_collection = db["Profesores"]
        profesor = [x for x in professors if x['email'] == email and x['password'] == password]
        if profesor != []:
            session["profesor"] = profesor[0]['id']
            return redirect(url_for('profesores_user', profesor=profesor[0]['id']))
            
        else:
            return redirect(url_for('profesores'))

    elif request.method == "GET":
        return render_template('login2.html')

@app.route('/profesores/logout')
def profesores_logout():
    session.pop("profesor", None)
    return redirect(url_for('profesores'))

@app.route('/profesores/<profesor>', methods=['GET', 'POST'])
def profesores_user(profesor):
    if request.method == "GET":
        if str(session.get("profesor")) == profesor:
            estudiantes_profesores_collection = db["Estudiante_Profesor"]
            list_est_prof = estudiantes_profesores_collection.find({"profesor": str(session.get("profesor"))})
            students = db["Estudiantes"]
            profesor = [x for x in professors if x['id'] == int(session.get("profesor"))][0]
            data = []
            for x in list_est_prof:
                student = students.find_one({"_id": x["estudiante"]})
                document = x
                data.append({
                    "student": student,
                    "document": document
                })
            return render_template('profesores.html', profesor=profesor, data=data)
        else:
            return redirect(url_for('profesores_login'))
    elif request.method == "POST":
        search = request.form.get('search', "")
        estudiantes_profesores_collection = db["Estudiante_Profesor"]
        search_pattern = f".*{re.escape(search)}.*"
        list_est_prof = estudiantes_profesores_collection.find({"profesor": str(session.get("profesor")), "proyecto": {"$regex": search_pattern, "$options": "i"}})
        students = db["Estudiantes"]
        profesor = [x for x in professors if x['id'] == int(session.get("profesor"))][0] #Encontrar el profesor
        data = []
        for x in list_est_prof:
            student = students.find_one({"_id": x["estudiante"]})
            document = x
            data.append({
                "student": student,
                "document": document
            })

        return render_template('profesores.html', profesor=profesor, data=data)

@app.route('/download/<document>')
def profesores_document(document):
    if os.path.isfile(os.path.join(os.path.dirname(__file__), 'static', 'documents', document)):
        return send_from_directory(os.path.join(os.path.dirname(__file__), 'static', 'documents'), document, as_attachment=True)
    else:
        return redirect(url_for('profesores_user', profesor=session.get("profesor")))

@app.route('/actualizar', methods=['POST'])
def actualizar():
    print(request.form)
    id = request.form.get('id', "")
    nombre = request.form.get('nombre', "")
    nc = request.form.get('nc', "")
    carrera = request.form.get('carrera', "")
    email = request.form.get('email', "")
    telefono = request.form.get('telefono', "")
    proyecto = request.form.get('proyecto', "")
    status = request.form.get('status', "")
    fecha = request.form.get('fecha', "")
    comentarios = request.form.get('comentarios', "")

    estudiantes_profesores_collection = db["Estudiante_Profesor"]
    estudiantes_profesores_collection.update_one({"_id": ObjectId(id)}, {"$set": {"status": status, "fecha": fecha, "comentarios": comentarios, "proyecto": proyecto}})

    estudiante = db["Estudiantes"]
    estudiante.update_one({"nc": nc}, {"$set": {"nombre": nombre, "correo": email, "telefono": telefono, "carrera": carrera}})

    return redirect(url_for('profesores_user', profesor=session.get("profesor")))

@app.route('/resumen', methods=['POST'])
def resumen():
    id = request.json['id']
    per = 0.3
    estudiantes_profesores_collection = db["Estudiante_Profesor"]
    estudiante_profesor = estudiantes_profesores_collection.find_one({"_id": ObjectId(id)})
    model = Model(os.path.join(os.path.dirname(__file__), 'static', 'documents', estudiante_profesor['path']), float(per))
    summary = model.summarize()
    return jsonify(summary)


if __name__ == '__main__':
    import os
    server_crt = os.path.join(os.path.dirname(__file__), 'server.crt')
    server_key = os.path.join(os.path.dirname(__file__), 'server.key')
    app.run(host='0.0.0.0',debug=True, ssl_context=(server_crt, server_key))