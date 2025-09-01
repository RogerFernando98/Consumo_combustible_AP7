Proyecto de Predicción del Consumo de Combustible – Datathon ZF

Este proyecto forma parte del reto propuesto en el Datathon ZF – Motortec. El objetivo principal fue predecir el consumo medio de combustible (avg_fuel) por parte de vehículos pesados en tramos de la AP-7, utilizando datos reales de telemetría.


Objetivo del Proyecto

Desarrollar un modelo de machine learning que prediga el consumo medio de combustible de un trayecto, utilizando variables como la velocidad media, distancia recorrida, tiempo, tipo de vehículo y si ha pasado por un tramo con peaje eliminado.


Estructura del Proyecto
	1.	Business Understanding
	•	Definición del objetivo: predecir consumo para mejorar eficiencia y sostenibilidad.
	2.	Data Understanding
	•	Análisis inicial de dos datasets (df1 y df2) con datos GPS, temporales y de combustible.
	•	Limpieza de datos: eliminación de valores Odo = -1, transformación de tiempos (timedelta), tratamiento de nulos y detección de duplicados.
	3.	Data Preparation
	•	Feature Engineering: se crean nuevas variables como:
	•	avg_speed, avg_fuel, consumo_por_km, velocidad_por_hora, hora_inicio, con_peaje_rapido.
	•	Matriz de correlación: se eliminaron variables altamente correlacionadas (Time, Bin_Time, m_marker, etc.).
	•	Revisión de baja varianza: ninguna variable fue eliminada porque todas mostraban suficiente variabilidad.
	•	Preparación del conjunto final de variables (features) para el modelo.
	4.	Modelado
	•	División train/test: 70% entrenamiento, 30% test.
	•	Torneo de modelos con:
	•	LinearRegression
	•	DecisionTreeRegressor
	•	RandomForestRegressor
	•	GradientBoostingRegressor
	•	Modelo ganador: Gradient Boosting
	•	MAE: 0.0245
	•	RMSE: 0.90
	•	R²: 0.5789
	5.	Interpretación con SHAP
	•	Variables más importantes:
	•	consumo_por_km
	•	distance_diff
	•	distanceMarker
	•	Se generaron gráficos SHAP beeswarm y bar plot para visualizar impacto de cada variable.
	6.	Exportación
	•	Se guardó el modelo entrenado en un archivo .pkl con pickle.
	•	Se exportaron las predicciones reales vs. predichas en un archivo .json.


Resultados
	•	El modelo logra explicar aproximadamente el 58% de la variabilidad del consumo de combustible, lo que se considera un buen resultado dado el tipo de datos y las condiciones reales del transporte.
	•	Se identificaron patrones clave en el consumo como:
	•	Mayor consumo en tramos más largos.
	•	Alta relación entre consumo_por_km y avg_fuel.



Ejemplo de predicciones

{
  "real": 0.1296,
  "predicha": 0.1012
}


💼 Herramientas utilizadas
	•	Python (Pandas, NumPy, Scikit-learn, SHAP, Matplotlib)
	•	Jupyter Notebook
	•	Pickle / JSON


📂 Archivos del proyecto
	•	datathon.ipynb → Notebook con todo el proceso completo
	•	modelo_gradient_boosting.pkl → Modelo entrenado
	•	predicciones_avg_fuel.json → Predicciones reales vs. predichas