# 📊 Trabajo Práctico: Gestión Colaborativa, Control de Versiones y Organización Empresarial
## 💻 (Git, GitHub y Jira) & Análisis de Ventas - Pequeña Empresa

---

## 🚀 Descripción del Proyecto
Este repositorio contiene el desarrollo de una solución modular en Python (Google Colab) orientada al **Análisis de Ventas para una Pequeña Empresa**. El objetivo principal es extraer métricas clave del negocio mediante el procesamiento de datos históricos, asegurando un entorno de ejecución reproducible, seguro y gestionado bajo buenas prácticas de ingeniería de software.

---

## 📅 I. Gestión Organizacional y Trazabilidad (Jira)
El desarrollo del proyecto se planificó de forma individual utilizando un enfoque ágil en **Jira**. Cada incremento de código y documentación está estrictamente vinculado a un ticket único para garantizar la trazabilidad completa del ciclo de vida del software.

### 🔗 Matriz de Trazabilidad de Requerimientos

| ID Ticket Jira | Tarea / Característica | Rama Asociada en GitHub | Estado |
| :--- | :--- | :--- | :--- |
| **AN-1** | Configuración de entorno Colab y PAT | `main` | ✅ Completado |
| **AN-2** | Diseño de Arquitectura y Estructura | `main` | ✅ Completado |
| **AN-3** | Optimización de Documentación (`README.md`) | `feature/desarrollo-analisis` | ✅ Completado |
| **AN-4** | Desarrollo del Algoritmo de Análisis | `feature/desarrollo-analisis` | ⏳ En Progreso |

---

## 🔀 II. Control de Versiones (Flujo Git & GitHub)
Para este proyecto individual se adoptó una estrategia de ramificación basada en **Feature Branches** para asegurar que la rama principal (`main`) permanezca siempre en un estado estable y ejecutable.

*   **Política de Integración:** Está prohibida la inyección directa de código sobre la rama `main`. Todo cambio se realiza en ramas secundarias identificadas con el prefijo del área correspondiente (ej. `feature/`).
*   **Aprobación mediante Pull Requests:** La integración de nuevas características se ejecuta formalmente a través de Pull Requests (PRs). Al ser un desarrollo unipersonal, el flujo se valida mediante auditoría propia y cierre de PR por la autora.

---

## 🛠️ III. Implementación Técnica y Reproducibilidad

### 🔒 Autenticación Segura (Google Colab)
La interacción entre el entorno de Google Colab y este repositorio remoto se realiza mediante un **Token de Acceso Personal (PAT)** de GitHub. 
*   Las credenciales se inyectan de forma privada utilizando la API `google.colab.userdata`.
*   Se configuró de forma exitosa la identidad global de Git de la desarrolladora, evitando la exposición de contraseñas o tokens dentro de las celdas públicas del notebook.

### 📁 Estructura General del Proyecto
El repositorio sigue un esquema de arquitectura organizada por responsabilidades para facilitar su auditoría y mantenimiento:

```text
├── datos/                   # Datasets y fuentes de información (CSV/Excel)
├── resultados/              # Reportes generados, gráficos y exportaciones
├── scripts/                 # Módulos auxiliares de código Python (.py)
├── .gitignore               # Archivo de exclusión de Git para entornos Colab/Python
└── README.md                # Documentación técnica principal del sistema
```

### ⚡ Guía de Reproducción Rápida
1. Almacenar el token de GitHub en el apartado **Secrets** (ícono de llave en Colab) bajo el nombre de variable `GH_PAT`.
2. Abrir el entorno de desarrollo y ejecutar secuencialmente las celdas de configuración de entorno.
3. El sistema gestionará automáticamente el montaje del repositorio y las dependencias necesarias.

print("¡Archivo README.md creado y guardado con éxito!")
