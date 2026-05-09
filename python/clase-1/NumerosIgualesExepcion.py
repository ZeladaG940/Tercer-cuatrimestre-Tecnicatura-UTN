class NumeroIgualesExepcion (Exception): #Extiede de la clase
    def __init__(self, mensaje):
        self.mensaje = mensaje