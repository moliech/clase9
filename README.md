# 🌱 Clase 9 — Construcción del Perceptrón Completo (Cooperativa Agrícola Cartago)

Repositorio de la **Actividad Grupal de la Clase 9** de Inteligencia Artificial (Ingeniería de Sistemas). Incluye el entorno Docker, los scripts de Python resueltos con asignación por roles, los gráficos generados, la plantilla del informe y una **Guía Interactiva en HTML** explicada desde cero para todo el equipo.

---

## 📥 1. Cómo Descargar el Proyecto

Puedes descargarlo de **dos formas**:

### Opción 1: Clonar con Git (Recomendado en WSL o Terminal)
Abre tu terminal (PowerShell o `wsl`) en la carpeta donde guardas tus clases de IA y ejecuta:

```bash
git clone https://github.com/moliech/clase9.git
cd clase9
```

### Opción 2: Descargar como archivo `.ZIP` (Sin usar comandos)
1. En la página de GitHub (`https://github.com/moliech/clase9`), haz clic en el botón verde **`<> Code`**.
2. Selecciona **`Download ZIP`**.
3. Descomprime la carpeta en tu computador.

---

## 📖 2. Abrir la Guía Interactiva del Equipo (¡Empiecen por aquí!)

Antes de ejecutar nada, abran el archivo **`Guia_Interactiva_Clase9_Perceptron.html`** haciendo **doble clic** sobre él (se abrirá en Chrome/Edge/Firefox).

Allí encontrarán:
1. **Explicación sencilla desde cero** de qué hace el perceptrón y un simulador interactivo de la función Sigmoide.
2. **Qué debe hacer, programar y responder cada Rol** (`Coordinador`, `Verificador`, `Programador`, `Relator`) si el profesor pregunta en la mesa.
3. **Código paso a paso de los 7 retos** con botón de copiar.
4. **Todas las respuestas listas** para que el **Relator(a)** diligencie `Plantilla_Informe_Clase9.docx`.

---

## 🚀 3. Cómo Ejecutar el Código

Puedes correr el proyecto con **Docker** (como indica el PDF de la clase) o **directamente con Python**.

### Método A: Con Docker en WSL (Flujo oficial de la guía)

1. Abre PowerShell, entra a WSL (`wsl`) y ubícate dentro de la carpeta `clase9`:
   ```bash
   cd clase9
   ```
2. Si tienes un contenedor de la clase anterior encendido, apágalo primero:
   ```bash
   docker compose down
   ```
3. Levanta el contenedor de la Clase 9:
   ```bash
   docker compose up -d --build
   ```
4. Entra al contenedor y ve a la carpeta `src`:
   ```bash
   docker exec -it python_ia bash
   cd src
   ```
5. Ejecuta los 3 scripts en orden:
   ```bash
   # 1. Generar los 120 lotes simulados en ../data/cultivos_cartago.csv
   python generar_datos.py

   # 2. Misión 0: Diagnóstico de la neurona de la Clase 8 (genera diagnostico_clase8.png)
   python neurona_clase8.py

   # 3. Misiones 1 a 7: Perceptrón completo (genera curva_aprendizaje.png y frontera_decision.png)
   python perceptron_reto.py
   ```

---

### Método B: Directo con Python (Sin Docker)

Si ya tienes Python instalado con `numpy`, `pandas` y `matplotlib`:

```bash
cd src
python generar_datos.py
python neurona_clase8.py
python perceptron_reto.py
```

*(Si necesitas instalar las librerías primero: `pip install -r requirements.txt`)*.

---

## 👥 4. Distribución de Roles en `src/perceptron_reto.py`

El archivo `src/perceptron_reto.py` ya tiene los 7 retos resueltos y marcados con el comentario del rol que los digitó:

| Rol | Etiqueta en el código | Retos asignados en el teclado |
| :--- | :--- | :--- |
| **Coordinador(a)** | `# [Coordinador]` | **RETO 1** (`suma_ponderada`) y **RETO 2** (`sigmoide`) |
| **Verificador(a)** | `# [Verificador]` | **RETO 3** (`calcular_perdida`) y **RETO 4A** (`calcular_gradientes`) |
| **Programador(a)** | `# [Programador]` | **RETO 4B** (actualización de `w` y `b`) y **RETO 5** (estandarización `X_esc`) |
| **Relator(a)** | `# [Relator]` | **RETO 6** (`x2_esc` frontera de decisión) y **RETO 7** (`lotes_nuevos_esc`) |

---

## 📂 5. Estructura del Repositorio

```text
clase9/
├── Guia_Interactiva_Clase9_Perceptron.html  # Guía visual e interactiva para el grupo
├── Plantilla_Informe_Clase9.docx            # Plantilla de Word para el informe grupal
├── Actividad_Grupal_Clase_9.pdf             # Guía oficial del docente
├── Dockerfile                               # Imagen Python 3.12 para el contenedor
├── docker-compose.yml                       # Servicio python_ia con volúmenes montados
├── requirements.txt                         # Librerías (numpy, pandas, matplotlib, etc.)
├── data/
│   └── cultivos_cartago.csv                 # Dataset generado (120 lotes)
└── src/
    ├── generar_datos.py                     # Generador del dataset
    ├── neurona_clase8.py                    # Script de diagnóstico (Misión 0)
    ├── perceptron_reto.py                   # Perceptrón completo con los 7 retos superados
    ├── diagnostico_clase8.png               # Gráfico de errores de la Misión 0
    ├── curva_aprendizaje.png                # Gráfico de pérdida y exactitud por época
    └── frontera_decision.png                # Gráfico de la frontera de decisión
```
