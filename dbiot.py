from pymongo import MongoClient

client = MongoClient()


def dbConexion():
    try:
        client = MongoClient(
            'mongodb+srv://21300058:7M8umXBqEen7rYZC@cluster0.ezrizac.mongodb.net')
        # El cliente se conecta a la base de datos dbiot
        db = client['db_01']

    except ConnectionError:
        print("Error al conectar a la base de datos")

    return db

def consultar_sensore():
    #crear una nueva conexion a la bd
    db = dbConexion()
    #Entramos a la coleccion de la bd llamada sensores
    sensores = db['sensores1']
    #Obtenemos todos los documentos de la colección sensores
    c_sensores = sensores.find()
    #retornamos la consulta
    return c_sensores

if __name__ == "__main__":
    dbConexion()
