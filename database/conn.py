import firebase_admin, os
from firebase_admin import credentials,db

cred = credentials.Certificate('')
cred = credentials.Certificate('authKey.json')

firebase_admin.initialize_app(cred, {
  'databaseURL' : 'https://proyectoi-invedu-default-rtdb.firebaseio.com/'
})


def home():
  result = db.reference("/").get('/proveedores', None)
  return str(result)

nProv = "3333333-3"
def setRef():
  ref = db.reference('/').child("proveedores")
  return ref
def getAllProv(ref):
  return print(ref.get())

def putNewProv(ref,nProv):
  ref.put({
    nProv:
      {
        'Nombre': 'test1',
        'apellido': 'apptest'
      }
  })

"""for i in ref:
  rut = ref.child(i).child("rut").get()
  razon_social = str(ref.child(i).child("razonSocial").get())
  print(rut, razon_social)"""

"""nProv = "3333333-3"
new_prov = ref.child(nProv)
rut = new_prov.child("rut")
razon_social = str(new_prov.child("razonSocial").get())
print("Rut:" + rut)
print("Razon social:" + razon_social)"""
"""ref.push({
  '19176913-2' :
    {
      'Nombre':'test1',
      'apellido':'apptest'
    }
})"""