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


@app.route('/', methods=['GET', 'POST'])
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


@app.route('/addItem.html', methods=['GET', 'POST'])
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
            "especie": especie,
            "estado": estado,
            "precio_unitario": int(precio_unitario),
            "precio_total": int(precio_total),
            "fecha_recepcion": fecha_recepcion,
            "numero_factura": int(numero_factura),
            "rut_proveedor": rut_proveedor,
            "centro_de_costo": centro_de_costo,
            "ubicacion_actual": ubicacion_actual,
            "observaciones": observaciones,
            "codigo_barra": int(codigo_barra)
        }
        try:
            dbAddPath = db.reference('/')
            dbAddPath = dbAddPath.child("data").child("especies").update({maxId: item})
            # dbAddPath.push({maxId: item})
            # print(item)
            # database.child("data").child("especies").child(str(last_code)).push(item)
            # database.child(last_code).patch(item)
            # return redirect("/")
            print("Antes" + str(maxId))
            dbPathTwo = db.reference('/')
            dbPathTwo = dbPathTwo.child("data").child("especies").get()
            maxId = str(len(dbPathTwo))
            print("Despues" + str(maxId))
            return render_template("addItem.html", cod=maxId)
        except:
            return render_template("addItem.html", message="Something wrong happened")
    return render_template("addItem.html", cod=maxId)


@app.route('/modifyItem.html', methods=['GET', 'POST'])
def modifyItem():
    o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 = "","","","","","","","","","","",""
    if request.method == 'POST':
        especie = request.form["sCodCor"]
        dbPath = db.reference('/')
        dbPath = dbPath.child("data").child("especies").child(especie).get()

        try:
            if("centro_de_costo" in dbPath): o1 = str(dbPath["centro_de_costo"])
            else: o1="SIN-DATOS"

            if("codigo_correlativo" in dbPath):o2 = str(dbPath["codigo_correlativo"])
            else: o2 = "SIN-DATOS"

            if("especie" in dbPath): o3 = str(dbPath["especie"])
            else: o3 = "SIN-DATOS"

            if("estado" in dbPath):
                if(str(dbPath["estado"])=="B"):o4 = "BUENO"
                elif(str(dbPath["estado"])=="M"):o4 = "MALO"
                else:o4 = "REGULAR"
            else: o4 = "SIN-DATOS"

            if("fecha_recepcion" in dbPath): o5 = str(dbPath["fecha_recepcion"])
            else: o5 = "SIN-DATOS"

            if("numero_factura" in dbPath): o6 = str(dbPath["numero_factura"]); print(str(dbPath["numero_factura"]))
            else: o6 = 0

            if("precio_unitario" in dbPath): o7 = str(dbPath["precio_unitario"])
            else: o7 = 0

            if("rut_proveedor" in dbPath): o8 = str(dbPath["rut_proveedor"])
            else: o8 = "SIN-DATOS"

            if("ubicacion_actual" in dbPath): o9 = str(dbPath["ubicacion_actual"])
            else: o9 = "SIN-DATOS"

            if("codigo_barra" in dbPath): o10 = str(dbPath["codigo_barra"])
            else: o10 = "SIN-DATOS"

            if("precio_total" in dbPath): o11 = str(dbPath["precio_total"])
            else: o11 = 0

            if("observaciones" in dbPath): o12 = str(dbPath["observaciones"])
            else: o12 = "SIN-DATOS"

            return render_template("modifyItem.html",
                                   rCCosto=o1,  rCCorrelativo=o2, rEspecie=o3,
                                   rEstado=o4,  rFRecepcion=o5, rNFactura=o6,
                                   rPUni=o7,    rRProveedor=o8, rUActual=o9,
                                   rCBarra=o10, rPTotal=o11, rObs=o12)
        except:
            return render_template("modifyItem.html", err = "error")


    return render_template("modifyItem.html",
                           rCCosto=o1, rCCorrelativo=o2, rEspecie=o3,
                           rEstado=o4, rFRecepcion=o5, rNFactura=o6,
                           rPUni=o7, rRProveedor=o8, rUActual=o9,
                           rCBarra=o10, rPTotal=o11, rObs=o12)


