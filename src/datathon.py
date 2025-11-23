# Run in terminal (IF NEEDED)

#pip3 install geopy
#pip3 install ipykernel
#pip3 install matplotlib
#pip3 install numpy
#pip3 install pandas
#pip3 install plotly
#pip3 install scikit-learn
#pip3 install seaborn

# ------------------------
# LIBRERÍAS
# ------------------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle
import json

# ------------------------
# CARGA DE DATOS
# ------------------------
df1 = pd.read_csv('/Users/fernandoarroyo/Desktop/Proyectos Jean-Anna/1.-ZF Datathon - Motortec/Data_Part1_Datathon.csv')
df2 = pd.read_csv('/Users/fernandoarroyo/Desktop/Proyectos Jean-Anna/1.-ZF Datathon - Motortec/Data_Part2_APG_Datathon.csv')

# --- LIMPIEZA DE DATOS (DATA PREPARATION) ---

# Convertir columnas de tiempo de tipo objeto a timedelta
df1['Time'] = pd.to_datetime(df1['Time'])
df1['Bin_Time'] = pd.to_timedelta(df1['Bin_Time'])


df2['time'] = pd.to_timedelta(df2['time'])
df2['start_time'] = pd.to_timedelta(df2['start_time'])

# Eliminar filas donde Odo (odómetro) tenga valores inválidos (-1)
df1 = df1[df1['Odo'] != -1]

# ------------------------
# CREACIÓN DE VARIABLES
# ------------------------

# Odo diff
df1['odo_diff'] = df1.groupby('Trip_Id')['Odo'].diff().fillna(0)

# Time diff
df1['time_diff'] = df1.groupby('Trip_Id')['Time'].diff().dt.total_seconds().fillna(0)

# Fuel diff
df1['fuel_diff'] = df1.groupby('Trip_Id')['Tfu'].diff().fillna(0)

# Distance diff
df1['distance_diff'] = np.sqrt(df1['Latitude'].diff()**2 + df1['Longitude'].diff()**2).fillna(0)

# Average speed (en el viaje)
df1['avg_speed'] = df1.groupby('Trip_Id')['Speed'].transform('mean')

# Average fuel (en el viaje)
df1['avg_fuel'] = df1.groupby('Trip_Id')['Tfu'].transform(lambda x: x.diff().fillna(0).mean())

# Consumo por km (fuel / odo)
df1['consumo_por_km'] = df1['fuel_diff'] / df1['odo_diff'].replace(0, np.nan)
df1['consumo_por_km'] = df1['consumo_por_km'].fillna(0)

# Velocidad por hora
df1['velocidad_por_hora'] = df1['Speed'] * 3.6  # de m/s a km/h

# Hora de inicio
df1['hora_inicio'] = df1['Time'].dt.hour

# ¿Tramo con peaje eliminado?
df1['con_peaje_rapido'] = df1['Is_toll_removed'].apply(lambda x: 0 if x == 1 else 1)

# ------------------------
# SELECCIÓN DE VARIABLES
# ------------------------
features = [
    'Is_toll_removed', 'VehicleCategory', 'Speed', 'Tfu',
    'distance_diff', 'time_diff', 'fuel_diff', 'avg_speed',
    'consumo_por_km', 'velocidad_por_hora', 'hora_inicio',
    'con_peaje_rapido'
]
target = 'avg_fuel'

X = df1[features]
y = df1[target]

# ------------------------
# DIVISIÓN TRAIN/TEST
# ------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ------------------------
# ENTRENAMIENTO DEL MODELO
# ------------------------
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# ------------------------
# EVALUACIÓN DEL MODELO
# ------------------------
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Evaluación del modelo Gradient Boosting:")
print(f"MAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")

# ------------------------
# GUARDAR MODELO
# ------------------------
with open('modelo_script_gradient_boosting.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Modelo guardado como 'modelo_script_gradient_boosting.pkl'")

# ------------------------
# GUARDAR PREDICCIONES
# ------------------------
predicciones_dict = [
    {"real": real, "predicha": pred}
    for real, pred in zip(y_test.values, y_pred)
]

with open('predicciones_script_avg_fuel.json', 'w') as f:
    json.dump(predicciones_dict, f, indent=4)
print("Predicciones guardadas en 'predicciones_script_avg_fuel.json'")