
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

### 2.9. Primer Commit y publicación en GitHub

**Objetivo:** Registrar y publicar la documentación académica inicial del proyecto mediante Git.

**Procedimiento realizado:**

- Se verificó que GitHub Desktop detectaba únicamente `docs/bitacora_proyecto.md` como archivo nuevo.
- Se prepararon los campos Summary y Description con mensajes descriptivos.
- Se ejecutó `Commit 1 file to main`.
- GitHub Desktop confirmó que existía un commit local pendiente de publicación.
- Se ejecutó `Push origin`.
- Se comprobó la publicación directamente en GitHub.

**Resultados verificados:**

- El archivo `docs/bitacora_proyecto.md` está disponible en el repositorio público.
- GitHub Desktop mostró `No local changes` después del Push.
- La rama utilizada fue `main`.

**Interpretación:**

El Commit registró la documentación en el historial local de Git. Posteriormente, Push publicó ese registro en el repositorio remoto de GitHub.

La verificación desde el navegador confirmó que la documentación quedó accesible públicamente.

**Estado:** Primer ciclo Commit → Push → verificación remota completado.

### 2.10. Verificación inicial de entornos Conda

**Objetivo:** Identificar los entornos Python disponibles antes de preparar un entorno aislado para el proyecto.

**Comando ejecutado en la terminal PowerShell de VS Code:**

```powershell
conda env list
```

**Resultados observados:**

- `base`: entorno principal de Anaconda, disponible.
- `c3_prueba`: entorno independiente creado en prácticas anteriores, disponible.
- Ningún entorno aparece activado.
- `vehicles_env` todavía no existe.

**Interpretación:**

La instalación de Conda reconoce correctamente los entornos existentes. Para el proyecto se utilizará un entorno independiente, evitando modificar innecesariamente `base` o `c3_prueba`.

**Estado:** Verificación inicial completada. Creación del entorno del proyecto pendiente.

### 2.11. Creación y activación del entorno Python del proyecto

**Objetivo:** Crear un entorno Python independiente para desarrollar la aplicación web, manteniendo aisladas sus dependencias de otros proyectos.

**Entorno seleccionado:** `vehicles_env`

**Comando ejecutado en PowerShell:**

```powershell
conda create -n vehicles_env python=3.14
```

**Resultados observados:**

- Conda presentó la transacción de instalación, que fue autorizada.
- `Preparing transaction: done`
- `Verifying transaction: done`
- `Executing transaction: done`
- Se mostraron las instrucciones para activar y desactivar el entorno.

**Advertencias observadas:**

- Aviso sobre el futuro mantenimiento de Python 3.10 en el canal `defaults`.
- Aviso informativo sobre la función experimental `conda-pypi`.

Ninguno impidió completar la creación del entorno.

**Activación:**

```powershell
conda activate vehicles_env
```

**Resultado verificado:**

La terminal integrada de VS Code mostró el prefijo `(vehicles_env)`.

**Interpretación:**

Conda creó un entorno independiente del entorno principal `base` y del entorno de práctica `c3_prueba`.

La activación permite que los comandos Python ejecutados desde esta terminal utilicen el entorno seleccionado. La versión exacta del intérprete y las dependencias disponibles deberán verificarse posteriormente.

**Estado:** Entorno creado y activado correctamente. Verificación del intérprete pendiente.

### 2.12. Verificación del intérprete Python del entorno

**Objetivo:** Comprobar que el entorno `vehicles_env` utiliza su propia instalación de Python y que los comandos ejecutados desde PowerShell no dependen del intérprete del entorno `base`.

**Comando ejecutado:**

```powershell
python -c "import sys; print(sys.version); print(sys.executable)"
```

**Resultados observados:**

- Versión: Python 3.14.8.
- Distribución: Anaconda, Inc.
- Arquitectura: 64 bits (AMD64).
- Intérprete utilizado:

  `C:\Users\victor.hernandezm\AppData\Local\anaconda3\envs\vehicles_env\python.exe`

- Entorno activo en PowerShell: `(vehicles_env)`.

**Interpretación:**

La ruta de `sys.executable` confirma que Python se ejecutó desde el entorno Conda específico del proyecto.

Esto demuestra que el entorno está correctamente activado en la terminal actual. Sin embargo, todavía debemos verificar por separado que VS Code haya seleccionado ese mismo intérprete para ejecutar archivos y notebooks.

**Estado:** Versión e intérprete de Python verificados correctamente.

### 2.13. Selección del intérprete Python en VS Code

**Objetivo:** Configurar VS Code para utilizar el entorno Conda `vehicles_env` del proyecto.

**Procedimiento realizado:**

- Se abrió `Python: Select Interpreter` desde la paleta de comandos.
- Se identificó `vehicles_env (3.14.8)`.
- VS Code mostró inicialmente la advertencia `An Invalid Python interpreter is selected`.
- Se revisaron los canales `Python` y `Python Environments` del panel Output.
- Los registros identificaron `vehicles_env` para el proyecto y `base` para el ámbito global.
- Se confirmó la selección de `vehicles_env` desde el menú de intérpretes.

