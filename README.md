# 🔍 Predicción del Consumo de Combustible con Machine Learning

Este proyecto tiene como objetivo construir un modelo de regresión para predecir el **consumo medio de combustible (`avg_fuel`)** en trayectos de vehículos pesados. Para ello, se utilizaron datos de telemetría, distancia recorrida, velocidad, diferencias horarias, consumo acumulado y variables derivadas.

---

## 🧠 Objetivo del Proyecto

- Predecir el consumo medio de combustible (`avg_fuel`) en función de variables relacionadas con la conducción.
- Identificar las variables más influyentes en el consumo.
- Obtener un modelo interpretable y útil para apoyar decisiones de eficiencia o sostenibilidad.

---

## 🧱 Estructura del Proyecto
├── datathon.ipynb                  # Notebook principal con todo el flujo de trabajo

├── datathon.py                    # Versión en script Python (opcional)

├── modelo_gradient_boosting.pkl   # Modelo entrenado y guardado (pickle)

├── predicciones_avg_fuel.json     # Predicciones reales vs. predichas

├── Datathon_definición_reto.pdf   # Descripción del reto original (sin datos sensibles)

└── .gitignore                     # Evita subir archivos innecesarios como .csv

> ❗ Los archivos `.csv` con datos crudos **no están incluidos** por razones de confidencialidad. El proyecto funciona a partir del `df1` ya procesado.

---

## 🧪 Flujo del Proyecto

### 1. Carga y exploración de datos
- Se trabajó principalmente con un único DataFrame (`df1`) que incluía información de posiciones GPS, velocidades, odómetros, consumo acumulado (`Tfu`), etc.
- Se crearon variables nuevas como:
  - `consumo_por_km = avg_fuel / distanceMarker`
  - `velocidad_por_hora = distanceMarker / time_diff`
  - `con_peaje_rapido = (Is_toll_removed == 0) & (avg_speed > 90)`

### 2. Limpieza y preparación
- Se imputaron nulos, eliminaron duplicados y se eliminaron columnas con **alta correlación** (corr > 0.85).
- Se revisaron posibles columnas con **baja varianza**, pero no fue necesario eliminarlas.

### 3. Selección de variables
- Se seleccionaron 12 variables relevantes para el modelo basadas en el análisis de correlación y sentido del negocio.

### 4. División del dataset
- División 70% entrenamiento / 30% test usando `train_test_split`.

### 5. Torneo de modelos (model competition)
Se compararon cuatro modelos usando MAE, RMSE y R² como métricas:

| Modelo              | MAE     | RMSE    | R²       |
|---------------------|---------|---------|----------|
| Linear Regression   | 0.0665  | 1.3896  | 0.0032   |
| Decision Tree       | 0.0129  | 0.9530  | 0.5311   |
| Random Forest       | 0.0110  | 0.9164  | 0.5664   |
| **Gradient Boosting** | **0.0245** | **0.9031** | **0.5789** |

> 🔝 **Gradient Boosting** fue seleccionado como el modelo ganador por su mejor equilibrio entre precisión y capacidad explicativa (R² más alto).

### 6. Interpretabilidad con SHAP
- Se utilizó `shap` para analizar la importancia de cada variable en el modelo.
- Las 3 variables más influyentes fueron:
  - `consumo_por_km` (+0.27 SHAP mean)
  - `distance_diff` (+0.17 SHAP mean)
  - `distanceMarker` (+0.10 SHAP mean)

### 7. Exportación de resultados
- Modelo guardado como `.pkl` con `pickle`.
- Predicciones exportadas a `.json` en formato:

```json
[
  { "real": 0.1296, "predicha": 0.1012 },
  { "real": 0.0303, "predicha": 0.0323 },
  ...
]



📈 Métrica final del modelo

El modelo de Gradient Boosting alcanzó un R² de 0.579, lo que significa que explica aproximadamente el 58% de la variabilidad en el consumo de combustible. Considerando la naturaleza ruidosa de los datos reales de telemetría, es un resultado robusto y valioso para la toma de decisiones estratégicas.

📚 Librerías utilizadas
	•	pandas, numpy, matplotlib, seaborn
	•	scikit-learn: modelos y métricas
	•	shap: interpretabilidad
	•	pickle y json: exportación de modelo y predicciones