@app.route('/addProveedores.html', methods=['GET', 'POST'])
def addProveedor():
    dbAddPath = db.reference('/')
    if request.method == 'POST':
        razon_social = request.form['razonProv']
        rut = request.form['rutProv']
        correo = request.form['mailProv']
        numero_telefonico = request.form['telefonoProv']
        buscaRut = dbAddPath.child("proveedores").child(rut).get()
        try:
            x = len(buscaRut)
            print(x)
            return render_template("addProveedores.html", err=0)
        except:
            proveedor = {
                "razonSocial": razon_social,
                "email": correo,
                "estado": "Activo",
                "telefono": int(numero_telefonico),
                "rut": rut
            }
            try:
                dbAddPath.child("proveedores").update({rut: proveedor})
                print("postupdate")
                return render_template("addProveedores.html", err=1)
            except:
                return render_template("addProveedores.html", message="Something wrong happened", err=1)
    return render_template("addProveedores.html", err=1)

@app.route('/modifyProv.html', methods=['GET', 'POST'])
def modifyProv():
    o1,o2,o3,o4 = "","","",""
    if request.method == 'POST':
        sProv = request.form["sRProv"]
        dbPath = db.reference('/')
        dbPath = dbPath.child("proveedores").child(sProv).get()

        try:
            if("razonSocial" in dbPath): o1 = str(dbPath["razonSocial"])
            else: o1="SIN-DATOS"

            if("rut" in dbPath):o2 = str(dbPath["rut"])
            else: o2 = "SIN-DATOS"

            if("email" in dbPath): o3 = str(dbPath["email"])
            else: o3 = "SIN-DATOS"

            if("telefono" in dbPath): o4 = str(dbPath["telefono"])
            else: o4 = "SIN-DATOS"

            return render_template("modifyProv.html",
                                razonSocial=o1,  rut=o2, email=o3, telefono=o4)
        except:
            return render_template("modifyProv.html", err = "error")
    return render_template("modifyProv.html",
                           razonSocial=o1,  rut=o2, email=o3, telefono=o4)


@app.route('/addUsuarios.html', methods=['GET', 'POST'])
def addUsuario():
    dbAddPath = db.reference('/')
    if request.method == 'POST':
        nombre = request.form['uNombre']
        rut = request.form['uRut']
        correo = request.form['uMail']
        numero_telefonico = request.form['uFono']
        contraseña = request.form['uPass']
        buscaUsuario = dbAddPath.child("usuarios").child(rut).get()
        try:
            x = len(buscaUsuario)
            print(x)
            return render_template("addUsuarios.html", err=0)
        except:
            usuarios = {
                "razonSocial": nombre,
                "email": correo,
                "estado": "Activo",
                "telefono": int(numero_telefonico),
                "rut": rut,
                "contraseña": contraseña
            }
            try:
                dbAddPath.child("usuarios").update({rut: usuarios})
                print(usuarios)
                return render_template("addUsuarios.html", err=1)
            except:
                return render_template("addUsuarios.html", message="Something wrong happened")
    return render_template("addUsuarios.html", err=1)


@app.route('/listUsuarios.html', methods=['GET', 'POST'])
def modifyUsuarios():
    o1, o2, o3, o4, o5 = "", "", "", "", ""
    if request.method == 'POST':
        uRut = request.form["uRut"]
        dbPath = db.reference('/')
        dbPath = dbPath.child("usuarios").child(uRut).get()

        try:
            if ("nombre" in dbPath): o1 = str(dbPath["nombre"])
            else: o1 = "SIN-DATOS"

            if ("rut" in dbPath): o2 = str(dbPath["rut"])
            else: o2 = "SIN-DATOS"

            if ("email" in dbPath): o3 = str(dbPath["email"])
            else: o3 = "SIN-DATOS"

            if ("telefono" in dbPath): o4 = str(dbPath["telefono"])
            else: o4 = 0

            if ("contraseña" in dbPath): o5 = str(dbPath["contraseña"])
            else: o5 = "SIN-DATOS"

            return render_template("modifyProv.html",
                                   nombre=o1, rut=o2, email=o3, telefono=o4, contraseña=o5)
        except:
            return render_template("modifyProv.html", err="error")
    return render_template("modifyProv.html",
                           nombre=o1, rut=o2, email=o3, telefono=o4, contraseña=o5)



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
