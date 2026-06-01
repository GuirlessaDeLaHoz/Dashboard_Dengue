"""
tabs/introduccion.py
Pestaña: Introducción y enfoque del proyecto de investigación.
"""

import dash_bootstrap_components as dbc
from dash import html


def layout():
    return dbc.Container([

        # ─── ENCABEZADO INSTITUCIONAL DE ALTO IMPACTO (TÍTULO MAXIMIZADO) ───
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Span(
                        "PROYECTO DE INVESTIGACIÓN",
                        className="sup-title fw-bold d-block mb-2", 
                        style={"color": "#475569", "font-size": "1.2rem", "letter-spacing": "1.5px", "font-weight": "800"}
                    ),
                    html.H1(
                        "Predicción Espacio-Temporal de la Incidencia de Dengue en los Departamentos de Colombia Mediante Técnicas de Deep Learning", 
                        className="section-title-main fw-bold", 
                        style={
                            "font-weight": "900", 
                            "color": "#000000", 
                            "font-size": "3.5rem",
                            "margin-top": "10px", 
                            "line-height": "1.25",
                            "letter-spacing": "-1px"
                        }
                    ),
                    html.H5([
                        html.Strong("Autoría: ", style={"font-weight": "800", "color": "#475569"}),
                        html.Span("Guirlessa De La Hoz Guerrero, Mariangel Mercado Utria", style={"color": "#000000", "font-weight": "700"})
                    ], className="mt-4 mb-0", style={"font-size": "1.35rem"}),
                ], className="pb-4 border-bottom-academic", style={"border-bottom": "3px solid #000000"})
            ], width=12)
        ], className="mb-5"),

        # ─── SECCIÓN ENFOQUE E IMAGEN EN EQUILIBRIO MAXIMIZADO (LADO A LADO) ───
        dbc.Row([
            # Columna Izquierda: El Texto del Enfoque (Ancho equilibrado al 50%)
            dbc.Col([
                html.H4("Enfoque del Proyecto", className="mb-4 fw-bold", style={"font-weight": "900", "color": "#000000", "font-size": "2rem"}),
                
                html.P(
                    "Este proyecto combina el análisis espacio-temporal de la incidencia del dengue en Colombia "
                    "con la aplicación de modelos de deep learning para su predicción departamental, integrando "
                    "variables climáticas y epidemiológicas orientadas a identificar patrones de propagación y "
                    "fortalecer la salud pública.",
                    className="lead mb-4", 
                    style={
                        "font-size": "1.4rem",
                        "line-height": "1.6", 
                        "color": "#000000", 
                        "font-weight": "600"
                    }
                ),
                
                html.P(
                    "Adopta un enfoque metodológico y predictivo, orientado a transformar el análisis tradicional "
                    "de la salud pública mediante el uso de analítica avanzada. En lugar de limitarse a un diagnóstico descriptivo "
                    "de la situación del dengue, el proyecto se centra en estudiar el comportamiento histórico del virus en el territorio "
                    "para, posteriormente, aplicar arquitecturas de deep learning capaces de anticipar su comportamiento. Este enfoque permite "
                    "capturar las relaciones no lineales y los rezagos temporales entre las variaciones del clima y la velocidad de contagio, "
                    "convirtiendo los datos en una herramienta científica activa para predecir brotes y optimizar las interventions en salud pública.",
                    className="text-justify", 
                    style={
                        "font-size": "1.15rem",
                        "color": "#1e293b", 
                        "line-height": "1.7"
                    }
                )
            ], md=6, className="pe-md-5 d-flex flex-column justify-content-center"),
            
            # Columna Derecha: La Imagen con Mayor Presencia Lateral (50% del espacio)
            dbc.Col([
                html.Div([
                    html.Img(
                        src="/assets/IMG_INTRO.jpeg",
                        className="img-fluid rounded shadow-sm",
                        style={
                            "width": "100%",
                            "max-height": "550px",    # Techo de altura ampliado para que gane volumen vertical
                            "height": "100%",         # Obliga a estirarse dinámicamente con el texto
                            "object-fit": "cover",    # Mantiene el encuadre perfecto
                            "border": "1px solid #cbd5e1"
                        }
                    )
                ], className="d-flex justify-content-center align-items-center h-100 bg-white p-2 rounded border")
            ], md=6, className="mt-4 mt-md-0"),
            
        ], className="mb-5 pt-2 align-items-stretch") # align-items-stretch iguala la altura de ambas columnas automáticamente

    ], fluid=True, className="p-4 p-lg-5 tab-problem-container")


# ─── COMPONENTES AUXILIARES (HELPERS - PRESERVADOS) ───

def _tech_card(icon_class, title, description):
    return dbc.Card([
        dbc.CardBody([
            html.Div([
                html.I(className=f"{icon_class} tech-icon"),
            ], className="tech-icon-wrapper mb-3"),
            html.H5(title, className="tech-card-title"),
            html.P(description, className="tech-card-desc text-muted")
        ])
    ], className="h-100 tech-card border-0 shadow-sm")