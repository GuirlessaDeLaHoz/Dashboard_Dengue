from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

from tabs import (
    prediccion,
    resultados
)
from tabs import contexto
from tabs import introduccion
from tabs import objetivos
from tabs import problema

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY]
)

app.title = "Dashboard Dengue"

app.layout = dbc.Container([

    html.H1(
        "Predicción Espacio-Temporal del Dengue en Colombia",
        className="main-title"
    ),

    dcc.Tabs([

        dcc.Tab(label="Introducción", children=introduccion.layout()),
        dcc.Tab(label="Contexto", children=contexto.layout()),
        dcc.Tab(label="Problema", children=problema.layout()),
        dcc.Tab(label="Objetivos", children=objetivos.layout()),
        dcc.Tab(label="EDA", children=resultados.layout()),
    ])

], fluid=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
