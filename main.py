from estudiante import Estudiante
from estudiante_internacional import EstudianteInternacional
from estudiante_becado import EstudianteBecado
from universidad import Universidad

if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN UNIVERSITARIA CON HERENCIA ===")

    # 1. Crear instancia de la universidad
    universidad = Universidad("Universidad Ciudadana")

    # 2. Crear diferentes tipos de estudiantes
    print("\n--- Creando estudiantes ---")
    alumno1 = Estudiante("María López", "UC-2026-001", "Ingeniería en Sistemas")
    alumno2 = EstudianteInternacional(
        "John Smith", 
        "UC-2026-002", 
        "Administración", 
        "Estados Unidos", 
        "F-1", 
        "Inglés"
    )
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

    # 4. Agregar calificaciones
    print("\n--- Agregando calificaciones ---")
    alumno1.agregar_calificacion(8.5)
    alumno1.agregar_calificacion(9.0)
    alumno2.agregar_calificacion(7.5)
    alumno2.agregar_calificacion(8.2)
    alumno3.agregar_calificacion(9.0)
    alumno3.agregar_calificacion(8.5)
    alumno3.agregar_calificacion(9.5)

    # 5. Probar métodos exclusivos
    print("\n--- Probando métodos exclusivos ---")
    alumno2.agregar_curso_idioma("Español Avanzado")
    alumno2.agregar_curso_idioma("Francés Básico")
    costo_extra = alumno2.calcular_costo_extra()
    print(f"💰 Costo extra por idiomas: ${costo_extra}")
    
    alumno3.agregar_actividad_beca("Voluntariado en hospital")
    alumno3.agregar_actividad_beca("Investigación médica")
    alumno3.verificar_estado_beca()

    # 6. Mostrar información
    print("\n--- Mostrando información de estudiantes ---")
    alumno1.mostrar_informacion()
    alumno2.mostrar_informacion()
    alumno3.mostrar_informacion()

    # 7. Mostrar estadísticas
    universidad.mostrar_estadisticas_tipo()
    universidad.listar_estudiantes()