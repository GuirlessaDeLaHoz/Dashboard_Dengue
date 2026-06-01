"""
tabs/objetivos.py
Pestaña: Objetivos de investigación y justificación del proyecto.
"""

import dash_bootstrap_components as dbc
from dash import html

# Paleta cromática coordinada y académica
AZUL_OSCURO = "#0d2d6b"
AZUL_MEDIO  = "#1a73e8"
AZUL_CLARO  = "#4da6ff"
GRIS_TEXTO  = "#1e293b"


def layout():
    return dbc.Container([
        _header("Objetivos del Proyecto",
                "Metas investigativas y fundamentación de la plataforma predictiva para el control epidemiológico."),

        # ─── OBJETIVO GENERAL ───
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Div([
                            html.Span("OBJETIVO GENERAL", className="text-muted small d-block mb-2 fw-bold", style={"letter-spacing": "1px", "font-weight": "700"}),
                            html.H3(
                                "Predecir la incidencia del dengue en los departamentos de Colombia mediante modelos "
                                "espacio-temporales capaces de capturar dependencias geográficas y temporales de la enfermedad.",
                                className="fw-bold m-0 text-justify", 
                                style={"font-weight": "850", "color": "#000000", "font-size": "1.7rem", "line-height": "1.5"}
                            ),
                        ], className="p-2")
                    ], className="p-4 p-lg-5")
                ], className="border-0 shadow-sm", style={"border-radius": "12px", "background-color": "#ffffff", "border-left": f"6px solid {AZUL_OSCURO}"})
            ], width=12)
        ], className="mb-5"),

        # ─── OBJETIVOS ESPECÍFICOS (TRÍO SIMÉTRICO COLGADO EN FILA) ───
        dbc.Row([
            dbc.Col([
                html.H4("Objetivos Específicos", className="mb-4 fw-bold", style={"font-weight": "850", "color": "#000000", "font-size": "1.6rem"}),
                
                dbc.Row([
                    dbc.Col(_obj_especifico("OE1", AZUL_OSCURO,
                        "Caracterización del comportamiento basal",
                        "Caracterizar el comportamiento espacio-temporal de la incidencia del dengue en los "
                        "departamentos de Colombia, estableciendo las dinámicas iniciales de transmisión."), md=4, className="d-flex"),
                    
                    dbc.Col(_obj_especifico("OE2", AZUL_MEDIO,
                        "Análisis de anomalías y persistencia",
                        "Evaluar los patrones espacio-temporales de la incidencia del dengue mediante el análisis "
                        "focalizado de años epidemiológicos atípicos y de departamentos con persistencia histórica "
                        "de alta incidencia en Colombia."), md=4, className="d-flex"),
                    
                    dbc.Col(_obj_especifico("OE3", AZUL_CLARO,
                        "Modelado avanzado con Deep Learning",
                        "Implementar y evaluar modelos espacio-temporales de Deep Learning para la predicción "
                        "de la incidencia del dengue, validando su capacidad de generalización estadística."), md=4, className="d-flex"),
                ], className="mb-4 g-4"),
            ], width=12)
        ], className="mb-5 pt-2"),

        # ─── JUSTIFICACIÓN ENFOCADA EN LA PROBLEMÁTICA NACIONAL ───
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Justificación Institucional y Científica", className="mb-5 fw-bold", style={"font-weight": "850", "color": "#000000", "font-size": "1.6rem"}),
                        
                        dbc.Row([
                            # COLUMNA IZQUIERDA: EL PROBLEMA EN COLOMBIA
                            dbc.Col([
                                _justificacion_item(
                                    "Magnitud de la Carga Epidemiológica",
                                    "El dengue es una de las enfermedades transmitidas por vectores más críticas en Colombia, "
                                    "comprobando al país (según la OPS, 2024) con una de las mayores incidencias en América Latina. "
                                    "Los ciclos epidémicos recurrentes (cada 3 a 5 años) saturan las redes hospitalarias, "
                                    "exigiendo una transición urgente de la respuesta reactiva tradicional hacia una vigilancia "
                                    "epidemiológica predictiva y anticipatoria."
                                ),
                                
                                _justificacion_item(
                                    "Heterogeneidad Territorial y Movilidad",
                                    "La transmisión del virus afecta de manera profundamente desigual a los departamentos debido a "
                                    "determinantes como la diversidad climática, la densidad de población y las condiciones socioeconómicas. "
                                    "Además, la fuerte movilidad humana interdepartamental actúa como un motor de propagación biológica, "
                                    "lo que hace inviable seguir analizando el riesgo de forma aislada sin evaluar cómo interactúan las regiones."
                                ),
                            ], md=6, className="pe-md-4"),
                            
                            # COLUMNA DERECHA: LA NECESIDAD METODOLÓGICA (LOS MODELOS)
                            dbc.Col([
                                _justificacion_item(
                                    "Insuficiencia de Enfoques Clásicos",
                                    "La literatura científica demuestra que los modelos estadísticos tradicionales (como ARIMA/SARIMA) "
                                    "son insuficientes para la toma de decisiones actuales, ya que fallan al capturar el comportamiento "
                                    "no lineal de las variables ambientales y omiten por completo las conexiones espaciales interregionales, "
                                    "dejando un vacío crítico en la planeación de la salud pública."
                                ),
                                
                                _justificacion_item(
                                    "Pertinencia de Modelos de Última Generación",
                                    "Para capturar esta complejidad, el proyecto evalúa tres enfoques distintos: LSTM como la referencia "
                                    "obligada en dependencias temporales largas (Nguyen et al., 2022); DCRNN para incorporar la difusión "
                                    "espacial guiada por conectividad territorial (Li et al., 2018); y STGNN para modelar explícitamente "
                                    "a los departamentos como nodos de grafos interconectados (Siabi et al., 2026). Validar estos benchmarks "
                                    "en el escenario local generará la evidencia científica necesaria para optimizar recursos e intervenciones."
                                ),
                            ], md=6, className="ps-md-4"),
                        ]),
                    ], className="p-4 p-lg-5")
                ], className="border-0 shadow-sm", style={"border-radius": "12px", "background-color": "#ffffff"})
            ], width=12)
        ], className="mb-5 pt-2"),

        # ─── ALCANCE CIENTÍFICO Y EXCLUSIONES (BIEN DESPEGADO) ───
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Alcance del Proyecto", className="mb-4 fw-bold", style={"font-weight": "850", "color": "#000000", "font-size": "1.6rem"}),
                        
                        dbc.Row([
                            # Dentro del Alcance
                            dbc.Col([
                                html.Div("Componentes Incluidos", className="fw-bold mb-3 small", style={"color": "#16a34a", "letter-spacing": "0.5px"}),
                                html.Ul([
                                    html.Li("Modelado espacio-temporal a resolución departamental (32 entidades territoriales de Colombia)."),
                                    html.Li("Análisis histórico focalizado en brotes anómalos y zonas de persistencia endémica alta."),
                                    html.Li("Implementación de arquitecturas de Deep Learning diseñadas para series de tiempo multidimensionales."),
                                    html.Li("Evaluación y comparación de métricas de rendimiento predictivo sobre horizontes temporales."),
                                    html.Li("Despliegue de un entorno interactivo en Dash para contrastar las tendencias reales frente a las estimadas."),
                                ], style={"font-size": "1.05rem", "color": GRIS_TEXTO, "line-height": "1.8", "padding-left": "20px"}),
                            ], md=6, className="pe-md-4"),
                            
                            # Fuera de Alcance
                            dbc.Col([
                                html.Div("Exclusiones del Proyecto", className="fw-bold mb-3 small", style={"color": "#dc2626", "letter-spacing": "0.5px"}),
                                html.Ul([
                                    html.Li("Predicción desagregada a nivel micro-geográfico (municipal, comunal o veredal)."),
                                    html.Li("Integración automatizada o sincronización por API en tiempo real con las bases primarias del SIVIGILA."),
                                    html.Li("Evaluación diagnóstica, clínica o seguimiento individualizado de historias de pacientes."),
                                    html.Li("Modelado molecular o segregación epidemiológica por serotipos específicos del virus (DENV-1 a DENV-4)."),
                                    html.Li("Desarrollo o ejecución automatizada de planes físicos de intervención o control de vectores."),
                                ], style={"font-size": "1.05rem", "color": GRIS_TEXTO, "line-height": "1.8", "padding-left": "20px"}),
                            ], md=6, className="ps-md-4"),
                        ]),
                    ], className="p-4 p-lg-5")
                ], className="border-0 shadow-sm", style={"border-radius": "12px", "background-color": "#ffffff"})
            ], width=12)
        ], className="mt-5 pt-2 mb-4")

    ], fluid=True, className="p-4 p-lg-5 tab-problem-container")


