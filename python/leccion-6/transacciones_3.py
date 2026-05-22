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
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO persona(nombre, apellido, email)VALUES(%s, %s, %s)"
            valores = ("Alex", "Rojas", "Rojas@gmail.com")
            cursor.execute(sentencia, valores)

            sentencia = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
            valores = ("Juan", "JuanPerez1", "jcjuan@gamil.com", 2)
            cursor.execute(sentencia, valores)

            conexion.commit() #Hasemos el commit manualmente
            print("Termina la transaccion")
except Exception as e:
    print(f'se hizo un rolback: {e}')

finally:
    conexion.close()

# http://www.pycopg.org/docs/usage.html