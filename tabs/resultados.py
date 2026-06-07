import json

from dash import html, dcc, Input, Output, callback  # type: ignore[import]
try:
    import dash_bootstrap_components as dbc
except ImportError:
    dbc = None
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots
import geopandas as gpd

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

COLORES_COV = ["#E74C3C", "#2ECC71", "#F39C12", "#9B59B6"]

TEMPLATE = "plotly_white"

DESC_STYLE = {
    "color": "#6C757D",
    "fontSize": "0.85rem",
    "marginTop": "6px",
    "fontStyle": "italic",
    "lineHeight": "1.4"
}

# ======================================================
# CARGA DE DATOS
# ======================================================
df = pd.read_csv("data/df_full.csv")
df["fecha_inicio"] = pd.to_datetime(df["fecha_inicio"])

# Cargar shapefile UNA SOLA VEZ y simplificar geometria
_mapa_base = gpd.read_file(
    "data/MGN_ADM_DPTO_POLITICO/MGN_ADM_DPTO_POLITICO_limpio.shp"
)
_mapa_base = gpd.GeoDataFrame(
    _mapa_base[["dpto_cnmbr", "geometry"]].copy(),
    geometry="geometry"
)
_mapa_base["geometry"] = _mapa_base["geometry"].simplify(
    tolerance=0.01,
    preserve_topology=True
)
_GEOJSON = json.loads(_mapa_base.to_json())


