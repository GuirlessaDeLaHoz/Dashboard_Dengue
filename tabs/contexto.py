import dash_bootstrap_components as dbc
from dash import html

def layout():
    return dbc.Container([

        # ==================================================
        # ENCABEZADO (Estilo Académico de Alto Impacto)
        # ==================================================
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Span(
                        "PREDICCIÓN ESPACIO-TEMPORAL DE LA INCIDENCIA DE DENGUE",
                        className="sup-title fw-bold d-block mb-2", 
                        style={"color": "#475569", "font-size": "1.1rem", "letter-spacing": "1.5px", "font-weight": "800"}
                    ),
                    html.H1("Base de Datos Multimodal", className="section-title-main fw-bold", 
                            style={
                                "font-weight": "900", 
                                "color": "#000000", 
                                "font-size": "3.5rem",       # Mismo tamaño imponente de la introducción
                                "margin-top": "10px", 
                                "line-height": "1.25",
                                "letter-spacing": "-1px"
                            }),
                    html.P(
                        "La base de datos se consolidó mediante la integración estratégica de tres fuentes de información independientes. Este enfoque multimodal permite unificar registros epidemiológicos, climáticos y geográficos, transformando datos aislados en un ecosistema robusto de alta dimensionalidad espacial y temporal indispensable para garantizar la precisión de los modelos predictivos.",
                        className="lead mb-4 mt-3", 
                        style={
                            "font-size": "1.3rem",        # Texto destacado, limpio y legible
                            "line-height": "1.6", 
                            "color": "#1e293b", 
                            "font-weight": "500"
                        }
                    ),
                ], className="pb-4", style={"border-bottom": "3px solid #000000"}) # Línea gruesa institucional
            ], width=12)
        ], className="mb-5"),

        # ==================================================
        # KPIs (Métricas del Dataset)
        # ==================================================
        dbc.Row([
            dbc.Col(_kpi_card("Rango Temporal", "2012 - 2024", "Años estudiados en la investigación", "fas fa-calendar-alt"), md=3),
            dbc.Col(_kpi_card("Registros Totales", "21.664", "Semanas × departamentos × años", "fas fa-database"), md=3),
            dbc.Col(_kpi_card("Variables Predictoras", "26", "Indicadores climáticos y demográficos", "fas fa-columns"), md=3),
            dbc.Col(_kpi_card("Casos Analizados", "+700K", "Casos históricos de dengue", "fas fa-chart-line"), md=3),
        ], className="g-4 mb-5"),

        # ==================================================
        # FUENTES DE DATOS (Tarjetas Adaptadas al Estilo Introducción)
        # ==================================================
        html.H4("Fuentes de Datos", className="mb-4 fw-bold", 
                style={"font-weight": "900", "color": "#000000", "font-size": "2rem"}), # Título de sección más grande

        dbc.Row([
            # SIVIGILA
            dbc.Col([
                _source_card(
                    title="Variables Epidemiológicas",
                    institution="SIVIGILA",
                    description="Casos reportados de pacientes con sospecha de dengue a nivel nacional.",
                    bullets=[
                        "Caracterización de población con dengue.",
                        "Cantidad de casos por semana epidemiológica.",
                        "Incidencia por cada 100.000 habitantes."
                    ],
                    badge_text="Variable Objetivo (Y)",
                    badge_color="danger"
                )
            ], md=4, className="d-flex"),

            # CLIMA
            dbc.Col([
                _source_card(
                    title="Variables Climáticas",
                    institution="Google Earth Engine (CHIRPS)",
                    description="Variables ambientales asociadas al ciclo biológico del mosquito Aedes aegypti.",
                    bullets=[
                        "Temperatura media, precipitación y humedad relativa.",
                        "Extracción de medias zonales por departamento.",
                        "Rezagos temporales entre t-1 y t-20 semanas."
                    ],
                    badge_text="Predictores Dinámicos (X)",
                    badge_color="primary"
                )
            ], md=4, className="d-flex"),

            # DANE
            dbc.Col([
                _source_card(
                    title="Variables Demográficas",
                    institution="DANE",
                    description="Indicadores demográficos y censales del territorio colombiano.",
                    bullets=[
                        "Proyecciones de población anual y densidad de habitantes por departamento.",
                        "Proporción de población en zonas urbanas frente a zonas rurales.",
                        "Sustento matemático para el cálculo de la Tasa de Incidencia por cada 100.000 habitantes."
                    ],
                    badge_text="Predictores Contextuales (X)",
                    badge_color="warning"
                )
            ], md=4, className="d-flex"),
        ], className="g-4 mb-5 justify-content-center align-items-stretch"),

    ], fluid=True, className="p-4 p-lg-5 tab-problem-container")


# ======================================================
# COMPONENTES AUXILIARES (HELPERS OPTIMIZADOS)
# ======================================================

def _kpi_card(title, value, subtext, icon_class):
    return dbc.Card([
        dbc.CardBody([
            html.Div(html.I(className=f"{icon_class} text-dark", style={"font-size": "1.8rem"}), className="mb-2 text-center w-100"),
            html.H6(title, className="text-dark small text-uppercase mb-1 text-center w-100", 
                    style={"letter-spacing": "0.5px", "font-weight": "800", "color": "#000000"}),
            html.H2(value, className="mb-2 text-center w-100 text-dark", 
                    style={"font-weight": "900", "font-size": "2.2rem", "color": "#000000"}),
            html.Hr(className="my-2 w-75 mx-auto", style={"color": "#cbd5e1", "border-top": "2px solid"}),
            html.Small(subtext, className="text-center d-block w-100", 
                       style={"font-size": "0.85rem", "line-height": "1.3", "color": "#1e293b", "font-weight": "600"})
        ], className="d-flex flex-column align-items-center justify-content-center p-4 text-center h-100 w-100")
    ], className="w-100 h-100 border-0 shadow-sm", style={"border-radius": "12px", "background-color": "white"})


def _source_card(title, institution, description, bullets, badge_text, badge_color):
    return dbc.Card([
        dbc.CardBody([
            # Contenedor superior con el Badge
            html.Div([
                dbc.Badge(badge_text, color=badge_color, className="px-3 py-1.5", style={"font-weight": "700", "font-size": "0.85rem"})
            ], className="mb-3 w-100 text-start"),
            
            # Bloque de Título y Fuente (Estilo Introducción: Negro Absoluto y Pesado)
            html.Div([
                html.H5(title, className="mb-1", 
                        style={"color": "#000000", "font-weight": "900", "font-size": "1.4rem", "letter-spacing": "-0.3px"}),
                html.Small(f"Fuente: {institution}", className="d-block mt-1", 
                           style={"color": "#000000", "font-weight": "800", "font-size": "0.95rem", "text-transform": "uppercase", "letter-spacing": "0.5px"})
            ], className="mb-3 w-100"),
            
            html.Hr(className="my-2", style={"color": "#cbd5e1", "border-top": "2px solid"}),
            
            # Descripción en negro legible
            html.P(
                description, 
                className="card-text text-justify mt-3 mb-3",
                style={"font-size": "1.05rem", "color": "#334155", "line-height": "1.5"}
            ),
            
            # Lista de Viñetas
            html.Ul([
                html.Li(bullet, className="mb-2 text-justify", style={"font-size": "1rem", "color": "#334155", "line-height": "1.4"}) for bullet in bullets
            ], className="ps-3 mb-0 text-start")
            
        ], className="p-4 d-flex flex-column justify-content-start")
    ], className="w-100 h-100 border-0 shadow-sm", style={"border-radius": "12px", "background-color": "white", "border-top": "4px solid #000000"})