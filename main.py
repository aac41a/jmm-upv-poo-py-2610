# This is a sample Python script.

from Alumno import Alumno


if __name__ == '__main__':
    al1 = Alumno('Jose', 'Marín', '123456789X', 35, 7)
    al2 = Alumno('David', 'Lopez', '123456000A', 45, 9)
    al3 = Alumno('Fernando', '', '144456789B', 15, 3)

    print(al1)

    al1.saludar()
    al1.addNota(13)
    al1.addAge()

    print(al1.edad)
