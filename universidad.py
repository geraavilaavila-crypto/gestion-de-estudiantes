from estudiante import Estudiante
from estudiante_internacional import EstudianteInternacional
from estudiante_becado import EstudianteBecado

class Universidad:
    """
    Clase que representa una universidad.
    Atributos:
        nombre: Nombre de la institución
        estudiantes: Lista de estudiantes inscritos
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def inscribir_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"📚 Estudiante {estudiante.nombre} inscrito en {self.nombre}.")
        
    def mostrar_estadisticas_tipo(self):
        internacionales = sum(1 for e in self.estudiantes if isinstance(e, EstudianteInternacional))
        becados = sum(1 for e in self.estudiantes if isinstance(e, EstudianteBecado))
        regulares = sum(1 for e in self.estudiantes if not isinstance(e, (EstudianteInternacional, EstudianteBecado)))
        
        print(f"\n📊 ESTADÍSTICAS DE {self.nombre}:")
        print(f"Estudiantes internacionales: {internacionales}")
        print(f"Estudiantes becados: {becados}")
        print(f"Estudiantes regulares: {regulares}")
        print(f"Total: {len(self.estudiantes)}")

    def listar_estudiantes(self):
        print(f"\n📋 Lista de estudiantes en {self.nombre}:")
        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados.")
            return
        for alumno in self.estudiantes:
            tipo = "Regular"
            if isinstance(alumno, EstudianteInternacional):
                tipo = "Internacional"
            elif isinstance(alumno, EstudianteBecado):
                tipo = "Becado"
            print(f"- {alumno.nombre} | Matrícula: {alumno.matricula} | Tipo: {tipo}")