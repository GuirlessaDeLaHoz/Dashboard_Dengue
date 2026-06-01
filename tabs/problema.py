import dash_bootstrap_components as dbc
from dash import dcc, html


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
                        "Planteamiento del Problema", 
                        className="section-title-main fw-bold", 
                        style={
                            "font-weight": "900", 
                            "color": "#000000", 
                            "font-size": "3.5rem",       # Consistente con Introducción y Base de Datos
                            "margin-top": "10px", 
                            "line-height": "1.25",
                            "letter-spacing": "-1px"
                        }
                    ),
                    html.P(
                        "Fundamentación cuantitativa de la carga epidemiológica de las arbovirosis y la necesidad imperativa de un enfoque predictivo de analítica avanzada.",
                        className="lead mb-4 mt-3", 
                        style={
                            "font-size": "1.3rem",        # Párrafo destacado limpio y visible
                            "line-height": "1.6", 
                            "color": "#1e293b", 
                            "font-weight": "500"
                        }
                    ),
                ], className="pb-4", style={"border-bottom": "3px solid #000000"}) # Línea gruesa institucional académica
            ], width=12)
        ], className="mb-5"),

        # ─── BLOQUE 1: LA CARGA GLOBAL Y REGIONAL (TARJETAS ADAPTADAS) ───
        dbc.Row([
            # Tarjeta 1: Carga Mundial
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Div([
                            html.I(className="fas fa-globe-americas me-2 text-dark", style={"font-size": "1.6rem"}),
                            html.H5("Amenaza Global Desatendida", className="m-0 fw-bold", 
                                    style={"font-weight": "900", "color": "#000000", "font-size": "1.35rem"})
                        ], className="d-flex align-items-center mb-3"),
                        
                        html.Hr(className="my-2", style={"color": "#cbd5e1", "border-top": "2px solid"}),
                        
                        html.P([
                            "Las enfermedades transmitidas por vectores representan más del ",
                            html.B("17% de las enfermedades infecciosas", style={"font-weight": "800"}), " y provocan más de ",
                            html.B("700.000 defunciones al año", style={"font-weight": "800"}), "."
                        ], className="text-justify mt-3 mb-3", style={"font-size": "1.05rem", "color": "#334155", "line-height": "1.5"}),
                        
                        html.Div([
                            html.Span("Aproximadamente la mitad de la población mundial se encuentra en riesgo de contraer dengue, con estimaciones de 100 a 400 millones de infecciones anuales."),
                        ], className="p-3 rounded mb-3", style={"background-color": "#f8fafc", "font-size": "0.95rem", "color": "#1e293b", "border-left": "4px solid #475569", "font-weight": "500"}),
                        
                        html.Small("Fuente: OMS (2024)", className="d-block text-end", style={"font-weight": "800", "color": "#000000", "text-transform": "uppercase", "letter-spacing": "0.5px"})
                    ], className="p-4 d-flex flex-column justify-content-between h-100")
                ], className="border-0 shadow-sm h-100", style={"border-radius": "12px", "background-color": "white", "border-top": "4px solid #000000"})
            ], md=6, lg=4, className="d-flex"),

            # Tarjeta 2: Alerta Regional
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Div([
                            html.I(className="fas fa-triangle-exclamation me-2 text-dark", style={"font-size": "1.6rem"}),
                            html.H5("Crisis Sanitaria en las Américas", className="m-0 fw-bold", 
                                    style={"font-weight": "900", "color": "#000000", "font-size": "1.35rem"})
                        ], className="d-flex align-items-center mb-3"),
                        
                        html.Hr(className="my-2", style={"color": "#cbd5e1", "border-top": "2px solid"}),
                        
                        html.P([
                            "Durante 2024, la región ha mostrado un incremento sostenido de la actividad epidémica, registrando más de ",
                            html.B("12 millones de casos sospechosos", style={"font-weight": "800"}), " de dengue."
                        ], className="text-justify mt-3 mb-3", style={"font-size": "1.05rem", "color": "#334155", "line-height": "1.5"}),
                        
                        html.Div([
                            html.Span("Existe una expansión simultánea con circulación activa de los cuatro serotipos (DENV-1, DENV-2, DENV-3 y DENV-4), elevando críticamente el riesgo de manifestaciones graves."),
                        ], className="p-3 rounded mb-3", style={"background-color": "#f8fafc", "font-size": "0.95rem", "color": "#1e293b", "border-left": "4px solid #475569", "font-weight": "500"}),
                        
                        html.Small("Fuente: PAHO (2026)", className="d-block text-end", style={"font-weight": "800", "color": "#000000", "text-transform": "uppercase", "letter-spacing": "0.5px"})
                    ], className="p-4 d-flex flex-column justify-content-between h-100")
                ], className="border-0 shadow-sm h-100", style={"border-radius": "12px", "background-color": "white", "border-top": "4px solid #000000"})
            ], md=6, lg=4, className="d-flex"),

            # Tarjeta 3: Realidad Nacional
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Div([
                            html.I(className="fas fa-chart-line me-2 text-dark", style={"font-size": "1.6rem"}),
                            html.H5("El Escenario de Colombia", className="m-0 fw-bold", 
                                    style={"font-weight": "900", "color": "#000000", "font-size": "1.35rem"})
                        ], className="d-flex align-items-center mb-3"),
                        
                        html.Hr(className="my-2", style={"color": "#cbd5e1", "border-top": "2px solid"}),
                        
                        html.P([
                            "El país constituye un escenario crítico. La incidencia nacional pasó de 86,5 casos en 2022 a un alarmante estatus de ",
                            html.B("148,4 casos por cada 100.000 habitantes en 2023", style={"font-weight": "800"}), "."
                        ], className="text-justify mt-3 mb-3", style={"font-size": "1.05rem", "color": "#334155", "line-height": "1.5"}),
                        
                        html.Div([
                            html.Span("Variables como la temperatura, precipitación y humedad relativa actúan como determinantes clave que favorecen la persistencia y distribución del vector."),
                        ], className="p-3 rounded mb-3", style={"background-color": "#f8fafc", "font-size": "0.95rem", "color": "#1e293b", "border-left": "4px solid #475569", "font-weight": "500"}),
                        
                        html.Small("Fuente: INS (2023) / Mordecai et al. (2020)", className="d-block text-end", style={"font-weight": "800", "color": "#000000", "text-transform": "uppercase", "letter-spacing": "0.5px"})
                    ], className="p-4 d-flex flex-column justify-content-between h-100")
                ], className="border-0 shadow-sm h-100", style={"border-radius": "12px", "background-color": "white", "border-top": "4px solid #000000"})
            ], md=12, lg=4, className="d-flex"),
        ], className="g-4 mb-5"),

        # ─── BLOQUE 2: INTERACTIVIDAD (FACTORES DETERMINANTES) ───
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H4("Factores Determinantes del Modelado", className="mb-4 fw-bold", 
                            style={"font-weight": "900", "color": "#000000", "font-size": "2rem"}),
                    
                    html.Div([
                        # Botón 1: Clima
                        html.Button([
                            html.Div([
                                html.I(className="fas fa-cloud-sun text-dark mt-1", style={"font-size": "1.6rem", "width": "35px"}),
                                html.Div([
                                    html.H6("Gobernanza Climática y Ambiental", className="m-0 fw-bold", 
                                            style={"font-weight": "900", "color": "#000000", "font-size": "1.15rem"}),
                                    html.P("Influencia de las variables físicas en los ciclos de transmisión.", className="text-muted m-0 mt-1", style={"font-size": "0.9rem"})
                                ], className="ms-2 text-start")
                            ], className="d-flex align-items-start")
                        ], id="btn-factor-clima", n_clicks=0, className="flex-fill p-4 border rounded design-interactive-card-btn", 
                           style={"background-color": "#ffffff", "flex-basis": "0", "border-width": "2px", "border-color": "#cbd5e1"}),

                        # Botón 2: Espacio-Temporal
                        html.Button([
                            html.Div([
                                html.I(className="fas fa-map-location-dot text-dark mt-1", style={"font-size": "1.6rem", "width": "35px"}),
                                html.Div([
                                    html.H6("Variabilidad Espacio-Temporal", className="m-0 fw-bold", 
                                            style={"font-weight": "900", "color": "#000000", "font-size": "1.15rem"}),
                                    html.P("Comportamiento geográfico dinámico documentado en el país.", className="text-muted m-0 mt-1", style={"font-size": "0.9rem"})
                                ], className="ms-2 text-start")
                            ], className="d-flex align-items-start")
                        ], id="btn-factor-espacio", n_clicks=0, className="flex-fill p-4 border rounded design-interactive-card-btn", 
                           style={"background-color": "#ffffff", "flex-basis": "0", "border-width": "2px", "border-color": "#cbd5e1"}),

                        # Botón 3: Brecha
                        html.Button([
                            html.Div([
                                html.I(className="fas fa-code-merge text-dark mt-1", style={"font-size": "1.6rem", "width": "35px"}),
                                html.Div([
                                    html.H6("La Brecha Metodológica Actual", className="m-0 fw-bold", 
                                            style={"font-weight": "900", "color": "#000000", "font-size": "1.15rem"}),
                                    html.P("Límite de los análisis de clústeres y modelos clásicos.", className="text-muted m-0 mt-1", style={"font-size": "0.9rem"})
                                ], className="ms-2 text-start")
                            ], className="d-flex align-items-start")
                        ], id="btn-factor-brecha", n_clicks=0, className="flex-fill p-4 border rounded design-interactive-card-btn", 
                           style={"background-color": "#ffffff", "flex-basis": "0", "border-width": "2px", "border-color": "#cbd5e1"}),
                        
                    ], className="d-flex flex-column flex-md-row gap-4 w-100")
                ])
            ], width=12)
        ], className="mb-5"),

        # ─── FILA 3: PROPUESTA DE VALOR EN LÍNEA CON INTRODUCCIÓN ───
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H4("Propuesta de Valor del Proyecto", className="mb-4 fw-bold", 
                            style={"font-weight": "900", "color": "#000000", "font-size": "2rem", "letter-spacing": "-0.5px"}),
                    
                    html.P([
                        "Ante este panorama, el proyecto propone una ", 
                        html.B("contribución técnica", style={"font-weight": "800"}), 
                        " directa a la salud pública mediante el desarrollo de un modelo predictivo basado en ", 
                        html.B("Deep Learning", style={"font-weight": "800"}), "."
                    ], className="lead text-dark mb-4", style={"font-size": "1.3rem", "color": "#000000", "font-weight": "600"}),

                    html.Hr(className="my-4", style={"color": "#cbd5e1", "border-top": "2px solid"}),

                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H5("Innovación del Enfoque", className="fw-bold mb-2", 
                                        style={"font-weight": "900", "color": "#000000", "font-size": "1.3rem"}),
                                html.P("Supera la limitación de los modelos tradicionales al capturar simultáneamente la dependencia temporal de las series de tiempo y la variabilidad espacial entre departamentos.", 
                                       className="text-justify", style={"font-size": "1.05rem", "color": "#334155", "line-height": "1.5"})
                            ], className="pe-md-4")
                        ], md=6),
                        
                        dbc.Col([
                            html.Div([
                                html.H5("Impacto en Decisiones", className="fw-bold mb-2", 
                                        style={"font-weight": "900", "color": "#000000", "font-size": "1.3rem"}),
                                html.P("Optimiza la asignación de recursos institucionales y fortalece de manera oportuna la capacidad de respuesta y prevención antes de la maduración del brote.", 
                                       className="text-justify", style={"font-size": "1.05rem", "color": "#334155", "line-height": "1.5"})
                            ])
                        ], md=6)
                    ])
                ], className="p-5 rounded bg-white shadow-sm", style={"border-top": "5px solid #000000"})
            ], width=12)
        ], className="mt-5 pt-2 mb-4")

    ], fluid=True, className="p-4 p-lg-5 tab-problem-container")