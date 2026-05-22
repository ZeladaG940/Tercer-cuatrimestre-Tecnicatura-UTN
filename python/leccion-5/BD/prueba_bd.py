import psycopg2
#se importa psycopg2 = posgreSQL

conexion = psycopg2.connect(
    user = 'postgres',
    password = '9488', #contraseña puesta en posgreSQL
    host = '127.0.0.1',
    port = '5432', #puerto que se ejecuta posgreSQL
    database = 'test_bd' #nombre de baseData puesta en posgreSQL
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input('Digite un numero para el id_persona: ')
            cursor.execute(sentencia, (id_persona, )) #de esta manera ejecutamos la sentencia
            registros = cursor.fetchone() #Recuperamos todos los registros que seran en una lista
            print(registros)

except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close()

# http://www.pycopg.org/docs/usage.html