#para abrir una archivo se le debe de declara una variable
try:
    archivos = open('prueba.txt', 'w', encoding='utf8')#la w es de write que significa escribir
    archivos.write('Programamos con diferentes tipos de archivos, ahora en txt. \n')
    archivos.write('Los acentos son mas importantes para las palabras\n')
    archivos.write('Como por ejemplo: acción, ejecución, y producción\n')
    archivos.write('las letras son:\n r read,\n a append,\n w write,\n x')
    archivos.write('\n t esta es para texto o text,\n b archivos binarios,\n w+ leer y escribe son iguales r+\n')
    archivos.write('saludos a todos los alumnos de la Tecnicatura\n')
    archivos.write('Con esto terminamos...')
except Exception as e:
    print(e)
finally: #Siempre se ejecuta
    archivos.close() #Con esto se debe cerrar el archivo

#archivos.write('todo quedo perfecto') Esto es un error
