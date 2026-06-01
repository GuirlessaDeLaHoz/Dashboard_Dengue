from dash import html, dcc, Input, Output, callback # type: ignore[import]
try:
    import dash_bootstrap_components as dbc  # type: ignore[import]
except ImportError:
    dbc = None
import pandas as pd # type: ignore[import]
import plotly.express as px  # type: ignore[import]
import plotly.graph_objects as go  # type: ignore[import]
import plotly.subplots  # type: ignore[import]
import geopandas as gpd # type: ignore[import]

# ======================================================
# PALETA GLOBAL (AZULES + GRISES)
# ======================================================
PALETA_CATEGORICA = [
    "#1F77B4",
    "#4C78A8",
    "#A0B1C5",
    "#6C757D",
    "#2C3E50"
]

PALETA_CONTINUA = [
    "#F7FBFF",
    "#DEEBF7",
    "#C6DBEF",
    "#9ECAE1",
    "#6BAED6",
    "#3182BD",
    "#08519C"
]

TEMPLATE = "plotly_white"

# ======================================================
# CARGA DE DATOS
# ======================================================

df = pd.read_csv("data/df_full.csv")

df["fecha_inicio"] = pd.to_datetime(df["fecha_inicio"])

# ======================================================
# LAYOUT
# ======================================================
def layout():

    return dbc.Container([

        html.Br(),

        html.H2(
            "Resultados del Proyecto",
            style={
                "color": "#0B3C5D",
                "fontWeight": "bold"
            }
        ),

        html.Hr(),

        html.H3(
            "Exploratory Data Analysis (EDA)",
            style={
                "color": "#0B3C5D",
                "fontWeight": "bold"
            }
        ),

        html.P(
            "Análisis exploratorio de la incidencia de dengue en Colombia (2012–2024).",
            style={"color": "#6C757D"}
        ),

        # ======================================================
        # FILTROS
        # ======================================================
        dbc.Row([

            dbc.Col([
                html.Label("Selecciona Año"),

                dcc.Dropdown(
                    id="eda-year-dropdown",
                    options=[
                        {"label": str(y), "value": y}
                        for y in sorted(df["ano"].unique())
                    ],
                    value=None,
                    placeholder="Todos los años",
                    clearable=True
                )
            ], width=3),

            dbc.Col([
                html.Label("Selecciona Departamento"),

                dcc.Dropdown(
                    id="eda-depto-dropdown",
                    options=[
                        {"label": d, "value": d}
                        for d in sorted(df["departamento"].unique())
                    ],
                    value=None,
                    placeholder="Todos los departamentos",
                    clearable=True
                )
            ], width=3)

        ], className="mb-4"),

        # ======================================================
        # SUBPESTAÑAS EDA
        # ======================================================
        dbc.Tabs([

            # ======================================================
            # TAB 1
            # ======================================================
            dbc.Tab(
                label="Caracterización de la Población",
                tab_id="caracterizacion",
                children=[

                    html.Br(),

                    dbc.Row([

                        dbc.Col(
                            dbc.Card([
                                dbc.CardBody([
                                    html.H6("Casos acumulados"),

                                    html.H2(
                                        id="eda-total-casos",
                                        style={
                                            "color": "#1F77B4",
                                            "fontWeight": "bold"
                                        }
                                    )
                                ])
                            ], className="shadow-sm border-0"),
                            width=4
                        ),

                        dbc.Col(
                            dbc.Card([
                                dbc.CardBody([
                                    html.H6("Incidencia acumulada (x100k)"),

                                    html.H2(
                                        id="eda-incidencia",
                                        style={
                                            "color": "#4C78A8",
                                            "fontWeight": "bold"
                                        }
                                    )
                                ])
                            ], className="shadow-sm border-0"),
                            width=4
                        )
                    ], className="mb-5"),

                    dbc.Row([
                        dbc.Col(dcc.Graph(id="eda-pie-sexo"), width=4),
                        dbc.Col(dcc.Graph(id="eda-bar-edad"), width=4),
                        dbc.Col(dcc.Graph(id="eda-pie-zona"), width=4)
                    ], className="mb-5")
                ]
            ),

            # ======================================================
            # TAB 2
            # ======================================================
            dbc.Tab(
                label="Distribución de la Incidencia",
                tab_id="incidencia",
                children=[

                    html.Br(),

                    dbc.Row([
                        dbc.Col(dcc.Graph(id="eda-hist-incidencia"), width=6),
                        dbc.Col(dcc.Graph(id="eda-box-incidencia"), width=6)
                    ], className="mb-5"),

                    dbc.Row([
                        dbc.Col(
                            dcc.Graph(id="eda-bar-incidencia-depto"),
                            width=12
                        )
                    ], className="mb-5")
                ]
            ),

            # ======================================================
            # TAB 3
            # ======================================================
            dbc.Tab(
                label="Análisis Espacio-Temporal",
                tab_id="espacio_temporal",
                children=[

                    html.Br(),

                    # ======================================================
                    # INDICADORES
                    # ======================================================
                    dbc.Row([

                        dbc.Col(
                            dbc.Card([
                                dbc.CardBody([
                                    html.H6(
                                        "Periodo analizado",
                                        style={"color": "#0B3C5D"}
                                    ),

                                    html.H4(
                                        "2012–2024",
                                        style={
                                            "fontWeight": "bold",
                                            "color": "#1E3A8A"
                                        }
                                    ),

                                    html.P(
                                        "13 años · ~676 semanas",
                                        style={"color": "#6C757D"}
                                    )
                                ])
                            ], className="shadow-sm border-0"),
                            width=3
                        ),

                        dbc.Col(
                            dbc.Card([
                                dbc.CardBody([
                                    html.H6(
                                        "Pico epidémico máximo",
                                        style={"color": "#0B3C5D"}
                                    ),

                                    html.H4(
                                        "2023–2024",
                                        style={
                                            "fontWeight": "bold",
                                            "color": "#1E3A8A"
                                        }
                                    ),

                                    html.P(
                                        "Más intenso de la serie",
                                        style={"color": "#6C757D"}
                                    )
                                ])
                            ], className="shadow-sm border-0"),
                            width=3
                        ),

                        dbc.Col(
                            dbc.Card([
                                dbc.CardBody([
                                    html.H6(
                                        "Ciclos epidémicos",
                                        style={"color": "#0B3C5D"}
                                    ),

                                    html.H4(
                                        "~4–5 años",
                                        style={
                                            "fontWeight": "bold",
                                            "color": "#1E3A8A"
                                        }
                                    ),

                                    html.P(
                                        "2013–14 · 2019–20 · 2023–24",
                                        style={"color": "#6C757D"}
                                    )
                                ])
                            ], className="shadow-sm border-0"),
                            width=3
                        ),

                        dbc.Col(
                            dbc.Card([
                                dbc.CardBody([
                                    html.H6(
                                        "Estacionariedad (ADF)",
                                        style={"color": "#0B3C5D"}
                                    ),

                                    html.H4(
                                        "No estacionaria",
                                        style={
                                            "fontWeight": "bold",
                                            "color": "#1E3A8A"
                                        }
                                    ),

                                    html.P(
                                        "p-value 0.080 · cercano al umbral",
                                        style={"color": "#6C757D"}
                                    )
                                ])
                            ], className="shadow-sm border-0"),
                            width=3
                        )

                    ], className="mb-4"),

                    # ======================================================
                    # SERIE TEMPORAL
                    # ======================================================
                    html.H5(
                        "Serie temporal de incidencia y covariables ambientales",
                        style={
                            "color": "#0B3C5D",
                            "fontWeight": "bold"
                        }
                    ),

                    dbc.Row([

                        dbc.Col([

                            html.Label("Selecciona Covariable"),

                            dcc.Dropdown(
                                id="eda-covariable-dropdown",
                                options=[
                                    {
                                        "label": "Ninguna",
                                        "value": None
                                    },
                                    {
                                        "label": "Precipitación (lag 4)",
                                        "value": "precip_lag_4"
                                    },
                                    {
                                        "label": "Temperatura Media",
                                        "value": "temp_c"
                                    },
                                    {
                                        "label": "Humedad Relativa",
                                        "value": "humedad_relativa"
                                    }
                                ],
                                value=None,
                                clearable=True
                            )

                        ], width=3),

                        dbc.Col(
                            dcc.Graph(id="eda-serie-incidencia-covariable"),
                            width=9
                        )

                    ], className="mb-5"),

                    # ======================================================
                    # BOXPLOT ANUAL
                    # ======================================================
                    html.H5(
                        "Distribución y variabilidad anual de la incidencia",
                        style={
                            "color": "#0B3C5D",
                            "fontWeight": "bold"
                        }
                    ),

                    dbc.Row([
                        dbc.Col(dcc.Graph(id="eda-box-anual"), width=12)
                    ], className="mb-5"),

                    # ======================================================
                    # HEATMAP
                    # ======================================================
                    html.H5(
                        "Heatmap de incidencia semanal por año",
                        style={
                            "color": "#0B3C5D",
                            "fontWeight": "bold"
                        }
                    ),

                    dbc.Row([
                        dbc.Col(dcc.Graph(id="eda-heatmap"), width=12)
                    ], className="mb-5"),

                    # ======================================================
                    # MAPA + RANKING
                    # ======================================================
                    html.H5(
                        "Distribución espacial y ranking nacional",
                        style={
                            "color": "#0B3C5D",
                            "fontWeight": "bold"
                        }
                    ),

                    dbc.Row([

                        dbc.Col(
                            dcc.Graph(id="eda-mapa-incidencia"),
                            width=6
                        ),

                        dbc.Col(
                            dcc.Graph(id="eda-ranking-incidencia"),
                            width=6
                        )

                    ], className="mb-5")

                ]
            )

        ], id="eda-subtabs", active_tab="caracterizacion")

    ], fluid=True)


