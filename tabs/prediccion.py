import pandas as pd
import numpy as np

from dash import html, dcc, dash_table
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

BASE_DATA = "data"

tabla_metricas = pd.read_csv(
    f"{BASE_DATA}/comparacion_metricas_modelos.csv"
)

print(tabla_metricas.columns.tolist())

tabla_paper = pd.read_csv(
    f"{BASE_DATA}/tabla_paper.csv"
)

matriz_p = pd.read_csv(
    f"{BASE_DATA}/matriz_pvalues_wilcoxon.csv",
    index_col=0
)

wilcoxon_df = pd.read_csv(
    f"{BASE_DATA}/comparacion_wilcoxon.csv"
)

best_rmse = tabla_metricas.loc[
    tabla_metricas["RMSE Mean"].idxmin()
]

best_mae = tabla_metricas.loc[
    tabla_metricas["MAE Mean"].idxmin()
]

best_r2 = tabla_metricas.loc[
    tabla_metricas["R² Mean"].idxmax()
]

def fig_rmse():

    return px.bar(
        tabla_metricas,
        x="Modelo",
        y="RMSE Mean",
        error_y="RMSE Std",
        title="Comparación RMSE"
    )
    
def fig_mae():

    return px.bar(
        tabla_metricas,
        x="Modelo",
        y="MAE Mean",
        error_y="MAE Std",
        title="Comparación MAE"
    )
    
def fig_r2():

    return px.bar(
        tabla_metricas,
        x="Modelo",
        y="R² Mean",
        error_y="R² Std",
        title="Comparación R²"
    )

def fig_wilcoxon():

    return px.imshow(
        matriz_p,
        text_auto=".4f",
        color_continuous_scale="RdYlGn_r",
        title="Matriz de p-values (Wilcoxon)"
    )
    
ranking = tabla_metricas.copy()

ranking["rank_rmse"] = ranking[
    "RMSE Mean"
].rank()

ranking["rank_mae"] = ranking[
    "MAE Mean"
].rank()

ranking["rank_r2"] = ranking[
    "R² Mean"
].rank(
    ascending=False
)

ranking["TOTAL"] = (
    ranking["rank_rmse"]
    + ranking["rank_mae"]
    + ranking["rank_r2"]
)

ranking = ranking.sort_values(
    "TOTAL"
)

def fig_ranking():

    return px.bar(
        ranking,
        x="Modelo",
        y="TOTAL",
        title="Ranking Global"
    )
    
    html.Hr(),

html.H2(
    "Comparación de Modelos",
    style={
        "textAlign":"center",
        "marginTop":"40px"
    }
),

def layout():

    return dbc.Container([

        html.Hr(),

        html.H2(
            "Comparación de Modelos",
            style={
                "textAlign": "center",
                "marginTop": "40px"
            }
        ),

        dbc.Row([

            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H6("Mejor RMSE"),
                        html.H4(best_rmse["Modelo"])
                    ])
                ])
            ),

            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H6("Mejor MAE"),
                        html.H4(best_mae["Modelo"])
                    ])
                ])
            ),

            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H6("Mejor R²"),
                        html.H4(best_r2["Modelo"])
                    ])
                ])
            )

        ]),

        html.Br(),

        html.H4("Tabla Comparativa"),

        dash_table.DataTable(
            data=tabla_paper.to_dict("records"),
            columns=[
                {"name": i, "id": i}
                for i in tabla_paper.columns
            ],
            style_table={
                "overflowX": "auto"
            },
            style_cell={
                "textAlign": "center"
            }
        ),

        html.Br(),

        dcc.Graph(
            figure=fig_rmse()
        ),

        dcc.Graph(
            figure=fig_mae()
        ),

        dcc.Graph(
            figure=fig_r2()
        ),

        dcc.Graph(
            figure=fig_ranking()
        ),

        dcc.Graph(
            figure=fig_wilcoxon()
        ),

        html.H4(
            "Pruebas de Wilcoxon"
        ),

        dash_table.DataTable(
            data=wilcoxon_df.to_dict("records"),
            columns=[
                {"name": i, "id": i}
                for i in wilcoxon_df.columns
            ],
            style_table={
                "overflowX": "auto"
            },
            style_cell={
                "textAlign": "center"
            }
        )

    ], fluid=True)