# ======================================================
# PESTAÑA DE RESULTADOS LSTM — DASHBOARD DENGUE
# ======================================================

import pandas as pd
import os
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px

# ======================================================
# CONFIGURACIÓN DE RUTAS
# ======================================================

BASE_RESULTS = "/home/guirlessa/Dashboard_Dengue/data/"
HISTORY_DIR = os.path.join(BASE_RESULTS, "history")
METRICS_DIR = os.path.join(BASE_RESULTS, "metrics")
PREDICTIONS_DIR = os.path.join(BASE_RESULTS, "predictions")

# ======================================================
# COORDENADAS DE DEPARTAMENTOS (sin shapefile)
# ======================================================

DEPT_COORDS = {
    "Amazonas": {"lat": -3.7, "lon": -70.0},
    "Antioquia": {"lat": 7.0, "lon": -75.5},
    "Arauca": {"lat": 6.8, "lon": -70.8},
    "Atlántico": {"lat": 10.8, "lon": -75.0},
    "Bolívar": {"lat": 9.0, "lon": -74.0},
    "Boyacá": {"lat": 5.5, "lon": -73.3},
    "Caldas": {"lat": 5.0, "lon": -75.5},
    "Caquetá": {"lat": 0.8, "lon": -74.0},
    "Casanare": {"lat": 5.8, "lon": -71.8},
    "Cauca": {"lat": 2.5, "lon": -76.6},
    "Cesar": {"lat": 9.8, "lon": -73.5},
    "Chocó": {"lat": 5.7, "lon": -77.0},
    "Córdoba": {"lat": 8.3, "lon": -75.8},
    "Cundinamarca": {"lat": 4.8, "lon": -74.3},
    "Guainía": {"lat": 2.5, "lon": -68.9},
    "Guaviare": {"lat": 2.0, "lon": -72.8},
    "Huila": {"lat": 2.8, "lon": -75.3},
    "La Guajira": {"lat": 11.0, "lon": -72.9},
    "Magdalena": {"lat": 10.0, "lon": -74.2},
    "Meta": {"lat": 3.5, "lon": -73.5},
    "Nariño": {"lat": 1.2, "lon": -77.3},
    "Norte de Santander": {"lat": 8.0, "lon": -72.5},
    "Putumayo": {"lat": 0.5, "lon": -76.0},
    "Quindío": {"lat": 4.5, "lon": -75.7},
    "Risaralda": {"lat": 5.0, "lon": -75.8},
    "Santander": {"lat": 7.0, "lon": -73.0},
    "Sucre": {"lat": 9.0, "lon": -75.0},
    "Tolima": {"lat": 4.0, "lon": -75.2},
    "Valle del Cauca": {"lat": 3.5, "lon": -76.5},
    "Vaupés": {"lat": 0.5, "lon": -70.8},
    "Vichada": {"lat": 5.0, "lon": -68.0}
}

# ======================================================
# FUNCIÓN DE CARGA DE DATOS
# ======================================================

def safe_read(path, empty_cols=None):
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        print(f"⚠️ Archivo no encontrado: {path}")
        return pd.DataFrame(columns=empty_cols if empty_cols else [])

def cargar_datos_lstm():
    global_metrics = safe_read(os.path.join(METRICS_DIR, "global_metrics.csv"))

    history_files = [f for f in os.listdir(HISTORY_DIR) if f.endswith(".csv")]
    history_dfs = []
    for file in history_files:
        df = pd.read_csv(os.path.join(HISTORY_DIR, file))
        df["archivo"] = file
        history_dfs.append(df)
    history_df = pd.concat(history_dfs, ignore_index=True) if history_dfs else pd.DataFrame()

    prediction_files = [f for f in os.listdir(PREDICTIONS_DIR) if f.endswith(".csv")]
    prediction_dfs = []
    for file in prediction_files:
        df = pd.read_csv(os.path.join(PREDICTIONS_DIR, file))
        df["archivo"] = file
        prediction_dfs.append(df)
    predictions_df = pd.concat(prediction_dfs, ignore_index=True) if prediction_dfs else pd.DataFrame()

    return global_metrics, history_df, predictions_df

# ======================================================
# CARGA INICIAL
# ======================================================

global_metrics, history_df, predictions_df = cargar_datos_lstm()

# ======================================================
# MAPA DE VALORES REALES VS PREDICHOS
# ======================================================

def crear_mapa_predicciones(predictions_df):
    if predictions_df.empty:
        return px.scatter_mapbox(title="No hay datos de predicciones disponibles")

    resumen = predictions_df.groupby("departamento")[["y_true", "y_pred"]].mean().reset_index()
    resumen["lat"] = resumen["departamento"].map(lambda d: DEPT_COORDS.get(d, {}).get("lat"))
    resumen["lon"] = resumen["departamento"].map(lambda d: DEPT_COORDS.get(d, {}).get("lon"))
    resumen["error"] = resumen["y_true"] - resumen["y_pred"]

    fig = px.scatter_mapbox(
        resumen,
        lat="lat",
        lon="lon",
        hover_name="departamento",
        hover_data={"y_true": True, "y_pred": True, "error": True},
        color="error",
        color_continuous_scale="RdBu",
        size="y_true",
        title="Mapa de Valores Reales vs Predichos (Error = y_true - y_pred)",
        zoom=4,
        center={"lat": 4.5, "lon": -74.0},
        height=600
    )

    fig.update_layout(mapbox_style="carto-positron", margin={"r":0,"t":50,"l":0,"b":0})
    return fig

# ======================================================
# LAYOUT DE LA PESTAÑA
# ======================================================

def layout():
    return dbc.Container([
        html.H2("Resultados del Modelo LSTM", style={"color": "#0B3C5D", "fontWeight": "bold"}),
        html.Hr(),

        html.H4("Métricas Globales", style={"marginTop": "20px"}),
        dash_table.DataTable(
            data=global_metrics.to_dict("records"),
            columns=[{"name": i, "id": i} for i in global_metrics.columns],
            style_table={"overflowX": "auto"},
            style_cell={"textAlign": "center", "padding": "5px"},
            page_size=10
        ),

        html.H4("Historial de Entrenamiento por Seed y Año", style={"marginTop": "40px"}),
        dash_table.DataTable(
            data=history_df.to_dict("records"),
            columns=[{"name": i, "id": i} for i in history_df.columns],
            style_table={"overflowX": "auto"},
            style_cell={"textAlign": "center", "padding": "5px"},
            page_size=10
        ),

        html.H4("Mapa de Valores Reales vs Predichos", style={"marginTop": "40px"}),
        dcc.Graph(figure=crear_mapa_predicciones(predictions_df))
    ], fluid=True)
