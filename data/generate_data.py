"""
generate_data.py
Genera datos sintéticos de incidencia de dengue por departamento en Colombia.
Simula series de tiempo semanales con patrones estacionales y espaciales realistas.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

# ── Semilla de reproducibilidad ──────────────────────────────────────────────
np.random.seed(42)

# ── Departamentos de Colombia con características base ───────────────────────
DEPARTAMENTOS = {
    "Antioquia":       {"base": 120, "lat": 7.19,  "lon": -75.34, "region": "Andina"},
    "Valle del Cauca": {"base": 100, "lat": 3.80,  "lon": -76.64, "region": "Pacífica"},
    "Atlántico":       {"base": 90,  "lat": 10.69, "lon": -74.87, "region": "Caribe"},
    "Bolívar":         {"base": 85,  "lat": 8.67,  "lon": -74.03, "region": "Caribe"},
    "Santander":       {"base": 75,  "lat": 6.64,  "lon": -73.65, "region": "Andina"},
    "Cundinamarca":    {"base": 60,  "lat": 4.60,  "lon": -74.08, "region": "Andina"},
    "Córdoba":         {"base": 95,  "lat": 8.35,  "lon": -75.89, "region": "Caribe"},
    "Tolima":          {"base": 80,  "lat": 4.09,  "lon": -75.15, "region": "Andina"},
    "Meta":            {"base": 70,  "lat": 3.99,  "lon": -73.56, "region": "Orinoquía"},
    "Cesar":           {"base": 88,  "lat": 9.33,  "lon": -73.66, "region": "Caribe"},
    "Norte de Santander": {"base": 72, "lat": 7.89, "lon": -72.50, "region": "Andina"},
    "Magdalena":       {"base": 83,  "lat": 10.47, "lon": -74.41, "region": "Caribe"},
    "Huila":           {"base": 68,  "lat": 2.53,  "lon": -75.53, "region": "Andina"},
    "Cauca":           {"base": 55,  "lat": 2.45,  "lon": -76.61, "region": "Pacífica"},
    "Nariño":          {"base": 50,  "lat": 1.21,  "lon": -77.28, "region": "Pacífica"},
    "Risaralda":       {"base": 65,  "lat": 5.31,  "lon": -76.02, "region": "Andina"},
    "Caldas":          {"base": 58,  "lat": 5.29,  "lon": -75.26, "region": "Andina"},
    "Quindío":         {"base": 52,  "lat": 4.46,  "lon": -75.66, "region": "Andina"},
    "Boyacá":          {"base": 40,  "lat": 5.45,  "lon": -73.36, "region": "Andina"},
    "Sucre":           {"base": 78,  "lat": 8.81,  "lon": -74.72, "region": "Caribe"},
    "La Guajira":      {"base": 65,  "lat": 11.35, "lon": -72.52, "region": "Caribe"},
    "Caquetá":         {"base": 60,  "lat": 1.61,  "lon": -75.61, "region": "Amazonía"},
    "Putumayo":        {"base": 55,  "lat": 0.43,  "lon": -76.64, "region": "Amazonía"},
    "Chocó":           {"base": 45,  "lat": 5.69,  "lon": -76.65, "region": "Pacífica"},
    "Arauca":          {"base": 62,  "lat": 7.08,  "lon": -70.76, "region": "Orinoquía"},
    "Vichada":         {"base": 30,  "lat": 4.42,  "lon": -70.03, "region": "Orinoquía"},
    "Casanare":        {"base": 55,  "lat": 5.76,  "lon": -71.58, "region": "Orinoquía"},
    "Guainía":         {"base": 25,  "lat": 2.58,  "lon": -68.53, "region": "Amazonía"},
    "Vaupés":          {"base": 20,  "lat": 0.86,  "lon": -70.81, "region": "Amazonía"},
    "Amazonas":        {"base": 22,  "lat": -1.00, "lon": -71.94, "region": "Amazonía"},
    "San Andrés":      {"base": 18,  "lat": 12.53, "lon": -81.72, "region": "Caribe"},
    "Guaviare":        {"base": 35,  "lat": 2.57,  "lon": -72.64, "region": "Amazonía"},
}


def patron_estacional(semana: int) -> float:
    """
    Genera un patrón estacional realista para dengue en Colombia.
    Pico en semanas 1-15 (primer semestre) y 35-52 (lluvias fin de año).
    """
    angulo = 2 * np.pi * semana / 52
    base = 1.0 + 0.6 * np.sin(angulo - np.pi / 4)
    pico_extra = 0.3 * np.exp(-((semana - 45) ** 2) / (2 * 8 ** 2))
    return max(0.3, base + pico_extra)


def generar_serie_departamento(nombre: str, info: dict, fechas: list) -> pd.DataFrame:
    """
    Genera la serie temporal de casos de dengue para un departamento.
    Incluye tendencia, estacionalidad, ruido y brotes ocasionales.
    """
    n = len(fechas)
    registros = []

    tendencia = np.linspace(0.9, 1.1, n)  # Ligera tendencia al alza
    base = info["base"]

    for i, fecha in enumerate(fechas):
        semana_del_año = fecha.isocalendar()[1]
        factor_estacional = patron_estacional(semana_del_año)
        factor_tendencia = tendencia[i]

        # Brote epidémico aleatorio (5% probabilidad)
        brote = np.random.exponential(scale=base * 0.8) if np.random.rand() < 0.05 else 0

        # Ruido gaussiano
        ruido = np.random.normal(0, base * 0.12)

        casos = base * factor_estacional * factor_tendencia + brote + ruido
        casos = max(0, int(round(casos)))

        # Variables climáticas y socioeconómicas correlacionadas
        temperatura = np.random.normal(26 + 2 * np.sin(2 * np.pi * semana_del_año / 52), 1.5)
        precipitacion = max(0, np.random.normal(120 * factor_estacional, 30))
        humedad = np.random.normal(72, 8)
        indice_urbanizacion = np.random.normal(0.65, 0.05)
        indice_pobreza = np.random.normal(0.38, 0.07)
        cobertura_salud = np.random.normal(0.72, 0.06)

        registros.append({
            "fecha": fecha,
            "semana_epidemiologica": semana_del_año,
            "año": fecha.year,
            "departamento": nombre,
            "region": info["region"],
            "latitud": info["lat"],
            "longitud": info["lon"],
            "casos": casos,
            "temperatura_media": round(temperatura, 1),
            "precipitacion_mm": round(precipitacion, 1),
            "humedad_relativa": round(humedad, 1),
            "indice_urbanizacion": round(indice_urbanizacion, 3),
            "indice_pobreza": round(indice_pobreza, 3),
            "cobertura_salud": round(cobertura_salud, 3),
        })

    return pd.DataFrame(registros)


def generar_dataset_completo(años: int = 5) -> pd.DataFrame:
    """
    Genera el dataset completo para todos los departamentos y el rango de años indicado.
    """
    fecha_inicio = datetime(2019, 1, 7)  # Primera semana epidemiológica 2019
    fecha_fin = datetime(2019 + años, 1, 6)

    # Generar fechas semanales
    fechas = []
    f = fecha_inicio
    while f <= fecha_fin:
        fechas.append(f)
        f += timedelta(weeks=1)

    dfs = []
    for nombre, info in DEPARTAMENTOS.items():
        df_dep = generar_serie_departamento(nombre, info, fechas)
        dfs.append(df_dep)

    df = pd.concat(dfs, ignore_index=True)
    df = df.sort_values(["fecha", "departamento"]).reset_index(drop=True)

    # Agregar columnas derivadas
    df["tasa_incidencia"] = (df["casos"] / 100000 * 100).round(2)  # Por 100k hab aprox
    df["semana_str"] = df["fecha"].dt.strftime("SE%U-%Y")

    return df


if __name__ == "__main__":
    print("Generando dataset sintético de dengue en Colombia...")
    df = generar_dataset_completo(años=5)

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/dengue_colombia.csv", index=False)

    print(f"Dataset generado: {df.shape[0]:,} registros × {df.shape[1]} columnas")
    print(f"Departamentos: {df['departamento'].nunique()}")
    print(f"Rango: {df['fecha'].min().date()} → {df['fecha'].max().date()}")
    print(f"Total de casos simulados: {df['casos'].sum():,}")
    print("\nPrimeras filas:")
    print(df.head())