
# Bitácora académica — Proyecto Sprint 7

## 1. Introducción

**Programa:** Bootcamp de Ciencia de Datos — Tripleten  

**Módulo:** Herramientas de desarrollo de software  

**Sprint:** 7  

**Proyecto:** Dashboard interactivo de anuncios de vehículos

### 1.1. Objetivo

Documentar el proceso de construcción, validación y despliegue de una aplicación web desarrollada con Python, pandas, Plotly y Streamlit, utilizando Git/GitHub para el control de versiones y Render para su publicación.

### 1.2. Metodología documental

Esta bitácora registra las decisiones técnicas, operaciones realizadas, resultados observados, dificultades y soluciones aplicadas.

El análisis exploratorio y sus interpretaciones se documentarán por separado en `notebooks/EDA.ipynb`.

---

## 2. Fase 0 — Preparación del proyecto

**Fecha de las actividades:** 26 de octubre de 2026.

### 2.1. Identificación del dataset

**Archivo:** `vehicles_us.csv`

**Ubicación original verificada:**

`C:\Users\victor.hernandezm\Documents\B ACAD\TRIPLETEN\M1 Python básico\Sprint7\C7.1 Proyecto`

**Resultado:** Se confirmó visualmente la existencia del archivo.

**Observación:** Todavía no se han inspeccionado sus dimensiones, columnas ni contenido.

### 2.2. Definición del repositorio

**Nombre aprobado:** `tripleten-s7-c7-vehicles-dashboard`

Se decidió crear un repositorio público independiente de los repositorios utilizados durante los capítulos anteriores.

### 2.3. Creación del repositorio remoto

**Plataforma:** GitHub  

**Cuenta:** `vmhernann110177`  

**Rama principal:** `main`

**Configuración inicial:**

- Visibilidad: Public.

- README.md: habilitado.

- .gitignore: plantilla Python.

- Licencia: No license.

**URL:**

https://github.com/vmhernann110177/tripleten-s7-c7-vehicles-dashboard


**Verificación:** GitHub mostró el repositorio público con ambos archivos iniciales y un commit.

### 2.4. Preparación del directorio local

Se aprobó la ubicación:

`C:\Users\victor.hernandezm\tripleten_s7\C7_Proyecto\tripleten-s7-c7-vehicles-dashboard`

**Comando ejecutado en PowerShell:**

```powershell

New-Item -ItemType Directory -Path "$HOME\tripleten_s7\C7_Proyecto" -Force

```

**Resultado:** Se creó correctamente la carpeta contenedora `C7_Proyecto`.

### 2.5. Clonación del repositorio

**Comando ejecutado:**

```powershell

git clone https://github.com/vmhernann110177/tripleten-s7-c7-vehicles-dashboard.git "$HOME\tripleten_s7\C7_Proyecto\tripleten-s7-c7-vehicles-dashboard"

```

**Resultado verificado:**

`Receiving objects: 100% (4/4), done.`

**Interpretación:** Git descargó correctamente el repositorio remoto y creó su copia local.

Se conservará una sola copia local para trabajar con VS Code y GitHub Desktop.

### 2.6. Apertura del proyecto en VS Code

**Comando ejecutado:**

```powershell

code "$HOME\tripleten_s7\C7_Proyecto\tripleten-s7-c7-vehicles-dashboard"

```

**Resultado:** VS Code abrió el proyecto y mostró `README.md` y `.gitignore` en Explorer.

### 2.7. Inicio de la documentación académica

Se creó la carpeta `docs` y el archivo:

`docs/bitacora_proyecto.md`

**Propósito:** Mantener un registro académico del desarrollo de software, separado del análisis exploratorio.

### 2.8. Integración con GitHub Desktop

**Objetivo:**

Integrar GitHub Desktop al flujo de desarrollo utilizando la misma copia local del repositorio que se encuentra abierta en VS Code.

**Procedimiento realizado:**

- Se abrió GitHub Desktop.
- Se seleccionó `File → Add local repository`.
- Se indicó la ruta local del proyecto previamente clonado.
- No se realizó una segunda clonación.

**Resultados verificados:**

- GitHub Desktop reconoció el repositorio `tripleten-s7-c7-vehicles-dashboard`.
- La rama activa es `main`.
- Se detectó un archivo nuevo: `docs/bitacora_proyecto.md`.
- El indicador `1 changed file` corresponde a un cambio local que todavía no se ha incorporado mediante un commit.

**Interpretación:**

GitHub Desktop y VS Code trabajan sobre el mismo repositorio local. Los archivos creados desde VS Code son reconocidos por Git, aunque todavía no se hayan publicado en GitHub.

La ausencia de líneas rojas no significa que no existan cambios. Las líneas verdes representan contenido añadido.

**Estado:** Integración local completada. Commit y Push pendientes.

---

## 3. Estado actual

**Completado:**

- Dataset localizado.

- Repositorio público creado.

- Rama principal identificada.

- Carpeta local preparada.

- Repositorio clonado.

- Proyecto abierto en VS Code.

- Archivo de bitácora creado.

- GitHub Desktop integrado con la misma copia local del repositorio.

**Pendiente:**

- Preparar y verificar el entorno Python del proyecto.

- Incorporar el dataset al repositorio.

- Crear `notebooks/EDA.ipynb` antes de iniciar el análisis.

- Desarrollar, probar y desplegar la aplicación.

**Criterio de continuidad:** Cada nueva actividad relevante se documentará y verificará antes de avanzar.