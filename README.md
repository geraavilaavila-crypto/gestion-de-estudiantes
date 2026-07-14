# 🎓 Sistema de Gestión Universitaria con Herencia

## 📚 Descripción del Proyecto
Sistema de gestión universitaria que demuestra el uso de **herencia** en Python. 
El proyecto extiende la aplicación base de gestión de estudiantes agregando 
tipos especializados de estudiantes con atributos y comportamientos únicos.

---

## 🎯 Conceptos de Programación Aplicados

### 🔗 Herencia
- **Clase Base**: `Estudiante` - Contiene atributos y métodos comunes
- **Clases Derivadas**: 
  - `EstudianteInternacional` - Hereda de Estudiante
  - `EstudianteBecado` - Hereda de Estudiante

### ♻️ Reutilización de Código
- Uso de `super()` para llamar al constructor de la clase base
- Métodos heredados: `agregar_calificacion()`, `calcular_promedio()`
- Atributos heredados: `nombre`, `matricula`, `carrera`, `calificaciones`

### ✏️ Sobrescritura de Métodos
- `mostrar_informacion()` es sobrescrito en ambas subclases
- Se extiende la funcionalidad agregando información específica

### 🆕 Métodos Exclusivos
- **EstudianteInternacional**: `agregar_curso_idioma()`, `calcular_costo_extra()`
- **EstudianteBecado**: `agregar_actividad_beca()`, `verificar_estado_beca()`

---

## 🏗️ Estructura del Proyecto
gestión-de-estudiantes/
│
├── 📄 estudiante.py # Clase base
├── 📄 estudiante_internacional.py # Subclase: Estudiantes internacionales
├── 📄 estudiante_becado.py # Subclase: Estudiantes con beca
├── 📄 universidad.py # Clase de gestión
├── 📄 main.py # Programa principal
├── 📄 README.md # Este archivo
└── 📄 .gitignore # Archivos ignorados por Git

text

---

## 📊 Diagrama de Clases
┌─────────────────────────────┐
│ Estudiante │ ← CLASE BASE
│─────────────────────────────│
│ - nombre: str │
│ - matricula: str │
│ - carrera: str │
│ - calificaciones: list │
│─────────────────────────────│
│ + agregar_calificacion() │
│ + calcular_promedio() │
│ + mostrar_informacion() │
└──────────┬──────────────────┘
│
│ HERENCIA
│
┌──────┴──────┬──────────────┐
▼ ▼ ▼
┌─────────────┐ ┌──────────┐
│Estudiante │ │Estudiante│
│Internacional│ │ Becado │
│─────────────│ │──────────│
│ - pais │ │ - tipo │
│ - visa │ │ - % beca │
│ - idioma │ │ - prom_req│
│ - cursos │ │ - activ │
│─────────────│ │──────────│
│ + agregar_ │ │ + agregar_│
│ curso() │ │ activ() │
│ + calcular_ │ │ + verificar│
│ costo() │ │ beca() │
│ + mostrar_ │ │ + mostrar_│
│ info() │ │ info() │
└─────────────┘ └──────────┘

text

---

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos
- Python 3.6 o superior

### Pasos
```bash
# 1. Clonar el repositorio
git clone https://github.com/geravialvaia-crypto/gestio

# 2. Navegar a la carpeta
cd gestio

# 3. Ejecutar el programa
python main.py
💻 Ejemplo de Ejecución
text
=== SISTEMA DE GESTIÓN UNIVERSITARIA CON HERENCIA ===

--- Creando estudiantes ---
📚 Estudiante María López inscrito en Universidad Ciudadana.
📚 Estudiante John Smith inscrito en Universidad Ciudadana.
📚 Estudiante Ana Rodríguez inscrito en Universidad Ciudadana.

--- Agregando calificaciones ---
✅ Calificación 8.5 agregada correctamente.
✅ Calificación 9.0 agregada correctamente.

--- Probando métodos exclusivos ---
🌍 Curso de idioma 'Español Avanzado' agregado para John Smith
💰 Costo extra por idiomas: $2000

--- Mostrando información de estudiantes ---
--------------------------------------------------
Nombre: John Smith
Matrícula: UC-2026-002
Carrera: Administración
Calificaciones: [7.5, 8.2]
Promedio: 7.85
Estado académico: Aprobado ✅
--------------------------------------------------
🌐 INFORMACIÓN INTERNACIONAL:
País de origen: Estados Unidos
Tipo de visa: F-1
Idioma principal: Inglés
Cursos de idioma: Español Avanzado, Francés Básico
--------------------------------------------------
🔍 Características de las Subclases
🌍 EstudianteInternacional
Atributos adicionales: país de origen, tipo de visa, idioma principal

Métodos exclusivos:

agregar_curso_idioma(): Registra cursos de idioma adicionales

calcular_costo_extra(): Calcula costos adicionales por idiomas

Sobrescritura: mostrar_informacion() agrega datos internacionales

🎓 EstudianteBecado
Atributos adicionales: tipo de beca, porcentaje, promedio requerido

Métodos exclusivos:

agregar_actividad_beca(): Registra actividades requeridas

verificar_estado_beca(): Verifica si mantiene la beca

Sobrescritura: mostrar_informacion() agrega datos de beca

📋 Versiones
v1.0 (Versión inicial)
Clase base Estudiante

Clase Universidad

Gestión básica de estudiantes

v1.1 (Versión con Herencia) ← ACTUAL
✅ Clases derivadas implementadas

✅ Métodos sobrescritos

✅ Métodos exclusivos

✅ Documentación completa

✅ Pruebas de funcionalidad

👤 Autor
Gerardo Avila Avila

GitHub: @geraavilaavila-crypto

📚 Tecnologías Utilizadas
https://img.shields.io/badge/Python-3.8+-blue.svg
https://img.shields.io/badge/Git-Control_de_versiones-orange.svg
https://img.shields.io/badge/GitHub-Repositorio-green.svg

📝 Licencia
Este proyecto es parte de una actividad académica. Todos los derechos reservados.

🎯 Objetivos de Aprendizaje
✅ Implementar herencia en Python

✅ Reutilizar código con super()

✅ Sobrescribir métodos de la clase base

✅ Crear métodos exclusivos para subclases

✅ Documentar código y proyecto

✅ Usar Git y GitHub para control de versiones