**Verificación en PowerShell:**

```powershell
python -c "import sys; print(sys.executable)"
```

**Resultado obtenido:**

`C:\Users\victor.hernandezm\AppData\Local\anaconda3\envs\vehicles_env\python.exe`

**Interpretación:**

VS Code identifica `vehicles_env (3.14.8)` como intérprete del proyecto, mientras que la terminal PowerShell ejecuta Python desde ese mismo entorno.

La advertencia inicial no impidió la selección del intérprete. Sin embargo, la verificación realizada confirma la ejecución desde PowerShell, no todavía mediante `Run Python File` de VS Code.

**Estado:** Selección del intérprete y ejecución desde PowerShell verificadas. Prueba directa desde el editor pendiente.

### 2.14. Verificación funcional de Python desde VS Code

**Objetivo:** Confirmar que VS Code ejecuta archivos Python utilizando el intérprete seleccionado para el proyecto C7.

**Archivo de prueba:** `verificar_entorno.py`

**Ubicación:** Raíz del repositorio.

**Código utilizado:**

```python
import sys

print("Versión de Python:", sys.version)
print("Ruta del intérprete:", sys.executable)
```

**Procedimiento:**

- Se creó `verificar_entorno.py` en el proyecto y se ubicó en la raíz del repositorio.
- Se abrió el archivo desde el editor de VS Code.
- Se utilizó el botón `Run Python File`.
- VS Code abrió una terminal denominada `Python` y activó automáticamente `vehicles_env`.

**Resultados verificados:**

- Python 3.14.8, distribuido por Anaconda.
- Entorno activo: `vehicles_env`.
- Ruta del intérprete:

  `C:\Users\victor.hernandezm\AppData\Local\anaconda3\envs\vehicles_env\python.exe`

- El script terminó sin errores.

**Interpretación:**

La prueba confirma que VS Code ejecuta correctamente archivos `.py` mediante el intérprete del entorno aislado `vehicles_env`.

La advertencia inicial sobre un intérprete inválido no impidió esta ejecución. No fue necesario reinstalar Python ni modificar los entornos existentes.

**Estado:** Configuración y ejecución del intérprete verificadas funcionalmente.

**Disposición del archivo temporal:**

Una vez verificada satisfactoriamente la ejecución desde VS Code, se decidió retirar `verificar_entorno.py` de la raíz del proyecto.

El archivo fue enviado a la Papelera de reciclaje porque su función era exclusivamente comprobar la configuración del intérprete Python.

El código, el procedimiento y los resultados de la prueba permanecen documentados en esta sección, permitiendo reproducir la verificación si fuera necesario.

**Estado final:** Prueba funcional completada y archivo temporal retirado del proyecto.

### 2.15. Revisión de cambios y configuración de .gitignore

**Objetivo:** Identificar los archivos pendientes de seguimiento y evitar publicar configuraciones locales innecesarias.

**Diagnóstico inicial:**

En Source Control se identificaron tres archivos:

- `verificar_entorno.py` — Untracked (U).
- `.vscode/settings.json` — Untracked (U).
- `docs/bitacora_proyecto.md` — Modified (M).

Se inspeccionó `.vscode/settings.json` y se comprobó que contenía preferencias del administrador de entornos y paquetes Conda de VS Code, sin credenciales visibles.

**Modificación realizada:**

En `.gitignore` se sustituyó:

```gitignore
# .vscode/
```

Por:

```gitignore
.vscode/
```

**Resultados verificados:**

- `.vscode/settings.json` dejó de aparecer en Source Control.
- `.gitignore` apareció como modificado (M).
- `verificar_entorno.py` permaneció como archivo nuevo (U).
- `docs/bitacora_proyecto.md` permaneció modificado (M).

**Interpretación:**

La regla `.vscode/` indica a Git que ignore los archivos no versionados contenidos en ese directorio.

Esta decisión permite conservar las preferencias locales de VS Code sin incorporarlas al repositorio público.

**Estado:** Exclusión de `.vscode/` verificada. Commit y Push pendientes.

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

- Primer ciclo Commit → Push → verificación en GitHub completado.

- Entorno Conda `vehicles_env` creado y activado.

- Python 3.14.8 verificado.

- Intérprete `vehicles_env` seleccionado en VS Code.

- Ejecución mediante `Run Python File` comprobada satisfactoriamente.

- Configuración de `.gitignore` verificada para excluir `.vscode/`.

- Prueba de ejecución de Python documentada y archivo temporal retirado.

- Revisión de Source Control completada: únicamente `.gitignore` y `docs/bitacora_proyecto.md` presentan modificaciones pendientes.

**Pendiente:**

- Incorporar el dataset al repositorio.

- Crear `notebooks/EDA.ipynb` antes de iniciar el análisis.

- Desarrollar, probar y desplegar la aplicación.

- Registrar y publicar los cambios posteriores de la bitácora.

**Criterio de continuidad:** Cada nueva actividad relevante se documentará y verificará antes de avanzar.