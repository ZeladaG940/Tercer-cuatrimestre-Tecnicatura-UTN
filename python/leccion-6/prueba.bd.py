import psycopg2 as bd
from psycopg2._psycopg import cursor

#se importa psycopg2 = posgreSQL

conexion = bd.connect(
    user = 'postgres',
    password = '9488', #contraseña puesta en posgreSQL
    host = '127.0.0.1',
    port = '5432', #puerto que se ejecuta posgreSQL
    database = 'test_bd' #nombre de baseData puesta en posgreSQL
)
try:
    conexion.autocommit = False
    cursor = conexion.cursor() #esto no deveria estar
    sentencia = "INSERT INTO persona(nombre, apellido, email)VALUES(%s, %s, %s)"
    valores = ("Maria", "Esparza", "mesapa@gmail.com")
    cursor.execute(sentencia, valores)
    conexion.commit() #Hasemos el commit manualmente
    print("Termina la transaccion")
except Exception as e:
    conexion.rollback()
    print(f'se hizo un rolback: {e}')

finally:
    conexion.close()

# http://www.pycopg.org/docs/usage.html