
from estudiante import Estudiante

class EstudianteInternacional(Estudiante):
    """
    Clase derivada de Estudiante para estudiantes internacionales.
    Hereda todos los atributos y métodos de Estudiante.
    Atributos adicionales:
        pais_origen: País de procedencia del estudiante
        visa_tipo: Tipo de visa que posee
        idioma: Idioma principal del estudiante
    """

    def __init__(self, nombre, matricula, carrera, pais_origen, visa_tipo, idioma):
        # Llamada al constructor de la clase base (Estudiante)
        super().__init__(nombre, matricula, carrera)
        
        # Atributos exclusivos de EstudianteInternacional
        self.pais_origen = pais_origen
        self.visa_tipo = visa_tipo
        self.idioma = idioma
        self.curso_idiomas = []

    def agregar_curso_idioma(self, curso):
        """Método exclusivo para agregar cursos de idioma"""
        self.curso_idiomas.append(curso)
        print(f"🌍 Curso de idioma '{curso}' agregado para {self.nombre}")

    def mostrar_informacion(self):
        """
        Sobrescritura del método mostrar_informacion.
        Reutiliza el método de la clase base y agrega información internacional.
        """
        super().mostrar_informacion()
        print("🌐 INFORMACIÓN INTERNACIONAL:")
        print(f"País de origen: {self.pais_origen}")
        print(f"Tipo de visa: {self.visa_tipo}")
        print(f"Idioma principal: {self.idioma}")
        if self.curso_idiomas:
            print(f"Cursos de idioma: {', '.join(self.curso_idiomas)}")
        print("-" * 50)

    def calcular_costo_extra(self):
        """Método exclusivo para calcular costos adicionales"""
        costo_base = 1000
        return costo_base * len(self.curso_idiomas)