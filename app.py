import firebase_admin
from firebase_admin import db, credentials
from flask import Flask, render_template, request, current_app

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
    dbPath = db.reference('/')
    dbPath = dbPath.child("data").child("especies").get()
    maxId = str(len(dbPath))
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
            "codigo_correlativo": int(maxId),
            "especie":          especie,
            "estado":           estado,
            "precio_unitario":  int(precio_unitario),
            "precio_total":     int(precio_total),
            "fecha_recepcion":  fecha_recepcion,
            "numero_factura":   int(numero_factura),
            "rut_proveedor":    rut_proveedor,
            "centro_de_costo":  centro_de_costo,
            "ubicacion_actual": ubicacion_actual,
            "observaciones":    observaciones,
            "codigo_barra":     int(codigo_barra)
        }
        try:
            dbAddPath = db.reference('/')
            dbAddPath = dbAddPath.child("data").child("especies").update({maxId: item})
            # dbAddPath.push({maxId: item})
            print(item)
            # database.child("data").child("especies").child(str(last_code)).push(item)
            # database.child(last_code).patch(item)
            return redirect("/")
            
        except:
            return render_template("addItem.html", message="Something wrong happened")
    return render_template("addItem.html",cod=maxId)

@app.route('/addProveedores.html', methods=['GET','POST'])
def addProveedor():
    dbPath = db.reference('/')
    dbPath = dbPath.child("proveedores").get()
    tamaño = str(len(dbPath))

    if request.method == 'POST':
        razon_social = request.form['razon_social']
        rut = request.form['rut']
        correo = request.form['email']
        numero_telefonico = request.form['telefono']

        proveedor = {
            "razonSocial": razon_social,
            "email": correo,
            "estado": "Activo",
            "telefono": numero_telefonico,
            "rut": rut
        }
        try:         
            dbAddPath = db.reference('/')
            dbAddPath = dbAddPath.child("proveedores").update({rut: proveedor})
            print(proveedor)
            return redirect("/")
        except:    
            return render_template("addProveedores.html", message="Something wrong happened")        
    return render_template("addProveedores.html", cod=tamaño)

@app.route('/addUsuarios.html', methods=['GET','POST'])
def addUsuario():
    dbPath = db.reference('/')
    dbPath = dbPath.child("usuarios").get()
    if request.method == 'POST':
        nombre = request.form['nombre']
        rut = request.form['rut']
        correo = request.form['email']
        numero_telefonico = request.form['telefono']
        contraseña = request.form['contraseña']

        proveedor = {
            "razonSocial": razon_social,
            "email": correo,
            "estado": "Activo",
            "telefono": numero_telefonico,
            "rut": rut,
            "contraseña": contraseña
        }
        try:         
            dbAddPath = db.reference('/')
            dbAddPath = dbAddPath.child("usuarios").update({rut: usuarios})
            print(proveedor)
            return redirect("/")
        except:    
            return render_template("addUsuarios.html", message="Something wrong happened")        
    return render_template("Usuarios.html")

@app.route('/usuarios.html', methods=['GET','POST'])
def cambiarPagina():
    return render_template("addUsuarios.html")


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