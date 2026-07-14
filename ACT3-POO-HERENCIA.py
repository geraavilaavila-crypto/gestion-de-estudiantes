# ==================== CLASE BASE: Estudiante ====================
class Estudiante:
    """
    Clase base que representa a un estudiante universitario.
    Atributos:
        nombre: Nombre completo del estudiante
        matricula: Número de identificación única
        carrera: Carrera que cursa
        calificaciones: Lista con las calificaciones obtenidas
    """

    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.calificaciones = []

    def agregar_calificacion(self, nota):
        """Agrega una calificación válida (entre 0 y 10)"""
        if 0 <= nota <= 10:
            self.calificaciones.append(nota)
            print(f"✅ Calificación {nota} agregada correctamente.")
        else:
            print("❌ Error: La calificación debe estar entre 0 y 10.")

    def calcular_promedio(self):
        """Devuelve el promedio de calificaciones o 0 si no hay notas"""
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

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


# ==================== CLASE DERIVADA 1: EstudianteInternacional ====================
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
        self.curso_idiomas = []  # Lista para cursos de idioma adicionales

    def agregar_curso_idioma(self, curso):
        """Método exclusivo para agregar cursos de idioma"""
        self.curso_idiomas.append(curso)
        print(f"🌍 Curso de idioma '{curso}' agregado para {self.nombre}")

    def mostrar_informacion(self):
        """
        Sobrescritura del método mostrar_informacion.
        Reutiliza el método de la clase base y agrega información internacional.
        """
        # Llamada al método de la clase base
        super().mostrar_informacion()
        
        # Información adicional específica
        print("🌐 INFORMACIÓN INTERNACIONAL:")
        print(f"País de origen: {self.pais_origen}")
        print(f"Tipo de visa: {self.visa_tipo}")
        print(f"Idioma principal: {self.idioma}")
        if self.curso_idiomas:
            print(f"Cursos de idioma: {', '.join(self.curso_idiomas)}")
        print("-" * 50)

    def calcular_costo_extra(self):
        """
        Método exclusivo para calcular costos adicionales
        para estudiantes internacionales
        """
        costo_base = 1000  # Costo base por curso de idioma
        return costo_base * len(self.curso_idiomas)


# ==================== CLASE DERIVADA 2: EstudianteBecado ====================
class EstudianteBecado(Estudiante):
    """
    Clase derivada de Estudiante para estudiantes con beca.
    Hereda todos los atributos y métodos de Estudiante.
    Atributos adicionales:
        tipo_beca: Tipo de beca (académica, deportiva, etc.)
        porcentaje_beca: Porcentaje de descuento (0-100)
        promedio_requerido: Promedio mínimo para mantener la beca
    """

    def __init__(self, nombre, matricula, carrera, tipo_beca, porcentaje_beca, promedio_requerido=7.0):
        # Llamada al constructor de la clase base
        super().__init__(nombre, matricula, carrera)
        
        # Atributos exclusivos de EstudianteBecado
        self.tipo_beca = tipo_beca
        self.porcentaje_beca = porcentaje_beca
        self.promedio_requerido = promedio_requerido
        self.actividades_beca = []  # Actividades requeridas por la beca

    def agregar_actividad_beca(self, actividad):
        """Método exclusivo para agregar actividades de la beca"""
        self.actividades_beca.append(actividad)
        print(f"📋 Actividad '{actividad}' agregada a la beca de {self.nombre}")

    def verificar_estado_beca(self):
        """
        Método exclusivo para verificar si el estudiante mantiene su beca
        """
        promedio = self.calcular_promedio()
        if promedio >= self.promedio_requerido:
            print(f"✅ {self.nombre} mantiene su beca (Promedio: {promedio:.2f})")
            return True
        else:
            print(f"❌ {self.nombre} está en riesgo de perder su beca (Promedio: {promedio:.2f})")
            return False

    def mostrar_informacion(self):
        """
        Sobrescritura del método mostrar_informacion.
        Reutiliza el método de la clase base y agrega información de beca.
        """
        super().mostrar_informacion()
        
        # Información adicional de la beca
        print("🎓 INFORMACIÓN DE BECA:")
        print(f"Tipo de beca: {self.tipo_beca}")
        print(f"Porcentaje de beca: {self.porcentaje_beca}%")
        print(f"Promedio requerido: {self.promedio_requerido}")
        
        # Verificar estado de la beca
        promedio = self.calcular_promedio()
        estado_beca = "MANTIENE" if promedio >= self.promedio_requerido else "EN RIESGO"
        print(f"Estado de beca: {estado_beca}")
        
        if self.actividades_beca:
            print(f"Actividades: {', '.join(self.actividades_beca)}")
        print("-" * 50)