# ======================================================
# CALLBACK PRINCIPAL
# ======================================================
@callback(
    Output("eda-total-casos", "children"),
    Output("eda-incidencia", "children"),
    Output("eda-pie-sexo", "figure"),
    Output("eda-pie-zona", "figure"),
    Output("eda-bar-edad", "figure"),
    Output("eda-hist-incidencia", "figure"),
    Output("eda-box-incidencia", "figure"),
    Output("eda-bar-incidencia-depto", "figure"),
    Output("eda-box-anual", "figure"),
    Output("eda-heatmap", "figure"),
    Output("eda-mapa-incidencia", "figure"),
    Output("eda-ranking-incidencia", "figure"),
    Input("eda-year-dropdown", "value"),
    Input("eda-depto-dropdown", "value")
)
def update_dashboard(year, departamento):

    df_filtered = df.copy()

    if year is not None:
        df_filtered = df_filtered[df_filtered["ano"] == year]

    df_filtered_depto = df_filtered.copy()

    if departamento is not None:
        df_filtered_depto = df_filtered_depto[
            df_filtered_depto["departamento"] == departamento
        ]

    df_depto = df.copy()

    if departamento is not None:
        df_depto = df_depto[
            df_depto["departamento"] == departamento
        ]

    label = (
        "2012–2024"
        if year is None and departamento is None
        else str(year)
        if year is not None and departamento is None
        else f"{departamento} (2012–2024)"
        if year is None
        else f"{departamento} ({year})"
    )

    # ======================================================
    # MÉTRICAS
    # ======================================================
    total_casos = df_filtered_depto["casos"].sum()

    incidencia_acumulada = (
        df_filtered_depto["incidencia"].mean()
    )

    # ======================================================
    # SEXO
    # ======================================================
    fig_sexo = px.pie(
        names=["Mujeres", "Hombres"],
        values=[
            df_filtered_depto["casos_mujeres"].sum(),
            df_filtered_depto["casos_hombres"].sum()
        ],
        title=f"Proporción Casos por Sexo ({label})",
        color_discrete_sequence=PALETA_CATEGORICA,
        template=TEMPLATE
    )

    # ======================================================
    # ZONA
    # ======================================================
    fig_zona = px.pie(
        names=["Rural", "Urbano"],
        values=[
            df_filtered_depto["casos_rural"].sum(),
            df_filtered_depto["casos_urbano"].sum()
        ],
        title=f"Proporción Casos por Zona ({label})",
        color_discrete_sequence=PALETA_CATEGORICA,
        template=TEMPLATE
    )

    # ======================================================
    # EDAD
    # ======================================================
    grupos = ["0-4", "5-13", "14-26", "27-59", "60+"]

    valores = [
        df_filtered_depto["n_0_4"].sum(),
        df_filtered_depto["n_5_13"].sum(),
        df_filtered_depto["n_14_26"].sum(),
        df_filtered_depto["n_27_59"].sum(),
        df_filtered_depto["n_60_mas"].sum()
    ]

    fig_edad = px.bar(
        x=grupos,
        y=valores,
        title=f"Casos por Edad ({label})",
        color=grupos,
        color_discrete_sequence=PALETA_CATEGORICA,
        template=TEMPLATE
    )

    # ======================================================
    # HISTOGRAMA
    # ======================================================
    fig_hist = px.histogram(
        df_filtered_depto,
        x="incidencia",
        nbins=40,
        title=f"Distribución de incidencia ({label})",
        color_discrete_sequence=["#1F77B4"],
        template=TEMPLATE
    )

    # ======================================================
    # BOXPLOT
    # ======================================================
    fig_box = px.box(
        df_filtered_depto,
        x="incidencia",
        title=f"Variabilidad de incidencia ({label})",
        color_discrete_sequence=["#4C78A8"],
        template=TEMPLATE
    )

    # ======================================================
    # INCIDENCIA POR DEPARTAMENTO
    # ======================================================
    espacial = (
        df_filtered.groupby("departamento")["incidencia"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig_bar_depto = px.bar(
        espacial,
        x="incidencia",
        y="departamento",
        orientation="h",
        title="Incidencia por Departamento",
        color="incidencia",
        color_continuous_scale=PALETA_CONTINUA,
        template=TEMPLATE
    )

    # ======================================================
    # BOXPLOT ANUAL
    # ======================================================
    fig_box_anual = px.box(
        df_depto,
        x="ano",
        y="incidencia",
        color="ano",
        title="Distribución anual de incidencia",
        color_discrete_sequence=PALETA_CATEGORICA,
        template=TEMPLATE
    )

    # ======================================================
    # HEATMAP
    # ======================================================
    heatmap_df = (
        df_depto
        .groupby(["ano", "semana"])["incidencia"]
        .mean()
        .reset_index()
    )

    matriz = heatmap_df.pivot(
        index="ano",
        columns="semana",
        values="incidencia"
    )

    fig_heatmap = px.imshow(
        matriz,
        color_continuous_scale=PALETA_CONTINUA,
        aspect="auto",
        title=f"Estacionalidad semanal ({label})"
    )

    # ======================================================
    # MAPA
    # ======================================================
    tabla_global = (
        df_filtered.groupby("departamento")["incidencia"]
        .mean()
        .reset_index()
    )

    mapa = gpd.read_file(
        "data/MGN_ADM_DPTO_POLITICO/MGN_ADM_DPTO_POLITICO_limpio.shp"
    )

    mapa = mapa.merge(
        tabla_global,
        left_on="dpto_cnmbr",
        right_on="departamento",
        how="left"
    )

    fig_mapa = px.choropleth(
        mapa,
        geojson=mapa.__geo_interface__,
        locations=mapa.index,
        color="incidencia",
        projection="mercator",
        color_continuous_scale=PALETA_CONTINUA,
        template=TEMPLATE
    )

    fig_mapa.update_geos(
        fitbounds="locations",
        visible=False
    )

    # ======================================================
    # RANKING
    # ======================================================
    fig_ranking = px.bar(
        tabla_global
        .sort_values("incidencia", ascending=False)
        .head(15),

        x="incidencia",
        y="departamento",
        orientation="h",
        title="Top 15 Departamentos",
        color="incidencia",
        color_continuous_scale=PALETA_CONTINUA,
        template=TEMPLATE
    )

    return (
        f"{int(total_casos):,}",
        f"{incidencia_acumulada:.2f}",
        fig_sexo,
        fig_zona,
        fig_edad,
        fig_hist,
        fig_box,
        fig_bar_depto,
        fig_box_anual,
        fig_heatmap,
        fig_mapa,
        fig_ranking
    )


# ======================================================
# CALLBACK SERIE TEMPORAL
# ======================================================
@callback(
    Output("eda-serie-incidencia-covariable", "figure"),
    Input("eda-covariable-dropdown", "value"),
    Input("eda-year-dropdown", "value"),
    Input("eda-depto-dropdown", "value")
)
def update_incidencia_covariable(covariable, year, departamento):

    df_filtered = df.copy()

    # ======================================================
    # FILTROS
    # ======================================================
    if year is not None:
        df_filtered = df_filtered[df_filtered["ano"] == year]

    if departamento is not None:
        df_filtered = df_filtered[
            df_filtered["departamento"] == departamento
        ]

    df_filtered = df_filtered.sort_values("fecha_inicio")

    # ======================================================
    # AGREGACIÓN
    # ======================================================
    df_nal = (
        df_filtered
        .groupby("fecha_inicio", as_index=False)
        .agg({"incidencia": "mean"})
    )

    # ======================================================
    # COVARIABLE
    # ======================================================
    if covariable is not None and covariable in df_filtered.columns:

        cov = (
            df_filtered
            .groupby("fecha_inicio", as_index=False)
            .agg({covariable: "mean"})
        )

        df_nal = df_nal.merge(
            cov,
            on="fecha_inicio",
            how="left"
        )

    if df_nal.empty:
        return go.Figure()

    # ======================================================
    # SUAVIZADO
    # ======================================================
    window = 52

    df_nal["media_movil"] = (
        df_nal["incidencia"]
        .rolling(window=window, center=True)
        .mean()
    )

    df_nal["std"] = (
        df_nal["incidencia"]
        .rolling(window=window, center=True)
        .std()
    )

    df_nal["upper"] = (
        df_nal["media_movil"] + df_nal["std"]
    )

    df_nal["lower"] = (
        df_nal["media_movil"] - df_nal["std"]
    ).clip(lower=0)

    # ======================================================
    # FIGURA
    # ======================================================
    fig = plotly.subplots.make_subplots(
        specs=[[{"secondary_y": True}]]
    )

    # Serie original
    fig.add_trace(
        go.Scatter(
            x=df_nal["fecha_inicio"],
            y=df_nal["incidencia"],
            name="Incidencia semanal",
            line=dict(
                width=1,
                color="rgba(108,117,125,0.35)"
            )
        ),
        secondary_y=False
    )

    # Tendencia
    fig.add_trace(
        go.Scatter(
            x=df_nal["fecha_inicio"],
            y=df_nal["media_movil"],
            name="Tendencia suavizada",
            line=dict(
                width=3,
                color="#1F77B4"
            )
        ),
        secondary_y=False
    )

    # Banda superior
    fig.add_trace(
        go.Scatter(
            x=df_nal["fecha_inicio"],
            y=df_nal["upper"],
            line=dict(width=0),
            showlegend=False
        ),
        secondary_y=False
    )

    # Banda inferior
    fig.add_trace(
        go.Scatter(
            x=df_nal["fecha_inicio"],
            y=df_nal["lower"],
            fill="tonexty",
            fillcolor="rgba(31,119,180,0.15)",
            line=dict(width=0),
            name="±1 desviación"
        ),
        secondary_y=False
    )

    # ======================================================
    # COVARIABLE
    # ======================================================
    if covariable is not None and covariable in df_nal.columns:

        df_nal[f"{covariable}_smooth"] = (
            df_nal[covariable]
            .rolling(window=4, min_periods=1)
            .mean()
        )

        fig.add_trace(
            go.Scatter(
                x=df_nal["fecha_inicio"],
                y=df_nal[f"{covariable}_smooth"],
                name=covariable,
                line=dict(
                    dash="dash",
                    width=2,
                    color="#2C3E50"
                )
            ),
            secondary_y=True
        )

    fig.update_layout(
        title="Serie temporal de incidencia y covariables ambientales",
        template=TEMPLATE,
        hovermode="x unified",
        plot_bgcolor="white",
        paper_bgcolor="white",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    fig.update_yaxes(
        title_text="Incidencia",
        secondary_y=False,
        gridcolor="rgba(0,0,0,0.08)"
    )

    if covariable:
        fig.update_yaxes(
            title_text=covariable,
            secondary_y=True
        )

    return fig
    
