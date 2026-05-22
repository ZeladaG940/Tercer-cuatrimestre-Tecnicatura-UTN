import sys

import psycopg2 as bd
from logger_base import log
import sys

class Conexion:
    __DATABASE = 'test_bd'
    __USERNAME = 'postgres'
    __PASSWORD = '9488'
    _DB_PORT = '5432'
    __HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                    host=cls.__HOST,
                    user=cls.__USERNAME,
                    password=cls.__PASSWORD,
                    port=cls._DB_PORT,
                    database=cls.__DATABASE
                )
                log.debug('Conexión exitosa')
                return cls._conexion

            except Exception as e:
                log.error(f'Ocurrio un error: {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio un error: {e}')
                sys.exit()
        else:
            return cls._cursor

if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
