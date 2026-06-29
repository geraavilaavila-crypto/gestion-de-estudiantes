class Estudiante:
    """
    Clase que representa a un estudiante universitario.
    Atributos:
        nombre: Nombre completo del estudiante
        matricula: Número de identificación única
        carrera: Carrera que cursa
        calificaciones: Lista con las calificaciones obtenidas
    """

    # Constructor: Inicializa los datos al crear un objeto
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.calificaciones = []  # Lista vacía para guardar calificaciones

    # Método para agregar una calificación
    def agregar_calificacion(self, nota):
        """Agrega una calificación válida (entre 0 y 10)"""
        if 0 <= nota <= 10:
            self.calificaciones.append(nota)
            print(f"✅ Calificación {nota} agregada correctamente.")
        else:
            print("❌ Error: La calificación debe estar entre 0 y 10.")

    # Método para calcular el promedio
    def calcular_promedio(self):
        """Devuelve el promedio de calificaciones o 0 si no hay notas"""
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    # Método para mostrar información completa
    def mostrar_informacion(self):
        """Imprime todos los datos y resultados del estudiante"""
        promedio = self.calcular_promedio()
        estado = "Aprobado ✅" if promedio >= 6 else "Reprobado ❌"

        print("-" * 50)
        print(f"Nombre: {self.nombre}")
        print(f"Matrícula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {promedio:.2f}")
        print(f"Estado académico: {estado}")
        print("-" * 50)


# ------------------------------ CLASE UNIVERSIDAD ----------------------------
class Universidad:
    """
    Clase que representa una universidad.
    Atributos:
        nombre: Nombre de la institución
        estudiantes: Lista de estudiantes inscritos
    """

    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    # Método para inscribir un estudiante
    def inscribir_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"📚 Estudiante {estudiante.nombre} inscrito en {self.nombre}.")

    # Método para mostrar todos los estudiantes registrados
    def listar_estudiantes(self):
        print(f"\n📋 Lista de estudiantes en {self.nombre}:")
        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados.")
            return
        for alumno in self.estudiantes:
            print(f"- {alumno.nombre} | Matrícula: {alumno.matricula}")


# ------------------------------ PROGRAMA PRINCIPAL ---------------------------
if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN UNIVERSITARIA ===")

    # 1. Crear instancia de la universidad
    universidad_ciudadana = Universidad("Universidad Ciudadana")

    # 2. Crear objetos (instanciar estudiantes)
    alumno1 = Estudiante("María López", "UC-2026-001", "Ingeniería en Sistemas")
    alumno2 = Estudiante("Juan Pérez", "UC-2026-002", "Administración")

    # 3. Inscribir estudiantes en la universidad
    universidad_ciudadana.inscribir_estudiante(alumno1)
    universidad_ciudadana.inscribir_estudiante(alumno2)

    # 4. Agregar calificaciones
    alumno1.agregar_calificacion(8.5)
    alumno1.agregar_calificacion(9.0)
    alumno1.agregar_calificacion(7.8)

    alumno2.agregar_calificacion(5.5)
    alumno2.agregar_calificacion(6.2)
    alumno2.agregar_calificacion(4.9)

    # 5. Mostrar información de cada estudiante
    alumno1.mostrar_informacion()
    alumno2.mostrar_informacion()

    # 6. Listar todos los estudiantes
    universidad_ciudadana.listar_estudiantes()
