class PersonaDao:
    ''''
    DAO significa: DATA Acesss Object
    CRUD significa:
                    Crate  -> Insertar
                    Read   -> Seleccionar
                    Update -> Actualizar
                    Delete -> Eliminar

    '''

    __SELECCINAR = 'SELECT * FROM persona BY id_persona'
    __INSERT = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    __UPDATE = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    __DELETE = 'DELETE FROM persona WHERE id_persona = %s'