# from sqlalchemy import create_engine, MetaData
import mysql.connector


def conectar_db():
    # Crea la conexión a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="proyecto_edilson"
    )

# engine = create_engine("mysql+pymysql://root:12345@localhost:3306/proyecto_caleb")

# meta = MetaData()

# conn = engine.connect()

    # conn = conexion.cursor()

    return conexion
