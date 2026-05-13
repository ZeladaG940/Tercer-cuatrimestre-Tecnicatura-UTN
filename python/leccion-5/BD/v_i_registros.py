import psycopg2

# se importa psycopg2 = PostgreSQL

conexion = psycopg2.connect(
    user='postgres',
    password='9488',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = (
                ('Carlos', 'Lara', 'CLara@gmail.com'),
                ('Marcos', 'Canto', 'Marco@gmail.com'),
                ('Marcelo', 'Cuenca', 'Cuenca@gamil.com')
            )# es una tupla de tuplas
            cursor.executemany(sentencia, valores)
            #conexion.commit() esto se utilioza para guardar en la base de datos
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close