# ======================================================
# LAYOUT
# ======================================================
def layout():

    return dbc.Container([

        html.Br(),

        html.H2(
            "Resultados del Proyecto",
            style={"color": "#0B3C5D", "fontWeight": "bold"}
        ),

        html.Hr(),

        html.H3(
            "Exploratory Data Analysis (EDA)",
            style={"color": "#0B3C5D", "fontWeight": "bold"}
        ),

        html.P(
            "Analisis exploratorio de la incidencia de dengue en Colombia (2012-2024).",
            style={"color": "#6C757D"}
        ),

        # ======================================================
        # FILTROS
        # ======================================================
        dbc.Row([

            dbc.Col([
                html.Label("Periodo de analisis"),
                dcc.RangeSlider(
                    id="eda-year-range",
                    min=int(df["ano"].min()),
                    max=int(df["ano"].max()),
                    value=[int(df["ano"].min()), int(df["ano"].max())],
                    marks={int(y): str(y) for y in sorted(df["ano"].unique())},
                    step=1,
                    tooltip={"placement": "bottom", "always_visible": True}
                )
            ], width=5),

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
        # SUBPESTANAS EDA
        # ======================================================
        dbc.Tabs([

            # ======================================================
            # TAB 1 - CARACTERIZACION
            # ======================================================
            dbc.Tab(
                label="Caracterizacion de la Poblacion",
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
                                        style={"color": "#1F77B4", "fontWeight": "bold"}
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
                                        style={"color": "#4C78A8", "fontWeight": "bold"}
                                    )
                                ])
                            ], className="shadow-sm border-0"),
                            width=4
                        )
                    ], className="mb-5"),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="eda-pie-sexo"),
                            html.Div(id="eda-desc-sexo", style=DESC_STYLE)
                        ], width=4),
                        dbc.Col([
                            dcc.Graph(id="eda-bar-edad"),
                            html.Div(id="eda-desc-edad", style=DESC_STYLE)
                        ], width=4),
                        dbc.Col([
                            dcc.Graph(id="eda-pie-zona"),
                            html.Div(id="eda-desc-zona", style=DESC_STYLE)
                        ], width=4)
                    ], className="mb-5")
                ]
            ),

            # ======================================================
            # TAB 2 - DISTRIBUCION
            # ======================================================
            dbc.Tab(
                label="Distribucion de la Incidencia",
                tab_id="incidencia",
                children=[

                    html.Br(),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="eda-hist-incidencia"),
                            html.Div(id="eda-desc-hist", style=DESC_STYLE)
                        ], width=6),
                        dbc.Col([
                            dcc.Graph(id="eda-box-incidencia"),
                            html.Div(id="eda-desc-box", style=DESC_STYLE)
                        ], width=6)
                    ], className="mb-5"),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="eda-bar-incidencia-depto"),
                            html.Div(id="eda-desc-bar-depto", style=DESC_STYLE)
                        ], width=12)
                    ], className="mb-5")
                ]
            ),

            # ======================================================
            # TAB 3 - ESPACIO-TEMPORAL
            # ======================================================
            dbc.Tab(
                label="Analisis Espacio-Temporal",
                tab_id="espacio_temporal",
                children=[

                    html.Br(),

                    dbc.Row([
                        dbc.Col(
                            dbc.Card([
                                dbc.CardBody([
                                    html.H6("Periodo analizado", style={"color": "#0B3C5D"}),
                                    html.H4("2012-2024", style={"fontWeight": "bold", "color": "#1E3A8A"}),
                                    html.P("13 anos · ~676 semanas", style={"color": "#6C757D"})
                                ])
                            ], className="shadow-sm border-0"),
                            width=3
                        ),
                        dbc.Col(
                            dbc.Card([
                                dbc.CardBody([
                                    html.H6("Pico epidemico maximo", style={"color": "#0B3C5D"}),
                                    html.H4("2023-2024", style={"fontWeight": "bold", "color": "#1E3A8A"}),
                                    html.P("Mas intenso de la serie", style={"color": "#6C757D"})
                                ])
                            ], className="shadow-sm border-0"),
                            width=3
                        ),
                        dbc.Col(
                            dbc.Card([
                                dbc.CardBody([
                                    html.H6("Ciclos epidemicos", style={"color": "#0B3C5D"}),
                                    html.H4("~4-5 anos", style={"fontWeight": "bold", "color": "#1E3A8A"}),
                                    html.P("2013-14 · 2019-20 · 2023-24", style={"color": "#6C757D"})
                                ])
                            ], className="shadow-sm border-0"),
                            width=3
                        ),
                        dbc.Col(
                            dbc.Card([
                                dbc.CardBody([
                                    html.H6("Estacionariedad (ADF)", style={"color": "#0B3C5D"}),
                                    html.H4("No estacionaria", style={"fontWeight": "bold", "color": "#1E3A8A"}),
                                    html.P("p-value 0.080 · cercano al umbral", style={"color": "#6C757D"})
                                ])
                            ], className="shadow-sm border-0"),
                            width=3
                        )
                    ], className="mb-4"),

                    html.H5(
                        "Serie temporal de incidencia y covariables ambientales",
                        style={"color": "#0B3C5D", "fontWeight": "bold"}
                    ),

                    dbc.Row([
                        dbc.Col([
                            html.Label("Selecciona Covariable(s)"),
                            dcc.Dropdown(
                                id="eda-covariable-dropdown",
                                options=[
                                    {"label": "Precipitacion (lag 4)", "value": "precip_lag_4"},
                                    {"label": "Temperatura Media",      "value": "temp_c"},
                                    {"label": "Humedad Relativa",       "value": "humedad_relativa"}
                                ],
                                value=None,
                                multi=True,
                                placeholder="Selecciona covariables...",
                                clearable=True
                            )
                        ], width=3),
                        dbc.Col([
                            dcc.Graph(id="eda-serie-incidencia-covariable"),
                            html.Div(id="eda-desc-serie", style=DESC_STYLE)
                        ], width=9)
                    ], className="mb-5"),

                    html.H5(
                        "Distribucion y variabilidad anual de la incidencia",
                        style={"color": "#0B3C5D", "fontWeight": "bold"}
                    ),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="eda-box-anual"),
                            html.Div(id="eda-desc-box-anual", style=DESC_STYLE)
                        ], width=12)
                    ], className="mb-5"),

                    html.H5(
                        "Heatmap de incidencia semanal por ano",
                        style={"color": "#0B3C5D", "fontWeight": "bold"}
                    ),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="eda-heatmap"),
                            html.Div(id="eda-desc-heatmap", style=DESC_STYLE)
                        ], width=12)
                    ], className="mb-5"),

                    html.H5(
                        "Distribucion espacial y ranking nacional",
                        style={"color": "#0B3C5D", "fontWeight": "bold"}
                    ),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="eda-mapa-incidencia"),
                            html.Div(id="eda-desc-mapa", style=DESC_STYLE)
                        ], width=6),
                        dbc.Col([
                            dcc.Graph(id="eda-ranking-incidencia"),
                            html.Div(id="eda-desc-ranking", style=DESC_STYLE)
                        ], width=6)
                    ], className="mb-5")

                ]
            )

        ], id="eda-subtabs", active_tab="caracterizacion")

    ], fluid=True)


