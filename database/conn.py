import firebase_admin
from firebase_admin import credentials,db

cred = credentials.Certificate('proyectoi-invedu-firebase-adminsdk-nplni-3aa203bb29.json')

firebase_admin.initialize_app(cred, {
  'databaseURL' : 'https://proyectoi-invedu-default-rtdb.firebaseio.com/'
})

ref = db.reference('/').child("proveedores")
nProv = "19176913-2"
new_prov = ref.child(nProv)
ref.push({
  '19176913-2' :
    {
      'Nombre':'test1',
      'apellido':'apptest'
    }
})