# ==================== CLASE MODIFICADA: Universidad ====================
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
        """Inscribe un estudiante en la universidad"""
        self.estudiantes.append(estudiante)
        print(f"📚 Estudiante {estudiante.nombre} inscrito en {self.nombre}.")
        
    def mostrar_estadisticas_tipo(self):
        """
        Método para mostrar estadísticas por tipo de estudiante
        """
        internacionales = sum(1 for e in self.estudiantes if isinstance(e, EstudianteInternacional))
        becados = sum(1 for e in self.estudiantes if isinstance(e, EstudianteBecado))
        regulares = sum(1 for e in self.estudiantes if not isinstance(e, (EstudianteInternacional, EstudianteBecado)))
        
        print(f"\n📊 ESTADÍSTICAS DE {self.nombre}:")
        print(f"Estudiantes internacionales: {internacionales}")
        print(f"Estudiantes becados: {becados}")
        print(f"Estudiantes regulares: {regulares}")
        print(f"Total: {len(self.estudiantes)}")

    def listar_estudiantes(self):
        """Muestra todos los estudiantes registrados"""
        print(f"\n📋 Lista de estudiantes en {self.nombre}:")
        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados.")
            return
        for alumno in self.estudiantes:
            # Mostrar tipo de estudiante
            tipo = "Regular"
            if isinstance(alumno, EstudianteInternacional):
                tipo = "Internacional"
            elif isinstance(alumno, EstudianteBecado):
                tipo = "Becado"
            print(f"- {alumno.nombre} | Matrícula: {alumno.matricula} | Tipo: {tipo}")


# ==================== PROGRAMA PRINCIPAL ====================
if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN UNIVERSITARIA CON HERENCIA ===")

    # 1. Crear instancia de la universidad
    universidad = Universidad("Universidad Ciudadana")

    # 2. Crear diferentes tipos de estudiantes
    print("\n--- Creando estudiantes ---")
    
    # Estudiante regular (de la clase base)
    alumno1 = Estudiante("María López", "UC-2026-001", "Ingeniería en Sistemas")
    
    # Estudiante internacional (clase derivada)
    alumno2 = EstudianteInternacional(
        "John Smith", 
        "UC-2026-002", 
        "Administración", 
        "Estados Unidos", 
        "F-1", 
        "Inglés"
    )
    
    # Estudiante becado (clase derivada)
    alumno3 = EstudianteBecado(
        "Ana Rodríguez", 
        "UC-2026-003", 
        "Medicina", 
        "Académica", 
        50, 
        8.0
    )

    # 3. Inscribir estudiantes
    print("\n--- Inscribiendo estudiantes ---")
    universidad.inscribir_estudiante(alumno1)
    universidad.inscribir_estudiante(alumno2)
    universidad.inscribir_estudiante(alumno3)

    # 4. Agregar calificaciones (método heredado)
    print("\n--- Agregando calificaciones ---")
    alumno1.agregar_calificacion(8.5)
    alumno1.agregar_calificacion(9.0)
    
    alumno2.agregar_calificacion(7.5)
    alumno2.agregar_calificacion(8.2)
    
    alumno3.agregar_calificacion(9.0)
    alumno3.agregar_calificacion(8.5)
    alumno3.agregar_calificacion(9.5)

    # 5. Probar métodos exclusivos de cada subclase
    print("\n--- Probando métodos exclusivos ---")
    
    # Método exclusivo de EstudianteInternacional
    alumno2.agregar_curso_idioma("Español Avanzado")
    alumno2.agregar_curso_idioma("Francés Básico")
    costo_extra = alumno2.calcular_costo_extra()
    print(f"💰 Costo extra por idiomas: ${costo_extra}")
    
    # Método exclusivo de EstudianteBecado
    alumno3.agregar_actividad_beca("Voluntariado en hospital")
    alumno3.agregar_actividad_beca("Investigación médica")
    alumno3.verificar_estado_beca()

    # 6. Mostrar información (método sobrescrito en cada subclase)
    print("\n--- Mostrando información de estudiantes ---")
    alumno1.mostrar_informacion()
    alumno2.mostrar_informacion()
    alumno3.mostrar_informacion()

    # 7. Mostrar estadísticas
    universidad.mostrar_estadisticas_tipo()
    universidad.listar_estudiantes()
    