# ======================================================
# CALLBACK PRINCIPAL
# ======================================================
@callback(
    # Figuras
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
    # Descripciones Tab 1
    Output("eda-desc-sexo", "children"),
    Output("eda-desc-edad", "children"),
    Output("eda-desc-zona", "children"),
    # Descripciones Tab 2
    Output("eda-desc-hist", "children"),
    Output("eda-desc-box", "children"),
    Output("eda-desc-bar-depto", "children"),
    # Descripciones Tab 3
    Output("eda-desc-box-anual", "children"),
    Output("eda-desc-heatmap", "children"),
    Output("eda-desc-mapa", "children"),
    Output("eda-desc-ranking", "children"),
    # Inputs
    Input("eda-year-range", "value"),
    Input("eda-depto-dropdown", "value")
)
def update_dashboard(year_range, departamento):

    df_filtered = df.copy()

    if year_range is not None:
        start_year, end_year = year_range
        df_filtered = df_filtered[
            (df_filtered["ano"] >= start_year) &
            (df_filtered["ano"] <= end_year)
        ]

    df_filtered_depto = df_filtered.copy()

    if departamento is not None:
        df_filtered_depto = df_filtered_depto[
            df_filtered_depto["departamento"] == departamento
        ]

    df_depto = df.copy()
    if departamento is not None:
        df_depto = df_depto[df_depto["departamento"] == departamento]

    periodo = f"{start_year}-{end_year}"
    label = periodo if departamento is None else f"{departamento} ({periodo})"

    # ======================================================
    # METRICAS
    # ======================================================
    total_casos = df_filtered_depto["casos"].sum()
    incidencia_acumulada = df_filtered_depto["incidencia"].mean()

    # ======================================================
    # SEXO
    # ======================================================
    total_m = df_filtered_depto["casos_mujeres"].sum()
    total_h = df_filtered_depto["casos_hombres"].sum()

    fig_sexo = px.pie(
        names=["Mujeres", "Hombres"],
        values=[total_m, total_h],
        title=f"Proporcion Casos por Sexo ({label})",
        color_discrete_sequence=PALETA_CATEGORICA,
        template=TEMPLATE
    )

    # ======================================================
    # ZONA
    # ======================================================
    casos_rural  = df_filtered_depto["casos_rural"].sum()
    casos_urbano = df_filtered_depto["casos_urbano"].sum()

    fig_zona = px.pie(
        names=["Rural", "Urbano"],
        values=[casos_rural, casos_urbano],
        title=f"Proporcion Casos por Zona ({label})",
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
        title=f"Distribucion de incidencia ({label})",
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
        title="Distribucion anual de incidencia",
        color_discrete_sequence=PALETA_CATEGORICA,
        template=TEMPLATE
    )

    # ======================================================
    # HEATMAP - sin filtro de ano, siempre serie completa
    # ======================================================
    df_heatmap = df.copy()
    if departamento is not None:
        df_heatmap = df_heatmap[df_heatmap["departamento"] == departamento]

    heatmap_df = (
        df_heatmap
        .groupby(["ano", "semana"])["incidencia"]
        .mean()
        .reset_index()
    )

    matriz = heatmap_df.pivot(index="ano", columns="semana", values="incidencia")

    fig_heatmap = px.imshow(
        matriz,
        color_continuous_scale=PALETA_CONTINUA,
        aspect="auto",
        title="Estacionalidad semanal (serie completa 2012-2024)"
    )

    # ======================================================
    # MAPA
    # ======================================================
    tabla_global = (
        df_filtered.groupby("departamento")["incidencia"]
        .mean()
        .reset_index()
    )

    mapa_plot = _mapa_base[["dpto_cnmbr"]].copy()
    mapa_plot = mapa_plot.merge(
        tabla_global,
        left_on="dpto_cnmbr",
        right_on="departamento",
        how="left"
    )
    mapa_plot["incidencia"] = mapa_plot["incidencia"].astype(float).fillna(0.0)

    fig_mapa = px.choropleth(
        mapa_plot,
        geojson=_GEOJSON,
        featureidkey="properties.dpto_cnmbr",
        locations="dpto_cnmbr",
        color="incidencia",
        projection="mercator",
        color_continuous_scale=PALETA_CONTINUA,
        template=TEMPLATE
    )
    fig_mapa.update_geos(fitbounds="locations", visible=False)

    # ======================================================
    # RANKING
    # ======================================================
    fig_ranking = px.bar(
        tabla_global.sort_values("incidencia", ascending=False).head(15),
        x="incidencia",
        y="departamento",
        orientation="h",
        title="Top 15 Departamentos",
        color="incidencia",
        color_continuous_scale=PALETA_CONTINUA,
        template=TEMPLATE
    )

    # ======================================================
    # DESCRIPCIONES DINAMICAS
    # ======================================================

    # --- Tab 1: Sexo ---
    pct_m = total_m / (total_m + total_h) * 100 if (total_m + total_h) > 0 else 0
    sexo_dom = "mujeres" if total_m > total_h else "hombres"
    desc_sexo = (
        f"El {pct_m:.1f}% de los casos corresponden a mujeres. "
        f"Los casos predominan en {sexo_dom}, patron consistente con "
        f"la mayor exposicion vectorial en actividades del hogar."
    )

    # --- Tab 1: Edad ---
    grupo_max = grupos[list(valores).index(max(valores))]
    desc_edad = (
        f"El grupo de edad con mayor carga de casos es {grupo_max}. "
        f"Una concentracion en adultos (14-59) sugiere exposicion laboral o escolar. "
    )

    # --- Tab 1: Zona ---
    total_zona = casos_rural + casos_urbano
    pct_urb = casos_urbano / total_zona * 100 if total_zona > 0 else 0
    zona_dom = "urbana" if casos_urbano > casos_rural else "rural"
    desc_zona = (
        f"El {pct_urb:.1f}% de los casos ocurren en zona urbana. "
        f"La predominancia {zona_dom} refleja la distribucion del vector "
        f"Aedes aegypti y la densidad poblacional en el area."
    )

    # --- Tab 2: Histograma ---
    inc_media = df_filtered_depto["incidencia"].mean()
    inc_max   = df_filtered_depto["incidencia"].max()
    desc_hist = (
        f"Distribucion de la incidencia semanal por 100.000 habitantes. "
        f"La incidencia media es {inc_media:.2f} y el maximo registrado es {inc_max:.2f}. "
        f"Una distribucion con cola larga a la derecha indica la presencia de semanas "
        f"epidemicas con valores extremos."
    )

    # --- Tab 2: Boxplot ---
    inc_q75 = df_filtered_depto["incidencia"].quantile(0.75)
    inc_med  = df_filtered_depto["incidencia"].median()
    desc_box = (
        f"La mediana de incidencia es {inc_med:.2f} casos por 100.000 hab. "
        f"El 75% de las semanas registran menos de {inc_q75:.2f}. "
        f"Los puntos fuera de los bigotes representan semanas epidemicas atipicas."
    )

    # --- Tab 2: Bar departamentos ---
    depto_top = espacial.iloc[0]["departamento"] if not espacial.empty else "N/A"
    inc_top   = espacial.iloc[0]["incidencia"]   if not espacial.empty else 0
    desc_bar_depto = (
        f"Incidencia media por departamento en el periodo seleccionado. "
        f"{depto_top} presenta la mayor incidencia promedio ({inc_top:.2f} x100k). "
        f"Las diferencias entre departamentos reflejan variaciones climaticas, "
        f"demograficas y de capacidad de vigilancia epidemiologica."
    )

    # --- Tab 3: Boxplot anual ---
    ano_max = df_depto.groupby("ano")["incidencia"].mean().idxmax() if not df_depto.empty else "N/A"
    desc_box_anual = (
        f"Cada caja resume la variabilidad semanal de incidencia dentro de un ano. "
        f"El ano {ano_max} presenta la mayor incidencia media del periodo. "
        f"Cajas mas anchas indican anos con mayor heterogeneidad entre semanas."
    )

    # --- Tab 3: Heatmap ---
    desc_heatmap = (
        "Cada celda muestra la incidencia media para una semana epidemiologica y un ano. "
        "Los colores mas oscuros indican mayor intensidad de transmision. "
        "Columnas con colores consistentemente altos revelan semanas de mayor riesgo estacional "
        "(generalmente semanas 1-15 y 40-52, asociadas a lluvias)."
    )

    # --- Tab 3: Mapa ---
    desc_mapa = (
        f"Mapa coropletico de incidencia media departamental en {periodo}. "
        f"Los tonos mas oscuros indican mayor carga de enfermedad. "
        f"Permite identificar los focos geograficos de transmision prioritarios."
    )

    # --- Tab 3: Ranking ---
    n_deptos = len(tabla_global)
    desc_ranking = (
        f"Top 15 departamentos por incidencia media en {periodo} "
        f"(de {n_deptos} departamentos con datos). "
        f"Permite priorizar territorios para intervencion y vigilancia reforzada."
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
        fig_ranking,
        # Descripciones Tab 1
        desc_sexo,
        desc_edad,
        desc_zona,
        # Descripciones Tab 2
        desc_hist,
        desc_box,
        desc_bar_depto,
        # Descripciones Tab 3
        desc_box_anual,
        desc_heatmap,
        desc_mapa,
        desc_ranking
    )


