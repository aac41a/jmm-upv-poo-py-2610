# ejemplo de clase asignatura

class Asignatura():
    nombre = ''
    nota = 0

    def __init__(self, newNombre, newNota):
        self.nombre = newNombre
        self.nota = newNota

    def addNota(self, newNota):
        self.nota = newNota
        print('Nueva nota añadida')

    def __str__(self):
        return f'[nombre: {self.nombre}, nota: {self.nota}]'