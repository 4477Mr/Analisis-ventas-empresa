# # #  Trabajo Práctico: Gestión Colaborativa, Control de Versiones y Organización Empresarial
##  Análisis de Ventas - Pequeña Empresa

##  Descripción del Proyecto
En la ingeniería de software moderna y la organización de procesos productivos, la capacidad de registrar, revisar y coordinar cambios en un equipo distribuido es un pilar fundamental para garantizar la trazabilidad y la calidad. En este informe integramos la gestión de proyectos y el control de versiones bajo el paradigma de Aprendizaje Basado en Problemas (ABP).

---

##  I. Gestión Organizacional y Trazabilidad (Jira - GitHub)
Este proyecto sigue una metodología ágil gestionada en Jira, vinculando cada cambio en el código con un ticket específico.

*   **Enlace al Tablero Jira: https://regnermaria579-1778628575092.atlassian.net/jira/software/projects/OE/boards/34**
*   **Estrategia de Ramas:** Se utiliza el flujo de trabajo de GitFeature Branch. Está prohibido pushear directamente a `main`.

### Tabla de Trazabilidad de Tareas

| ID Ticket Jira | Tarea / Característica | Rama en GitHub | Estado Actual |
| :--- | :--- | :--- | :--- |
| **PROY-1** | Configuración de entorno Colab | `feature/config-colab` | Completado |
| **PROY-2** | Desarrollo del algoritmo principal | `feature/algoritmo-core` | En Progreso |

>  **Nota de Trazabilidad:** Todos los commits deben iniciar con el ID del ticket (Ej: `git commit -m "PROY-1: Configuración de PAT en Colab"`).

---

##  II. Control de Versiones (Flujo Git & Evidencias)

### Historial de Ramas y Pull Requests (PRs)
El desarrollo se organiza en ramas de características que se integran a `main` exclusivamente mediante Pull Requests revisados.

*   **Rama Principal:** `main` (Código estable y listo para ejecución).
*   **Historial de Commits Significativos:** [Inserta captura de pantalla o texto del comando `git log --oneline` que demuestre los mensajes con el ID de Jira].
*   **Evidencia de Pull Requests:** [Inserta aquí una captura de pantalla de la sección "Pull Requests" de GitHub que muestre la revisión antes de fusionar].

---

##  III. Implementación Técnica y Reproducibilidad

### Entorno en Google Colab
La autenticación se realiza de forma segura mediante un **Token de Acceso Personal (PAT)** de GitHub, configurando la identidad global sin exponer credenciales en las celdas públicas del notebook.

### Estructura del Repositorio
```text
├── .gitignore               # Archivo de exclusión de Git
├── README.md                # Documentación principal del proyecto
├── notebooks/               # Archivos de Google Colab (.ipynb)
│   └── proyecto_main.ipynb
├── src/                     # Código fuente modularizado (.py)
│   └── utils.py
└── requirements.txt         # Dependencias del proyecto para reproducibilidad
```

### Guía de Ejecución Rápida
1. Abrir el notebook alojado en `notebooks/proyecto_main.ipynb` en Google Colab.
2. Crear un archivo de entorno o utilizar los *Secrets* de Colab para almacenar el `GH_PAT`.
3. Ejecutar las celdas en orden secuencial.

!git commit -m "Cambios en readme.md"

!git push origin {rama}
print(f"🚀 Código enviado con éxito a la rama {rama}")
