#clase alumno

from Asignatura import Asignatura

class Alumno():
    nombre = ''
    apellidos = ''
    dni = ''
    edad = 0
    nota = 0
    asignaturas = []

    def __init__(self, newNom, newApe, newDni, newEdad, newNota):
        self.nombre = newNom
        self.apellidos = newApe
        self.dni = newDni
        self.edad = newEdad
        self.nota = newNota


    def saludar(self):
        print(f'Hola {self.nombre}, bienvenido!')

    def addNota(self, newNota):
        if newNota > 0 and newNota <=10:
            self.nota = newNota
            print('Nota modificada')
        else:
            print('Introduce un valor de nota válido')

    def addAge(self):
        self.edad += 1
        print('edad modificada')

    def addAsignatura(self, Asignatura):
        self.asignaturas.append(Asignatura)
        print('Nueva Nota añadida')

    def delAsignatura(self, Asignatura):
        self.asignaturas.remove(Asignatura)
        print('Asignatura eliminada')