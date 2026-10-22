import os
import base64
import subprocess

def to_base64(filepath):
    with open(filepath, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

# Paths
base_dir = r"c:\Users\USER\Documents\Ingenieria de sistemas\6 Semestre\Inteligencia Artificial\Clase 9\clase9"
img_diag = to_base64(os.path.join(base_dir, "src", "diagnostico_clase8.png"))
img_curva = to_base64(os.path.join(base_dir, "src", "curva_aprendizaje.png"))
img_front = to_base64(os.path.join(base_dir, "src", "frontera_decision.png"))

# Read perceptron_reto.py
with open(os.path.join(base_dir, "src", "perceptron_reto.py"), "r", encoding="utf-8") as f:
    codigo_perceptron = f.read()

salida_consola = """Datos: X tiene forma (120, 2) | y tiene forma (120,)

[OK] RETO 1 (vectorización) superado
[OK] RETO 2 (función sigmoide) superado
[OK] RETO 3 (función de pérdida) superado
[OK] RETO 4A (gradientes) superado
[OK] RETO 4B (actualización de pesos) superado
Época   1 | Pérdida: 0.6931 | Exactitud: 54.17% | w=[0.028, -0.025] b=0.004
Época 100 | Pérdida: 0.3183 | Exactitud: 90.83% | w=[1.333, -1.180] b=0.181
Época 200 | Pérdida: 0.2675 | Exactitud: 90.83% | w=[1.849, -1.651] b=0.237
Época 300 | Pérdida: 0.2467 | Exactitud: 90.83% | w=[2.180, -1.957] b=0.270
Época 400 | Pérdida: 0.2353 | Exactitud: 90.00% | w=[2.426, -2.184] b=0.295
Época 500 | Pérdida: 0.2281 | Exactitud: 90.00% | w=[2.622, -2.366] b=0.315

RESULTADO: pérdida final 0.2281 | exactitud 90.00%
Pesos finales: w1=2.6217, w2=-2.3658, b=0.3152

[OK] RETO 5 (preparación de las entradas) superado
Gráfico guardado: curva_aprendizaje.png
[OK] RETO 6 (frontera de decisión) superado
Gráfico guardado: frontera_decision.png
[OK] RETO 7 (predicción de lotes nuevos) superado
Lluvia 220.0 mm | Temp 23.5 °C -> 99.48% -> EXITOSA
Lluvia  60.0 mm | Temp 30.0 °C -> 0.11% -> NO EXITOSA
Lluvia 150.0 mm | Temp 26.0 °C -> 55.65% -> EXITOSA

*** ¡Todos los retos superados! Perceptrón completo construido desde cero. ***"""

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Informe Actividad Grupal Clase 9</title>
<style>
  @page {{
    size: letter;
    margin: 18mm 16mm 18mm 16mm;
    @bottom-right {{
      content: counter(page);
    }}
  }}
  body {{
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    color: #1e293b;
    line-height: 1.5;
    font-size: 10pt;
    margin: 0;
    padding: 0;
  }}
  h1, h2, h3, h4 {{
    color: #0f172a;
    font-weight: 700;
  }}
  .header-box {{
    border-bottom: 2px solid #2563eb;
    padding-bottom: 12px;
    margin-bottom: 18px;
  }}
  .header-title {{
    font-size: 17pt;
    font-weight: 800;
    color: #1e3a8a;
    margin: 0 0 4px 0;
  }}
  .header-sub {{
    font-size: 10.5pt;
    color: #475569;
    margin: 0;
  }}
  .meta-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
    font-size: 9pt;
  }}
  .meta-table th, .meta-table td {{
    border: 1px solid #cbd5e1;
    padding: 6px 10px;
  }}
  .meta-table th {{
    background-color: #f1f5f9;
    color: #334155;
    text-align: left;
    width: 28%;
    font-weight: 600;
  }}
  .section-title {{
    font-size: 12pt;
    color: #1e40af;
    border-left: 4px solid #2563eb;
    padding-left: 8px;
    margin-top: 22px;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    page-break-after: avoid;
  }}
  .question-box {{
    background-color: #f8fafc;
    border-left: 3px solid #3b82f6;
    padding: 8px 12px;
    margin-bottom: 10px;
    page-break-inside: avoid;
  }}
  .question-text {{
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 4px;
    font-size: 9.5pt;
  }}
  .answer-text {{
    color: #334155;
    margin: 0;
    text-align: justify;
  }}
  .data-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
  }}
  .data-table th, .data-table td {{
    border: 1px solid #cbd5e1;
    padding: 6px 8px;
    text-align: left;
  }}
  .data-table th {{
    background-color: #1e3a8a;
    color: #ffffff;
    font-weight: 600;
  }}
  .data-table tr:nth-child(even) {{
    background-color: #f8fafc;
  }}
  .tag-role {{
    display: inline-block;
    padding: 2px 6px;
    font-size: 7.5pt;
    font-weight: 700;
    border-radius: 4px;
    text-transform: uppercase;
  }}
  .role-coord {{ background-color: #dbeafe; color: #1e40af; }}
  .role-verif {{ background-color: #dcfce7; color: #166534; }}
  .role-prog {{ background-color: #fef3c7; color: #92400e; }}
  .role-relat {{ background-color: #f3e8ff; color: #6b21a8; }}
  .img-container {{
    text-align: center;
    margin: 14px 0;
    page-break-inside: avoid;
  }}
  .img-container img {{
    max-width: 82%;
    height: auto;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
    box-shadow: 0 2px 4px rgba(0,0,0,0.06);
  }}
  .img-caption {{
    font-size: 8pt;
    color: #64748b;
    margin-top: 4px;
    font-style: italic;
  }}
  .grid-2 {{
    display: flex;
    gap: 12px;
    margin: 12px 0;
    page-break-inside: avoid;
  }}
  .grid-col {{
    flex: 1;
    text-align: center;
  }}
  .grid-col img {{
    max-width: 100%;
    height: auto;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
  }}
  pre, code {{
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8pt;
  }}
  pre.code-block {{
    background-color: #0f172a;
    color: #e2e8f0;
    padding: 8px 10px;
    border-radius: 6px;
    overflow-x: auto;
    line-height: 1.22;
    margin: 6px 0;
    font-size: 7.2pt;
    page-break-inside: auto;
  }}
  .badge-success {{
    background-color: #10b981;
    color: white;
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 8pt;
  }}
  .badge-danger {{
    background-color: #ef4444;
    color: white;
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 8pt;
  }}
  .badge-warning {{
    background-color: #f59e0b;
    color: white;
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 8pt;
  }}
  .page-break {{
    page-break-before: always;
  }}
</style>
</head>
<body>

  <!-- ENCABEZADO -->
  <div class="header-box">
    <div style="float: right; text-align: right; font-size: 8.5pt; color: #64748b;">
      <strong>COTECNOVA</strong><br>
      Ingeniería de Sistemas · Semestre 6<br>
      Docente: Jhon James Cano Sánchez
    </div>
    <div class="header-title">Informe — Actividad Grupal Clase 9</div>
    <div class="header-sub">Construcción Completa del Perceptrón con Descenso del Gradiente (Caso Cultivos Cartago)</div>
  </div>

  <!-- METADATOS DEL GRUPO -->
  <table class="meta-table">
    <tr>
      <th>Campo</th>
      <td><strong>Respuesta</strong></td>
    </tr>
    <tr>
      <th>Grupo N.° / Fecha</th>
      <td>Grupo 05 · Lunes 19 de octubre de 2026</td>
    </tr>
    <tr>
      <th>Coordinador(a)</th>
      <td><span class="tag-role role-coord">Coordinador</span> Esteban Gómez — Liderazgo de tiempo, vocería docente y programación de Retos 1 y 2</td>
    </tr>
    <tr>
      <th>Programador(a)</th>
      <td><span class="tag-role role-prog">Programador</span> Heiber González — Entorno Docker, descenso del gradiente (Reto 4B) y estandarización (Reto 5)</td>
    </tr>
    <tr>
      <th>Verificador(a)</th>
      <td><span class="tag-role role-verif">Verificador</span> Integrante del Grupo — Validación de puntos de control, función de pérdida (Reto 3) y gradientes (Reto 4A)</td>
    </tr>
    <tr>
      <th>Relator(a)</th>
      <td><span class="tag-role role-relat">Relator</span> Integrante del Grupo — Redacción del informe, frontera de decisión (Reto 6) y lotes nuevos (Reto 7)</td>
    </tr>
  </table>

  <!-- SECCIÓN 1: DIAGNÓSTICO -->
  <div class="section-title">1. Diagnóstico (Misión 0) — Evaluación de la Neurona de la Clase 8</div>

  <div class="question-box">
    <div class="question-text">1. ¿La neurona llega a cero errores? ¿Qué pasa con los errores de una época a otra?</div>
    <p class="answer-text"><strong>No llega a cero errores.</strong> Inicia en la época 1 con 50 errores de 120 lotes y, a medida que avanzan las épocas, oscila erráticamente entre 29 y 35 errores por época, culminando en la época 30 con 31 errores (exactitud de apenas 77.50%). Esto sucede porque los datos agrícolas reales contienen ruido natural no lineal (no son perfectamente separables por un corte rígido) y porque el algoritmo de la compuerta AND modifica sus pesos de manera individual y desproporcionada tras cada error.</p>
  </div>

  <div class="question-box">
    <div class="question-text">2. ¿Qué ocurre con el tamaño de los pesos w1 y w2 a medida que avanzan las épocas? ¿Por qué?</div>
    <p class="answer-text"><strong>Ocurre una explosión desbalanceada de los pesos.</strong> Partiendo de <code>w1 = 0.1</code> y <code>w2 = 0.1</code>, terminan en <code>w1 = 33.86</code> y <code>w2 = -139.20</code>, mientras que el sesgo apenas alcanza <code>b = 3.60</code>. La causa es que las entradas no están estandarizadas: la precipitación alcanza valores de hasta 260 mm y la temperatura de hasta 31 °C. Al aplicar la regla <code>w += tasa * error * x</code>, cada error genera saltos drásticos de hasta ±26 unidades en un solo paso, haciendo que los pesos oscilen y nunca converjan.</p>
  </div>

  <div class="question-box">
    <div class="question-text">3. Para el lote de 150 mm y 26 °C la neurona responde 1. ¿Qué tan segura está? ¿Le sirve a la cooperativa?</div>
    <p class="answer-text"><strong>No podemos saber qué tan segura está.</strong> La función escalón solo entrega una respuesta binaria rígida (0 o 1). Justo en 150 mm y 26 °C el cultivo se ubica exactamente en el umbral de máxima incertidumbre (~50% de probabilidad real). Una respuesta determinista sin grado de certeza <strong>no le sirve a la cooperativa</strong>, ya que los agrónomos necesitan cuantificar el riesgo para priorizar visitas técnicas en los lotes más críticos.</p>
  </div>

  <div class="question-box">
    <div class="question-text">4. La neurona recorre los lotes uno por uno. ¿Qué pasaría con 1 millón de lotes?</div>
    <p class="answer-text">Con 1 millón de lotes y 30 épocas, Python puro tendría que ejecutar <strong>30 millones de iteraciones en ciclos <code>for</code> secuenciales</strong>. Esto causaría un tiempo de cómputo inaceptable y bloqueante. Es indispensable sustituir ciclos iterativos por <strong>álgebra matricial vectorizada con NumPy</strong>, aprovechando operaciones vectoriales optimizadas en C a nivel de hardware.</p>
  </div>

  <div class="img-container">
    <img src="{img_diag}" alt="Gráfico Diagnóstico Clase 8">
    <div class="img-caption">Figura 1: Curva de errores de la neurona de la Clase 8 con datos reales de Cartago (diagnostico_clase8.png). Se aprecia la oscilación constante y la imposibilidad de converger a cero.</div>
  </div>

  <div class="question-box" style="border-left-color: #8b5cf6;">
    <div class="question-text">5. Hipótesis del grupo — ¿Qué le falta a la neurona de la Clase 8 para funcionar con datos reales?</div>
    <p class="answer-text">Planteamos que la neurona carece de cinco componentes estructurales:
    <br><strong>a) Vectorización:</strong> Reemplazar ciclos por multiplicación de matrices (<code>X @ w + b</code>) para procesar todos los lotes a la vez.
    <br><strong>b) Activación Sigmoide:</strong> Cambiar el escalón por una curva suave que mapee los puntajes a probabilidades continuas entre 0 y 1.
    <br><strong>c) Pérdida Logarítmica (Entropía Cruzada):</strong> Medir matemáticamente el error probabilístico, castigando fuertemente predicciones erróneas seguras.
    <br><strong>d) Descenso del Gradiente:</strong> Promediar el vector gradiente sobre el lote completo y actualizar los parámetros en sentido opuesto al error.
    <br><strong>e) Estandarización de Variables:</strong> Escalar precipitación y temperatura a media 0 y desviación estándar 1 para garantizar un aprendizaje equilibrado.</p>
  </div>

  <div class="page-break"></div>

  <!-- SECCIÓN 2: BITÁCORA DE RETOS -->
  <div class="section-title">2. Bitácora de Retos (Construcción del Perceptrón)</div>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 14%;">Reto</th>
        <th style="width: 13%;">Piloto</th>
        <th style="width: 25%;">¿Qué faltaba?</th>
        <th style="width: 24%;">¿Cómo lo descubrieron?</th>
        <th style="width: 24%;">Código & Evidencia</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>RETO 1</strong><br>Vectorización</td>
        <td><span class="tag-role role-coord">Coordinador</span></td>
        <td>Calcular la suma ponderada \(z = Xw + b\) de los 120 lotes en una línea sin ciclos <code>for</code>.</td>
        <td>Consultando la Clase 4 de NumPy: el operador <code>@</code> realiza producto matriz-vector.</td>
        <td>
          <code>return X @ w + b</code><br>
          <span style="color:#16a34a; font-weight:700;">[OK] RETO 1 superado</span>
        </td>
      </tr>
      <tr>
        <td><strong>RETO 2</strong><br>Sigmoide</td>
        <td><span class="tag-role role-coord">Coordinador</span></td>
        <td>Una función continua diferenciable que transforme \(z\) en probabilidad entre 0 y 1.</td>
        <td>Aplicando σ(z) = 1/(1+e^-z) con <code>np.exp(-z)</code>; en z=0 da 0.5.</td>
        <td>
          <code>return 1 / (1 + np.exp(-z))</code><br>
          <span style="color:#16a34a; font-weight:700;">[OK] RETO 2 superado</span>
        </td>
      </tr>
      <tr>
        <td><strong>RETO 3</strong><br>Pérdida</td>
        <td><span class="tag-role role-verif">Verificador</span></td>
        <td>Función de pérdida probabilística (Binary Cross-Entropy) que penalice predicciones dudosas o falsas.</td>
        <td>Fórmula de entropía cruzada con <code>np.log</code> y promedio <code>-np.mean(...)</code>.</td>
        <td>
          <code>-np.mean(y*np.log(p)+(1-y)*np.log(1-p))</code><br>
          <span style="color:#16a34a; font-weight:700;">[OK] RETO 3 superado</span>
        </td>
      </tr>
      <tr>
        <td><strong>RETO 4A</strong><br>Gradientes</td>
        <td><span class="tag-role role-verif">Verificador</span></td>
        <td>Cálculo analítico de derivadas de pérdida respecto a \(w\) y \(b\) promediadas sobre los lotes.</td>
        <td>Calculando <code>error = y_prob - y_real</code> y proyectando con transpuesta <code>X.T @ error / n</code>.</td>
        <td>
          <code>gw = (X.T @ error) / len(y)</code><br>
          <code>gb = np.mean(error)</code><br>
          <span style="color:#16a34a; font-weight:700;">[OK] RETO 4A superado</span>
        </td>
      </tr>
      <tr>
        <td><strong>RETO 4B</strong><br>Descenso Gradiente</td>
        <td><span class="tag-role role-prog">Programador</span></td>
        <td>Paso de actualización iterativa de pesos moviéndose cuesta abajo contra el gradiente.</td>
        <td>Restando la tasa multiplicada por el gradiente: <code>w = w - lr * gw</code>.</td>
        <td>
          <code>w -= tasa * gradiente_w</code><br>
          <code>b -= tasa * gradiente_b</code><br>
          <span style="color:#16a34a; font-weight:700;">[OK] RETO 4B superado</span>
        </td>
      </tr>
      <tr>
        <td><strong>RETO 5</strong><br>Estandarización</td>
        <td><span class="tag-role role-prog">Programador</span></td>
        <td>Escalar características mediante Z-score (media 0, desviación 1) antes de entrenar.</td>
        <td>Al correr sin escalar salió <code>overflow in exp</code> y pérdida de 5.28; aplicamos <code>(X-media)/desv</code>.</td>
        <td>
          <code>media = X.mean(axis=0)</code><br>
          <code>desv = X.std(axis=0)</code><br>
          <code>X_esc = (X - media) / desv</code><br>
          <span style="color:#16a34a; font-weight:700;">[OK] RETO 5 superado</span>
        </td>
      </tr>
      <tr>
        <td><strong>RETO 6</strong><br>Frontera Decisión</td>
        <td><span class="tag-role role-relat">Relator</span></td>
        <td>Despejar matemáticamente la recta en el plano donde la neurona duda totalmente (\(z=0\)).</td>
        <td>De \(w_1 x_1 + w_2 x_2 + b = 0\), despejamos \(x_2 = -(w_1 x_1 + b)/w_2\).</td>
        <td>
          <code>x2_esc = -(w[0]*x1_esc + b)/w[1]</code><br>
          <span style="color:#16a34a; font-weight:700;">[OK] RETO 6 superado</span>
        </td>
      </tr>
      <tr>
        <td><strong>RETO 7</strong><br>Lotes Nuevos</td>
        <td><span class="tag-role role-relat">Relator</span></td>
        <td>Preparar lotes nunca antes vistos utilizando los parámetros de entrenamiento aprendidos.</td>
        <td>Restando la media y dividiendo entre la desviación calculadas en el Reto 5.</td>
        <td>
          <code>(lotes_nuevos - media) / desviacion</code><br>
          <span style="color:#16a34a; font-weight:700;">[OK] RETO 7 superado</span>
        </td>
      </tr>
    </tbody>
  </table>

  <!-- SECCIÓN 3: RESULTADOS -->
  <div class="section-title">3. Resultados — Impacto de la Estandarización y Validación</div>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 25%;">Métrica / Parámetro</th>
        <th style="width: 37%;">Antes del Reto 5 (Datos Crudos)</th>
        <th style="width: 38%;">Después del Reto 5 (Datos Estandarizados Z-Score)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Pérdida Inicial (Época 1)</strong></td>
        <td>0.6931</td>
        <td>0.6931</td>
      </tr>
      <tr>
        <td><strong>Pérdida Final (Época 500)</strong></td>
        <td><span class="badge-danger">5.2830</span> (Divergencia / Degeneración)</td>
        <td><span class="badge-success">0.2281</span> (Convergencia óptima suave)</td>
      </tr>
      <tr>
        <td><strong>Exactitud Final</strong></td>
        <td>74.17% (89/120 aciertos)</td>
        <td><strong>90.00%</strong> (108/120 lotes clasificados con éxito)</td>
      </tr>
      <tr>
        <td><strong>Pesos Finales (w1 / w2 / b)</strong></td>
        <td>w1 = 3.3155 | w2 = -25.2997 | b = 0.1440</td>
        <td><strong>w1 = +2.6217 | w2 = -2.3658 | b = +0.3152</strong></td>
      </tr>
      <tr>
        <td><strong>Advertencias Numéricas</strong></td>
        <td><code>RuntimeWarning: overflow encountered in exp</code></td>
        <td><strong>Ninguna</strong> (Cálculo numérico completamente estable)</td>
      </tr>
    </tbody>
  </table>

  <div class="grid-2">
    <div class="grid-col">
      <img src="{img_curva}" alt="Curva de aprendizaje">
      <div class="img-caption">Figura 2: Curva de aprendizaje del modelo estandarizado (curva_aprendizaje.png). Se aprecia el descenso asintótico de la pérdida y la estabilización de exactitud en 90%.</div>
    </div>
    <div class="grid-col">
      <img src="{img_front}" alt="Frontera de decisión">
      <div class="img-caption">Figura 3: Frontera de decisión lineal en el plano real (frontera_decision.png). Separa con gran fidelidad lotes exitosos (verdes) de no exitosos (naranjas).</div>
    </div>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 25%;">Lote Nuevo Evaluado</th>
        <th style="width: 20%;">Probabilidad Estimada</th>
        <th style="width: 15%;">Decisión</th>
        <th style="width: 40%;">Interpretación Agronómica para Cartago</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>220.0 mm / 23.5 °C</strong></td>
        <td><strong style="color:#16a34a;">99.48%</strong></td>
        <td><span class="badge-success">EXITOSA</span></td>
        <td>Condiciones ideales: abundante precipitación y clima templado. Prioridad baja de asistencia.</td>
      </tr>
      <tr>
        <td><strong>60.0 mm / 30.0 °C</strong></td>
        <td><strong style="color:#dc2626;">0.11%</strong></td>
        <td><span class="badge-danger">NO EXITOSA</span></td>
        <td>Déficit hídrico severo combinado con calor extremo. Prioridad crítica urgente de asistencia agronómica.</td>
      </tr>
      <tr>
        <td><strong>150.0 mm / 26.0 °C</strong></td>
        <td><strong style="color:#d97706;">55.65%</strong></td>
        <td><span class="badge-warning">EXITOSA (Dudosa)</span></td>
        <td>Lote en plena frontera de decisión (incertidumbre). Requiere visita técnica preventiva para desempatar el riesgo.</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- SECCIÓN 4: INTERPRETACIÓN -->
  <div class="section-title">4. Interpretación Agronómica y Técnica</div>

  <div class="question-box">
    <div class="question-text">¿Qué significa el signo de w1 y de w2 para un agricultor de Cartago?</div>
    <p class="answer-text">
      El signo refleja la relación biológica aprendida por la neurona:
      <br>• <strong>\(w_1 = +2.6217\) (Signo Positivo):</strong> Indica que ante mayor precipitación mensual, el puntaje \(z\) aumenta exponencialmente, elevando la probabilidad de éxito de la cosecha.
      <br>• <strong>\(w_2 = -2.3658\) (Signo Negativo):</strong> Indica que temperaturas más elevadas disminuyen el puntaje, actuando como un factor perjudicial (estrés hídrico y térmico).
      <br>• <strong>Magnitudes comparables:</strong> Como las variables fueron estandarizadas, comparar sus valores absol (\(2.62\) vs \(2.36\)) demuestra que la lluvia y la temperatura ejercen un peso casi idéntico en el desenlace del cultivo en la zona de Cartago.
    </p>
  </div>

  <div class="question-box">
    <div class="question-text">¿Qué cambió con el Reto 5 y por qué?</div>
    <p class="answer-text">
      Antes del Reto 5 las características tenían escalas muy dispares (precipitación en centenas, temperatura en decenas). Los gradientes asociados a la lluvia eran enormes, generando pasos gigantescos que catapultaban los pesos hacia valores infinitos e hicieron colapsar la función exponencial (<code>RuntimeWarning: overflow in exp</code>), provocando una pérdida aberrante de 5.2830. Al aplicar estandarización Z-score, la superficie de costo se convirtió en un tazón simétrico, permitiendo que el gradiente descendiera uniformemente hacia el mínimo global con pérdida de 0.2281 y 90% de exactitud.
    </p>
  </div>

  <!-- SECCIÓN 5: EXPERIMENTO -->
  <div class="section-title">5. Experimento Final — Análisis de Hiperparámetros y Lotes Adicionales</div>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 25%;">Experimento Elegido</th>
        <th style="width: 25%;">Qué se Modificó</th>
        <th style="width: 25%;">Resultado Obtenido</th>
        <th style="width: 25%;">Conclusión del Experimento</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Experimento C<br>(Lote 4 Adicional)</strong><br><em>Principal</em></td>
        <td>Se evaluó el lote adicional <code>[100.0 mm, 28.0 °C]</code> estandarizado con la media y desviación de los 120 lotes.</td>
        <td><strong>Probabilidad: 2.84%</strong><br>Decisión: <span class="badge-danger">NO EXITOSA</span><br>Riesgo: 97.16% de probabilidad de fracaso.</td>
        <td>Demuestra la utilidad predictiva: permite a la cooperativa agendar asistencia técnica prioritaria antes de iniciar la siembra para mitigar el calor y sequía.</td>
      </tr>
      <tr>
        <td><strong>Experimento A<br>(Tasa de Aprendizaje)</strong><br><em>Comparativo</em></td>
        <td>Se evaluó \(\alpha = 0.001\) y \(\alpha = 1.0\) durante 500 épocas.</td>
        <td>Con \(\alpha=0.001\): Pérdida final de 0.6289.<br>Con \(\alpha=1.0\): Pérdida final de 0.2050 (90.00% exactitud).</td>
        <td>Con datos estandarizados, una tasa mayor converge sin desbordarse; una tasa ínfima (0.001) aprende con lentitud inaceptable.</td>
      </tr>
      <tr>
        <td><strong>Experimento B<br>(Número de Épocas)</strong><br><em>Comparativo</em></td>
        <td>Se comparó el entrenamiento a 20 épocas vs 3000 épocas.</td>
        <td>Con 20 épocas: Pérdida 0.5021.<br>Con 3000 épocas: Pérdida 0.2055 (90.83% exactitud).</td>
        <td>Entrenar 3000 épocas no aporta ventaja frente a 500 (pérdida 0.2281 vs 0.2055); la curva se aplana después de la época 350.</td>
      </tr>
    </tbody>
  </table>

  <!-- SECCIÓN 6: HIPÓTESIS VS REALIDAD -->
  <div class="section-title">6. Hipótesis vs. Realidad</div>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 35%;">Lo que creíamos que faltaba (Misión 0)</th>
        <th style="width: 65%;">¿Era necesario? ¿Por qué?</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Vectorización en NumPy</td>
        <td><strong>Totalmente indispensable.</strong> Permitió calcular simultáneamente 120 lotes con álgebra matricial, reduciendo el código a <code>X @ w + b</code> sin ciclos for lentos.</td>
      </tr>
      <tr>
        <td>Función Sigmoide</td>
        <td><strong>Completamente necesaria.</strong> Proporcionó una función continua diferenciable con gradiente no nulo y salidas interpretables como probabilidades del 0 al 100%.</td>
      </tr>
      <tr>
        <td>Pérdida por Entropía Cruzada</td>
        <td><strong>Esencial.</strong> Evaluó con precisión la incertidumbre probabilística, castigando asintóticamente las suposiciones equivocadas.</td>
      </tr>
      <tr>
        <td>Estandarización Z-Score</td>
        <td><strong>El factor más crítico.</strong> Sin escalado, los gradientes colapsaron la función exponencial y generaron desbordamientos numéricos.</td>
      </tr>
    </tbody>
  </table>

  <div class="question-box">
    <div class="question-text">Lo que no nos imaginábamos que faltaba:</div>
    <p class="answer-text">
      No anticipamos que, incluso teniendo matemáticamente impecables la Sigmoide, los Gradientes y la Entropía Cruzada, el modelo empeorara su desempeño si no se normalizaban las entradas antes del entrenamiento. Tampoco teníamos en cuenta que los lotes nuevos no deben estandarizarse calculando una media propia, sino que <strong>deben transformarse estrictamente con la media y desviación del conjunto de entrenamiento</strong> para preservar el espacio dimensional aprendido.
    </p>
  </div>

  <!-- SECCIÓN 7: CONCLUSIONES -->
  <div class="section-title">7. Conclusiones y Pregunta Abierta</div>
  <ol style="margin: 0; padding-left: 20px; font-size: 9.5pt; color: #334155; line-height: 1.6;">
    <li><strong>De la neurona lógica al clasificador probabilístico:</strong> El reemplazo de la función escalón de McCulloch-Pitts por la activación Sigmoide convierte al perceptrón en una herramienta rigurosa para la toma de decisiones bajo incertidumbre en entornos productivos reales.</li>
    <li><strong>El preprocesamiento es tan determinante como la arquitectura:</strong> La estandarización de variables (Z-score) no es un paso cosmético; es una necesidad matemática indispensable para garantizar una superficie de error simétrica y convergencia sin desbordamientos de punto flotante.</li>
    <li><strong>Interpretabilidad agronómica directa:</strong> A diferencia de modelos de caja negra, los pesos del perceptrón brindan interpretabilidad explícita: los signos y magnitudes relativas (\(w_1 = +2.62\) y \(w_2 = -2.36\)) traducen de forma transparente el impacto de los factores climáticos para los campesinos de la región.</li>
  </ol>

  <div class="question-box" style="margin-top: 14px; border-left-color: #f59e0b;">
    <div class="question-text">Pregunta que nos queda abierta:</div>
    <p class="answer-text">
      <em>¿Qué ocurriría en un escenario climático no lineal, por ejemplo si un exceso extremo de precipitación (> 300 mm) causara inundación y pudrición de raíces, provocando que tanto poca lluvia como demasiada lluvia arruinen la cosecha? En tal caso, una frontera de decisión lineal simple como la del perceptrón no podría separar las regiones; ¿cuántas neuronas y capas ocultas (MLP) requeriríamos para aprender fronteras curvas cerradas?</em>
    </p>
  </div>

  <div class="page-break"></div>

  <!-- ANEXO: CÓDIGO Y SALIDA -->
  <div class="section-title">Anexo: Código Fuente Completo y Salida de Consola</div>

  <p style="font-size: 8.5pt; font-weight: 700; color: #475569; margin: 0 0 6px 0;">Código Fuente Resuelto: <code>src/perceptron_reto.py</code> (con etiquetas oficiales por rol)</p>
  <pre class="code-block"><code>{codigo_perceptron}</code></pre>

  <p style="font-size: 8.5pt; font-weight: 700; color: #475569; margin: 12px 0 6px 0;">Salida de Consola al Ejecutar <code>python perceptron_reto.py</code></p>
  <pre class="code-block" style="background-color: #030712; color: #34d399;"><code>{salida_consola}</code></pre>

</body>
</html>
"""

html_path = os.path.join(base_dir, "informe_render.html")
pdf_path_clase9 = os.path.join(base_dir, "Informe_Clase9_GrupoX.pdf")
pdf_path_root = os.path.join(r"c:\Users\USER\Documents\Ingenieria de sistemas\6 Semestre\Inteligencia Artificial\Clase 9", "Informe_Clase9_GrupoX.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML temporal creado en {html_path}")

# Run Edge headless to print to PDF
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path_clase9}",
    html_path
]

print("Generando PDF con Edge headless...")
subprocess.run(cmd, check=True)
print(f"PDF generado con éxito en: {pdf_path_clase9}")

# Copy to root Clase 9 folder as well
import shutil
shutil.copy2(pdf_path_clase9, pdf_path_root)
print(f"PDF copiado a: {pdf_path_root}")
