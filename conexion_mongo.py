from pymongo import MongoClient

client = MongoClient()


def dbConexion():
    try:
        client = MongoClient(
            'mongodb+srv://21300058:7M8umXBqEen7rYZC@cluster0.ezrizac.mongodb.net')
        # El cliente se conecta a la base de datos dbiot
        db = client['Login']

    except ConnectionError:
        print("Error al conectar a la base de datos")

    return db

def consultar_datos():
    # crear una nueva conexion a la bd
    db = dbConexion()
    # Entramos a la coleccion de la bd llamada sensores
    data = db['data']
    # Obtenemos todos los documentos de la colección sensores
    datos = data.find()
    # retornamos la consulta
    return datos


if __name__ == '__main__':
    dbConexion()
