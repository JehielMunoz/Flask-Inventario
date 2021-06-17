import firebase_admin
from firebase_admin import db,credentials
from flask import Flask, render_template, request
import pyrebase
from werkzeug.utils import redirect

app = Flask(__name__)

cred = credentials.Certificate('key.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://proyectoi-invedu-default-rtdb.firebaseio.com/'
    })
database = db.reference('/')


@app.route('/', methods=['GET','POST'])
def index():
    # if request.method == 'POST' :
    # name = request.form.get("form")
    # db.child("19176913-9").push(name)
    # te = []
    provs = database.child("proveedores").get()
    if provs is None:
        return render_template("index.html")
    else:
        return render_template("index.html", t=provs)


@app.route('/addItem.html', methods=['GET','POST'])
def addItem():
    if request.method == 'POST':
        especie = request.form["especie"]
        estado = request.form["estado"]
        precio_unitario = request.form["precio_unitario"]
        precio_total = request.form["precio_total"]
        fecha_recepcion = request.form["fecha_recepcion"]
        numero_factura = request.form["numero_factura"]
        rut_proveedor = request.form["rut_proveedor"]
        centro_de_costo = request.form["centro_de_costo"]
        ubicacion_actual = request.form["ubicacion_actual"]
        observaciones = request.form["observaciones"]
        codigo_barra = request.form["codigo_barra"]

        item = {
            "codigo_correlativo": 1003,
            "especie":  especie,
            "estado":   estado,
            "precio_unitario":  precio_unitario,
            "precio_total": precio_total,
            "fecha_recepcion":  fecha_recepcion,
            "numero_factura":   numero_factura,
            "rut_proveedor":    rut_proveedor,
            "centro_de_costo":  centro_de_costo,
            "ubicacion_actual": ubicacion_actual,
            "observaciones":    observaciones,
            "codigo_barra": codigo_barra
        }
        try:
            database = db.reference('/')
            database = database.child("data").child("especies")
            database.push({"1003": item})
            print(item)
            # database.child("data").child("especies").child(str(last_code)).push(item)
            # database.child(last_code).patch(item)
            return redirect("/")
        except:
            return render_template("addItem.html", message="Something wrong happened")
    return render_template("addItem.html")
if __name__ == '__main__':
    app.run(debug=True)
"""
:
    last_code = len(database.child("data").child("especies").get())
    # maxId = len(lastCod)
    # lastCod = database.child("data").child("especies").child(str(maxId)).get()
    return render_template("addItem.html", cod=last_code)


@app.route('/addItem.html', methods=['GET','POST'])
def createItem():
"""