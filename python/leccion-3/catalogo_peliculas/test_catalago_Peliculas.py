from dominio.Pelicula import Pelicula
from servicio.catalogoPelicula import CatalogoPelicula as cp

opcion = None

#bucle para escojes solo 4 opciones
while opcion != 4:

    #Manejo de errores
    try:
        print('Opciones: ')
        print('1. Agregar pelicula')
        print('2. Listar de peliculas')
        print('3. Eliminar catálogo de pelicula')
        print('4. Salir')
        opcion = int(input('Digite una opcion de menú (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Digite el nombre de la pelicula: ')
            nombre = Pelicula(nombre_pelicula)
            cp.agregarpelicula(nombre)

        elif opcion == 2:
            cp.listar_peliculas()

        elif opcion == 3:
            cp.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None


    else:
        print('Salimos del programa...')