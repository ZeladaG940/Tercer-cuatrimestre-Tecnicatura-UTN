from NumerosIgualesExepcion import NumeroIgualesExepcion
resultado = None

try:
    a = int(input('Digite el primer numero: '))
    b = int(input('Digite el segundo numero: '))
    if a == b:
        raise NumeroIgualesExepcion('Son numero iguales')
    resultado =  a/ b # modificamos
except TypeError as e:
    print(f'Ocurrio un nerror: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError: Ocurrio un error {e}')
except Exception as e:
    print(f'Exception: Ocurrio un error: ´{e}')

else:
    print('No se arrojo nimguna exepcion')
finally:
    print('Ejecucion de este bloque finally')
print(f'el resultado es: {resultado}')
print('seguimos...')