# ======================================================
# CALLBACK SERIE TEMPORAL
# ======================================================
@callback(
    Output("eda-serie-incidencia-covariable", "figure"),
    Output("eda-desc-serie", "children"),
    Input("eda-covariable-dropdown", "value"),
    Input("eda-year-range", "value"),
    Input("eda-depto-dropdown", "value")
)
def update_incidencia_covariable(covariables, year_range, departamento):

    # Normalizar input
    if not covariables:
        covariables = []
    elif isinstance(covariables, str):
        covariables = [covariables]

    df_filtered = df.copy()

    if year_range is not None:
        start_year, end_year = year_range
        df_filtered = df_filtered[
            (df_filtered["ano"] >= start_year) &
            (df_filtered["ano"] <= end_year)
        ]

    if departamento is not None:
        df_filtered = df_filtered[
            df_filtered["departamento"] == departamento
        ]

    df_filtered = df_filtered.sort_values("fecha_inicio")

    df_nal = (
        df_filtered
        .groupby("fecha_inicio", as_index=False)
        .agg({"incidencia": "mean"})
    )

    for cov in covariables:
        if cov in df_filtered.columns:
            cov_df = (
                df_filtered
                .groupby("fecha_inicio", as_index=False)
                .agg({cov: "mean"})
            )
            df_nal = df_nal.merge(cov_df, on="fecha_inicio", how="left")

    if df_nal.empty:
        return go.Figure(), ""

    # Ventana adaptativa
    n_semanas = len(df_nal)
    window = min(52, max(4, n_semanas // 4))

    df_nal["media_movil"] = (
        df_nal["incidencia"]
        .rolling(window=window, center=True, min_periods=1)
        .mean()
    )
    df_nal["std"] = (
        df_nal["incidencia"]
        .rolling(window=window, center=True, min_periods=4)
        .std()
    )
    df_nal["upper"] = df_nal["media_movil"] + df_nal["std"]
    df_nal["lower"] = (df_nal["media_movil"] - df_nal["std"]).clip(lower=0)

    fig = plotly.subplots.make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(
            x=df_nal["fecha_inicio"],
            y=df_nal["incidencia"],
            name="Incidencia semanal",
            line=dict(width=1, color="rgba(108,117,125,0.35)")
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=df_nal["fecha_inicio"],
            y=df_nal["media_movil"],
            name="Tendencia suavizada",
            line=dict(width=3, color="#1F77B4")
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=df_nal["fecha_inicio"],
            y=df_nal["upper"],
            line=dict(width=0),
            showlegend=False
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=df_nal["fecha_inicio"],
            y=df_nal["lower"],
            fill="tonexty",
            fillcolor="rgba(31,119,180,0.15)",
            line=dict(width=0),
            name="+/-1 desviacion"
        ),
        secondary_y=False
    )

    # Covariables normalizadas (Z-score)
    for i, cov in enumerate(covariables):
        if cov in df_nal.columns:
            df_nal[f"{cov}_smooth"] = (
                df_nal[cov].rolling(window=4, min_periods=1).mean()
            )
            serie = df_nal[f"{cov}_smooth"]
            serie_norm = (serie - serie.mean()) / serie.std()

            fig.add_trace(
                go.Scatter(
                    x=df_nal["fecha_inicio"],
                    y=serie_norm,
                    name=f"{cov} (norm.)",
                    customdata=df_nal[f"{cov}_smooth"].round(2),
                    hovertemplate="%{customdata}",
                    line=dict(
                        dash="dash",
                        width=2,
                        color=COLORES_COV[i % len(COLORES_COV)]
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
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    fig.update_yaxes(
        title_text="Incidencia",
        secondary_y=False,
        gridcolor="rgba(0,0,0,0.08)"
    )

    if covariables:
        fig.update_yaxes(title_text="Covariables (Z-score)", secondary_y=True)

    # Descripcion dinamica de la serie
    if covariables:
        nombres = ", ".join(covariables)
        desc_serie = (
            f"Serie semanal de incidencia con tendencia suavizada (ventana={window} semanas) "
            f"y banda de +/-1 desviacion estandar. "
            f"Las covariables ({nombres}) se muestran normalizadas (Z-score) en el eje derecho "
            f"para facilitar la comparacion visual de patrones temporales con la incidencia."
        )
    else:
        desc_serie = (
            f"Serie semanal de incidencia con tendencia suavizada (ventana={window} semanas) "
            f"y banda de +/-1 desviacion estandar. "
            f"Los picos indican semanas epidemicas; la banda muestra la variabilidad tipica del periodo."
        )

    return fig, desc_serie