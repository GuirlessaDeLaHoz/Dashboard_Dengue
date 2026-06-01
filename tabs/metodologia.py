"""
tabs/metodologia.py
Pestaña: Metodología y arquitectura del modelado espacio-temporal.
"""

import dash_bootstrap_components as dbc
from dash import html

def layout():
    return dbc.Container([
        
        # ─── ENCABEZADO METODOLÓGICO DE ALTO IMPACTO (TÍTULO MAXIMIZADO) ───
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Span(
                        "PREDICCIÓN ESPACIO-TEMPORAL DE LA INCIDENCIA DE DENGUE",
                        className="sup-title fw-bold d-block mb-2", 
                        style={"color": "#475569", "font-size": "1.1rem", "letter-spacing": "1.5px", "font-weight": "800"}
                    ),
                    html.H1(
                        "Metodología del Proyecto", 
                        className="section-title-main fw-bold", 
                        style={
                            "font-weight": "900", 
                            "color": "#000000", 
                            "font-size": "3.5rem",       # Consistente con el resto del dashboard
                            "margin-top": "10px", 
                            "line-height": "1.25",
                            "letter-spacing": "-1px"
                        }
                    ),
                    html.P(
                        "Arquitectura del modelado, ingeniería de características y flujo de procesamiento de datos espacio-temporales.",
                        className="lead mb-4 mt-3", 
                        style={
                            "font-size": "1.3rem",
                            "line-height": "1.6", 
                            "color": "#1e293b", 
                            "font-weight": "500"
                        }
                    ),
                ], className="pb-4", style={"border-bottom": "3px solid #000000"}) # Línea gruesa institucional
            ], width=12)
        ], className="mb-5"),

        # ─── CONTENEDOR DE LA IMAGEN A FULL ANCHO (CORREGIDA) ───
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Img(
                        # RUTA CORREGIDA: Apunta a la carpeta assets servida por Dash
                        src="/assets/PF_DG_MET.png",  
                        className="img-fluid rounded shadow-sm",
                        style={
                            "width": "100%",          # Toma todo el ancho disponible de la fila
                            "max-height": "700px",    # Techo de altura para que no se deforme en pantallas gigantes
                            "object-fit": "contain",  # Cambiado a 'contain' para que el diagrama metodológico no se recorte
                            "background-color": "#ffffff"
                        }
                    )
                ], className="d-flex justify-content-center bg-white p-3 rounded border")
            ], width=12)
        ], className="mb-4")

    ], fluid=True, className="p-4 p-lg-5 tab-problem-container")