# Consumo Combustible AP7

Este proyecto tiene como objetivo construir un modelo de regresión para predecir el **consumo medio de combustible (`avg_fuel`)** en trayectos de vehículos pesados. Para ello, se utilizaron datos de telemetría, distancia recorrida, velocidad, diferencias horarias, consumo acumulado y variables derivadas.


## Objetivo del Proyecto

El objetivo es estudiar si existe un impacto medible en el consumo de combustible y la velocidad tras la eliminación de peajes en la AP-7, y construir un modelo predictivo que permita estimar el consumo medio por viaje, ayudando a optimizar la eficiencia logística de las flotas.


## ¿Qué problema soluciona?

El consumo de combustible representa uno de los mayores costes operativos para las empresas de transporte. Evaluar el impacto de políticas públicas (como la eliminación de peajes) permite tomar decisiones estratégicas para rutas, horarios y planificación de flotas.


## Contexto

El Datathon ZF – Motortec propone analizar telemetría real de flotas de camiones conectadas a través de la tecnología ZF SCALAR. A partir de datos antes y después de eliminar los peajes en la autopista AP-7, se busca entender cómo influye esta medida en el comportamiento de conducción y el rendimiento energético de los vehículos pesados ￼.


## Datos utilizados
- Data_Part1_Datathon.csv: Datos de telemetría por segundo de vehículos (velocidad, odómetro, consumo, GPS, tiempo, etc.) para cada viaje (Trip_Id) a lo largo de la AP-7.
- Data_Part2_APG_Datathon.csv: Datos agregados por tramos de 10 km y franjas horarias, que contienen velocidad media y consumo medio (avg_fuel, avg_speed) a lo largo de la ruta Tarragona–Girona.

**Variables clave:**
- Is_toll_removed: indica si el peaje fue eliminado (1) o no (0).
- Tfu: combustible total utilizado.
- Speed, Odo, Time, Trip_Id, Latitude, Longitude.

**Preprocesamiento aplicado:**
- Conversión de tiempos (Time, Bin_Time, start_time) a formatos legibles.
- Cálculo de variables nuevas: odo_diff, fuel_diff, avg_speed, consumo_por_km, velocidad_por_hora, hora_inicio, etc.
- Filtrado de datos inválidos (e.g., odómetro con valor -1).


## Metodología
**1.	EDA (Exploratory Data Analysis):**
- Limpieza y transformación de los datos.
- Visualización de consumo y velocidad según Is_toll_removed.
- Comparación por tramos: Tarragona–Barcelona y Barcelona–Girona.
- Test de hipótesis (Welch’s t-test) para validar diferencias en el consumo.

**2.	Modelado Predictivo:**
- Modelo Gradient Boosting Regressor entrenado con variables seleccionadas.
- Métricas obtenidas:
- MAE: 0.0005
- RMSE: 0.0030
- R²: 1.000

**3.	Exportación de resultados:**
- Modelo serializado (.pkl).
- Predicciones guardadas como .json.

## Estructura del repositorio
```bash
Consumo_combustible_AP7/
│
├── data/
│   └── raw/                            # Datos originales
│       ├── Data_Part1_Datathon.csv
│       └── Data_Part2_APG_Datathon.csv
│
├── models/                             # Modelos entrenados
│   └── modelo_gradient_boosting.pkl
│
├── notebook/                           # Notebook principal del proyecto
│   └── EDA.ipynb
│
├── predictions/                        # Resultados del modelo
│   └── predicciones_avg_fuel.json
│
├── src/                                # Scripts Python
│   └── datathon.py
│
├── .gitignore                          # Exclusiones para control de versiones
└── README.md                           # Este documento
```

## Tecnologías y Librerías
- Lenguaje: Python 3.10
- Librerías principales:
- pandas, numpy: procesamiento de datos
- matplotlib, seaborn: visualización
- scikit-learn: modelado (Gradient Boosting Regressor)
- pickle, json: serialización
- Visualización final: Power BI
- Editor: VSCode


## Resultados y Conclusiones
- Se identificó una reducción significativa en el consumo de combustible tras la eliminación de peajes.
- La velocidad media también aumentó ligeramente.
- El tramo Barcelona–Girona presentó el impacto más positivo.
- El modelo predictivo mostró un ajuste perfecto (R² ≈ 1.0), aunque este resultado podría deberse a la naturaleza del dataset y debe interpretarse con cautela.

## Posibles mejoras y próximos pasos
- Añadir más días de datos para mejorar la robustez de los análisis.
- Incluir nuevas variables como peso de la carga o condiciones climáticas.
- Desplegar el modelo como API o en una interfaz de usuario interactiva.
- Comparar con otros modelos más complejos (XGBoost, CatBoost).
- Refinar la visualización en Power BI incluyendo alertas, mapas de calor y predicciones del modelo.


## Autor
Proyecto desarrollado por Fernando Arroyo como práctica de limpieza y exploración de datos en Python. Todo esto no hubiese sido posible sin la supervición, guía y motivación de uno de los grandes prodijios de la Ciencia de datos, Jean Charles.
  
LinkedIn: [Contáctame por LinkedIn](www.linkedin.com/in/f-arroyo-herrera)