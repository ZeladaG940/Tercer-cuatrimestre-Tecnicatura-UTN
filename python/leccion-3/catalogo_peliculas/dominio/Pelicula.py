class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Pelicula: {self._nombre}'

    @property #metodo get
    def nombre(self):
        return self._nombre

    @nombre.setter #metodo set
    def nombre(self, nombre):
        self._nombre = nombre