# ─── AUXILIARES DE RENDERIZADO (HELPERS) ───

def _header(titulo, subtitulo):
    return dbc.Row([
        dbc.Col([
            html.Div([
                html.H1(titulo, className="section-title-main fw-bold", style={"font-weight": "900", "color": "#000000", "font-size": "2.8rem"}),
                html.P(subtitulo, className="text-subtitle-problem text-muted", style={"font-size": "1.1rem"}),
            ], className="pb-3 border-bottom-academic")
        ], width=12)
    ], className="mb-5")


def _obj_especifico(num, color, titulo, descripcion):
    return dbc.Card([
        dbc.CardBody([
            html.Div([
                html.Span(num, className="badge me-2 px-3 py-2", style={"background-color": color, "font-size": "0.9rem", "font-weight": "800", "border-radius": "6px"}),
                html.H5(titulo, className="m-0 fw-bold", style={"font-weight": "800", "color": "#000000", "font-size": "1.2rem"})
            ], className="d-flex align-items-center mb-3"),
            html.P(descripcion, className="m-0 text-justify", style={"font-size": "1.05rem", "color": GRIS_TEXTO, "line-height": "1.6"})
        ], className="p-4")
    ], className="border-0 shadow-sm w-100", style={"border-radius": "12px", "background-color": "#ffffff", "border-top": f"4px solid {color}"})


def _justificacion_item(titulo, descripcion):
    return html.Div([
        html.H6(titulo, className="fw-bold mb-2", style={"font-weight": "800", "color": "#000000", "font-size": "1.15rem"}),
        html.P(descripcion, className="text-justify mb-4", style={"font-size": "1.05rem", "color": GRIS_TEXTO, "line-height": "1.6"}),
    ], className="mb-3")