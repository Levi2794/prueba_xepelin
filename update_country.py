
# Cinfiguración de parametros del servidor
url = 'http://localhost:8069'
db = 'xepelinTest'
username = 'admin'
password = 'admin'

# Exportación de librerias (xmlrpc: para conectar con el servidor odoo)
import xmlrpc.client
import random

# Prueba de conexicón al servidor odoo
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#output = common.version()

# Prueba de credenciales. Devuelve el ID del usuario
uid = common.authenticate(db, username, password, {})

# Inicializa los modelos
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Extracción de registros de los modelos
fields_country = models.execute_kw(db, uid, password,
    'res.country', 'search',
    [[]])
fields_master_X = models.execute_kw(db, uid, password,
    'master_x', 'search',
    [[]])

# Actualización del campo cuontry_id
for i in fields_master_X:
    models.execute_kw(db, uid, password, 'master_x', 'write', [[i], {
        'country_id': random.choice(fields_country),
    }])