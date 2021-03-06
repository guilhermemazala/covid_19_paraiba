# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
from textwrap import dedent


app = dash.Dash(__name__)
server = app.server
app.title = "Covid-19 Paraíba"

eixo_dias = ['31-03-2020', '01-04-2020', '02-04-2020', '03-04-2020',
             '04-04-2020', '07-04-2020', '08-04-2020', '13-04-2020',
             '14-04-2020', '15-04-2020', '16-04-2020', '17-04-2020',
             '18-04-2020', '19-04-2020', '20-04-2020', '21-04-2020',
             '22-04-2020']

city_data = {
    'Paraíba': {'dias': eixo_dias,
                'confirmados': [17, 20, 28, 30, 34, 41, 55, 136, 152, 165, 195, 205, 236, 245, 263, 301, 345],
                'recuperados': [3, 3, 3, 3, 9, 11, 14, 52, 52, 80, 80, 90, 90, 99, 116, 116, 116],
                'obitos': [0, 1, 1, 1, 3, 4, 7, 14, 21, 24, 26, 28, 29, 32, 33, 39, 40]},

    'João Pessoa': {'dias': eixo_dias,
                    'confirmados': [12, 14, 22, 24, 26, 30, 40, 103, 115, 124, 142, 148, 163, 172, 185, 205, 230],
                    'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    'obitos': [0, 0, 0, 0, 1, 2, 4, 9, 12, 14, 14, 15, 15, 17, 20, 25, 25]},

    'Santa Rita': {'dias': eixo_dias,
                   'confirmados': [0, 0, 0, 0, 0, 2, 4, 10, 12, 14, 17, 17, 21, 20, 20, 24, 25],
                   'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3]},

    'Campina Grande': {'dias': eixo_dias, 'confirmados': [2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 8, 8, 12, 12, 12, 20, 24],
                       'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2]},

    'Cabedelo': {'dias': eixo_dias, 'confirmados': [0, 1, 1, 1, 1, 1, 2, 5, 5, 6, 7, 8, 9, 9, 11, 12, 15],
                 'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 'obitos': [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]},

    'Bayeux': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 6, 6, 8, 8, 9, 9, 10],
               'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]},

    'Patos': {'dias': eixo_dias, 'confirmados': [1, 1, 1, 0, 1, 1, 1, 4, 4, 4, 5, 5, 7, 8, 8, 8, 8],
              'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              'obitos': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]},

    'Junco do Seridó': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                        'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        'obitos': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]},

    'Sapé': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 3, 8],
             'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]},

    'Igaracy': {'dias': eixo_dias, 'confirmados': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Sousa': {'dias': eixo_dias, 'confirmados': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Serra Branca': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Taperoá': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]},

    'São João do Rio do Peixe': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                 'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Pombal': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2],
               'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Riachão do Poço': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                        'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]},

    'São Bento': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                  'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Congo': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
              'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Queimadas': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                  'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Bom Jesus': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                  'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Cajazeiras': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
                   'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]},

    'Itabaiana': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                  'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Cruz do Espírito Santo': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                               'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Conde': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
              'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Itapororoca': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Barra de São Miguel': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Alagoa Nova': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},

    'Coremas': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
}

cidades_pb = [
    {'label': 'Paraíba', 'value': 'Paraíba'},
    {'label': 'João Pessoa', 'value': 'João Pessoa'},
    {'label': 'Cabedelo', 'value': 'Cabedelo'},
    {'label': 'Patos', 'value': 'Patos'},
    {'label': 'Junco do Seridó', 'value': 'Junco do Seridó'},
    {'label': 'Campina Grande', 'value': 'Campina Grande'},
    {'label': 'Igaracy', 'value': 'Igaracy'},
    {'label': 'Sousa', 'value': 'Sousa'},
    {'label': 'Serra Branca', 'value': 'Serra Branca'},
    {'label': 'Santa Rita', 'value': 'Santa Rita'},
    {'label': 'Bayeux', 'value': 'Bayeux'},
    {'label': 'Sapé', 'value': 'Sapé'},
    {'label': 'Taperoá', 'value': 'Taperoá'},
    {'label': 'São João do Rio do Peixe', 'value': 'São João do Rio do Peixe'},
    {'label': 'Pombal', 'value': 'Pombal'},
    {'label': 'Riachão do Poço', 'value': 'Riachão do Poço'},
    {'label': 'São Bento', 'value': 'São Bento'},
    {'label': 'Congo', 'value': 'Congo'},
    {'label': 'Queimadas', 'value': 'Queimadas'},
    {'label': 'Bom Jesus', 'value': 'Bom Jesus'},
    {'label': 'Cajazeiras', 'value': 'Cajazeiras'},
    {'label': 'Itabaiana', 'value': 'Itabaiana'},
    {'label': 'Cruz do Espírito Santo', 'value': 'Cruz do Espírito Santo'},
    {'label': 'Conde', 'value': 'Conde'},
    {'label': 'Itapororoca', 'value': 'Itapororoca'},
    {'label': 'Barra de São Miguel', 'value': 'Barra de São Miguel'},
    {'label': 'Alagoa Nova', 'value': 'Alagoa Nova'},
    {'label': 'Coremas', 'value': 'Coremas'},
]


def build_modal_info_overlay(id, side, content):
    """
    Build div representing the info overlay for a plot panel
    """
    div = html.Div([  # modal div
        html.Div([  # content div
            html.Div([
                html.H4([
                    "Info",
                    html.Img(
                        id=f'close-{id}-modal',
                        src="assets/times-circle-solid.svg",
                        n_clicks=0,
                        className='info-icon',
                        style={'margin': 0},
                    ),
                ], className="container_title", style={'color': 'white'}),

                dcc.Markdown(
                    content
                ),
            ])
        ],
            className=f'modal-content {side}',
        ),
        html.Div(className='modal')
    ],
        id=f"{id}-modal",
        style={"display": "none"},
    )

    return div


app.layout = html.Div(
    html.Div([
        build_modal_info_overlay('indicator', 'bottom', dedent("""
    A _**Escolha de Cidades**_ é um painel em que você pode selecionar os municípios que você
    deseja ver a evolução do covid-19. Como padrão, mostrará os valores da Paraíba e de 
    João Pessoa.
    A primeira opção selecionada indicará qual informação deve ser mostrada nos
     quadros de valores (suspeitos, confirmados, recuperados e óbitos). Dessa forma, caso
     você queira ver os dados do seu município no Panorama e nos quadros de valores, você deve
     deixá-lo como primeira opção.
     A filtragem funciona apenas para o gráfico de Série Temporal. Ainda não é possível encontrar dados
     de recuperados por município, caso você tenha essa informação e/ou esse meio, entrar em contato em dos
     emails da nota de roda pé.
    """)),
        build_modal_info_overlay('map', 'bottom', dedent("""
    O _**Mapa**_ destaca os municípios que tiveram casos confirmados de covid-19 no estado
    da Paraíba. Ao clicar em um território, você pode visualizar informações detalhadas da região. 
    Os mapas são organizados pela paleta entre amarelo de vermelho, quanto mais vermelho, mais casos relativamente ao total
    de casos no estado, quanto mais amarelo, menos caso relativo a quantidade total de casos do estado.
    """)),
        build_modal_info_overlay('range', 'top', dedent("""
    O _**Panorama Confirmados/Recuperados/Óbitos**_ mostra a quantidade de cada um desses campos no decorrer
    dos dias no estado. Facilita a interpretação da proporção de óbitos e recuperação em relação ao total.

    O campo mostrará a primeira opção selecionada no _**Escolha de Cidades**_.
    """)),
        build_modal_info_overlay('created', 'top', dedent("""
    A _**Série Temporal**_ mostra a quantidade de casos confirmados/recuperados/óbitos por dia, ainda não se tem
    dados de recuperados por município. Caso você selecione mais de 1 município, você poderá comparar a evolução
    do fenômeno.
        """)),

        dcc.Store(id="aggregate_data"),

        #### CABEÇALHO
        html.Div([
            html.H1(children=[
                'Covid-19 (Paraíba)¹²³',
                html.A(
                    html.Img(
                        src="assets/logo_nova-removebg.png",
                        style={'float': 'right', 'height': '150px'}
                    ),

                    href="https://www.instagram.com/labimec/"),
            ], style={'text-align': 'left'}),

            html.H6(children=[
                'Laboratório de Inteligência Artificial e Macroeconomia Computacional - LABIMEC',
            ], style={'text-align': 'left'}),

        ]),

        dcc.Markdown(children=
                     ''' > Atualização Covid-19 22/04 às 20h. Para melhor experiência acesse pelo computador.
        '''),

        # Containers para mostrar os valores
        html.Div(
            [
                # Dropdown para selecionar cidade
                html.Div(
                    [
                        html.H4([
                            "Escolha as cidades que deseja:",
                            html.Img(
                                id='show-indicator-modal',
                                src="assets/question-circle-solid.svg",
                                className='info-icon',
                            ),
                        ], className="container_title"),

                        dcc.Dropdown(
                            id='Cities',
                            options=cidades_pb,
                            value=['Paraíba', 'João Pessoa'],
                            multi=True,
                            className="dcc_control",
                        ),

                        html.P('Filtrar dados por:'),
                        dcc.RadioItems(
                            id="situacao",
                            options=[
                                {"label": "Confirmados ", "value": "confirmados"},
                                {"label": "Recuperados", "value": "recuperados"},
                                {"label": "Óbitos ", "value": "obitos"},
                            ],
                            value="confirmados",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control",
                        ),
                    ],
                    className='six columns pretty_container',
                    id="indicator-div"
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                     html.H4(id="well_text", style={'text-align':'center'}),
                                     html.P(id="well_perc", style={'text-align':'center'}),
                                     html.P("Ativos", style={'text-align':'center'})
                                    ],
                                    id="wells",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H4(id="gasText", style={'text-align':'center'}),
                                     html.P(id="gas_perc", style={'text-align':'center'}),
                                     html.P("Confirmados", style={'text-align':'center'})],
                                    id="gas",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H4(id="oilText", style={'text-align':'center'}),
                                     html.P(id="oil_perc", style={'text-align':'center'}),
                                     html.P("Recuperados", style={'text-align':'center'})],
                                    id="oil",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H4(id="waterText", style={'text-align':'center'}),
                                     html.P(id="water_perc", style={'text-align': 'center'}),
                                     html.P("Óbitos", style={'text-align':'center'})],
                                    id="water",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H4(id="mortalidadeText", style={'text-align': 'center'}),
                                     html.P(id="mortalidade_perc", style={'text-align': 'center'}),
                                     html.P("Mortalidade", style={'text-align': 'center'})],
                                    id="mortalidade",
                                    className="mini_container",
                                ),
                            ],
                            id="info-container",
                            className="row container-display",
                        ),

                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
            style={"zIndex": 1}
        ),

        # Gráficos
        html.Div([
            html.Div(
                children=[
                    html.H4([
                        "Série Temporal dos Municípios Selecionados",
                        html.Img(
                            id='show-created-modal',
                            src="assets/question-circle-solid.svg",
                            className='info-icon',
                        ),
                    ], className="container_title"),

                    # Radio items para selecionar status

                    dcc.Graph(
                        id='example-graph-2',
                    ),
                ],
                className='six columns pretty_container', id="created-div"
            ),

            html.Div(
                children=[
                    html.H4([
                        "Panorama Confirmados/Recuperados/Óbitos",
                        html.Img(
                            id='show-range-modal',
                            src="assets/question-circle-solid.svg",
                            className='info-icon',
                        ),
                    ], className="container_title"),
                    dcc.Graph(
                        id='example-graph',
                    ),
                ],
                className='six columns pretty_container', id="range-div"
            ),
        ]),

        # Mapa
        html.Div(children=[
            html.Div(children=[
                html.H4([
                    "Mapa",
                    html.Img(
                        id='show-map-modal',
                        src="assets/question-circle-solid.svg",
                        className='info-icon',
                    ),
                ], className="container_title"),
                html.Iframe(id='map', srcDoc=open("MAPA_COVID19.html", 'r').read(), width='100%', height=600),
            ], className='nine columns pretty_container',
                style={
                    'float': 'left',
                    'width': '97%',
                    'height': '100%',
                    'margin-right': '0',
                },
                id="map-div"
            ),

            html.Div([
                html.H4(["Total de Casos Confirmados"], style={'text-align': 'center'}),
                html.H3([city_data['Paraíba']['confirmados'][-1]], id='total_casos', style={'text-align': 'center',
                                                                                            'color': 'crimson',
                                                                                            'margin-top': 2,
                                                                                            'height': "20%"}),
            ], className="three columns pretty_container"),

            html.Div([
                html.Div([
                    html.Strong([city_data['João Pessoa']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("João Pessoa", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Santa Rita']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Santa Rita", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Campina Grande']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Campina Grande", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Cabedelo']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Cabedelo", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Bayeux']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Bayeux", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Patos']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Patos", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Sapé']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Sapé", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Junco do Seridó']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Junco do Seridó", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Cajazeiras']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Cajazeiras", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Pombal']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Pombal", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Sousa']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Sousa", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Igaracy']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Igaracy", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Queimadas']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Queimadas", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Congo']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Congo", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['São Bento']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("São Bento", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['São João do Rio do Peixe']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("São João do Rio do Peixe", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Taperoá']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Taperoá", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Riachão do Poço']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Riachão do Povo", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Bom Jesus']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Bom Jesus", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Itabaiana']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Itabaiana", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Cruz do Espírito Santo']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Cruz do Espírito Santo", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                    html.Strong([city_data['Conde']['confirmados'][-1]],
                                style={'color': 'crimson', 'font-size': 20}),
                    html.Span(" "),
                    html.Span("Conde", style={'font-size': 20}),
                    html.Hr(style={'margin': 0}),

                ], className="control-tab"),

            ], className="three columns pretty_container",
                style={"overflowX": "scroll", 'text-align': 'left', 'height': 500}),
        ]),

        # Notas de roda pé
        html.Div([
            dcc.Markdown(
                children='''
           ¹ O Dashboard apresentado trata-se de uma iniciativa do Laboratório da Inteligência Artificial e Macroeconomia Computacional (LABIMEC), 
             ainda em versão de testes. O propósito é facilitar a visualização dos casos de coronavírus no estado da Paraíba e em seus municípios. Algumas funcionalidades
             estão sendo implementadas pela equipe do laboratório, para sugestões entrar em contato nos seguintes emails:
             * cassiodanobrega@yahoo.com.br - Coordenador do LABIMEC
             * flaviomacaubas@gmail.com - Membro do LABIMEC
             '''),

            dcc.Markdown(
                children='''
           ² Os dados disponibilizados são provenientes dos [Boletins Epidemiológicos Coronavírus / Covid-19](https://paraiba.pb.gov.br/diretas/saude/consultas/vigilancia-em-saude-1/boletins-epidemiologicos)
            da Secretaria de Saúde de Estado da Paraíba. Não há dados de recuperados discriminados por município, por esta razão não é possível gerar 
            os gráficos de série temporal.
           '''),

            dcc.Markdown(
                children='''
          ³ O Dashboard não substitui, sob qualquer hipótese, os dados oficiais do Governo do Estado da Paraíba.
          ''')
        ])

    ], id="mainContainer", style={"display": "flex", "flex-direction": "column"}
    )
)

# Adiciona e remove os dados de ajuda
for id in ['indicator', 'map', 'range', 'created']:
    @app.callback([Output(f"{id}-modal", 'style'), Output(f"{id}-div", 'style')],
                  [Input(f'show-{id}-modal', 'n_clicks'),
                   Input(f'close-{id}-modal', 'n_clicks')])
    def toggle_modal(n_show, n_close):
        ctx = dash.callback_context
        if ctx.triggered and ctx.triggered[0]['prop_id'].startswith('show-'):
            return {"display": "block"}, {'zIndex': 1003}
        else:
            return {"display": "none"}, {'zIndex': 0}


# Atualiza gráfico de barras
@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('Cities', 'value')])
def update_image_src(selector):
    if len(selector) == 0:
        selector.append('Paraíba')
    data = []
    if selector[0] == "Paraíba":
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['confirmados'],
                     'type': 'bar', 'name': 'Confirmados', 'marker': {"color": 'crimson'}})
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['recuperados'],
                     'type': 'bar', 'name': 'Recuperados', 'marker': {"color": 'blue'}})
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['obitos'],
                     'type': 'bar', 'name': 'Óbitos', 'marker': {"color": 'black'}})
    else:
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['confirmados'],
                     'type': 'bar', 'name': 'Confirmados', 'marker': {"color": 'crimson'}})
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['obitos'],
                     'type': 'bar', 'name': 'Óbitos', 'marker': {"color": 'black'}})
    figure = {
        'data': data,
        'layout': {
            'height': 350,
            'xaxis': dict(
                title='Dia',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=20,
                    color='#7f7f7f'
                )),
            'yaxis': dict(
                title='Quantidade',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f'
                )),
            'barmode': 'group',
            'bargap': 0.2,
            'bargroupgap': 0.15,
        }
    }
    return figure


# Atualiza gráfico de linha
@app.callback(
    dash.dependencies.Output('example-graph-2', 'figure'),
    [dash.dependencies.Input('Cities', 'value'), dash.dependencies.Input('situacao', 'value')])
def update_image_src(selector, situacao):
    if len(selector) == 0:
        selector.append('Paraíba')
    data = []
    for city in selector:
        data.append({'x': city_data[city]['dias'], 'y': city_data[city][situacao],
                     'type': 'line', 'name': city})
    figure = {
        'data': data,
        'layout': {
            'height': 350,
            'xaxis': dict(
                title='Dia',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=20,
                    color='#7f7f7f'
                )),
            'yaxis': dict(
                title='Quantidade',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f'
                ))
        }
    }
    return figure


@app.callback(
    [
        Output("well_text", "children"),
        Output("well_perc", "children"),
        Output("gasText", "children"),
        Output("gas_perc", "children"),
        Output("oilText", "children"),
        Output("oil_perc", "children"),
        Output("waterText", "children"),
        Output("water_perc", "children"),
        Output("mortalidadeText", "children"),
        Output("mortalidade_perc", "children"),
    ],
    [Input("aggregate_data", "data"), dash.dependencies.Input('Cities', 'value')],
)
def update_text(data, selector):

    def formata_saida(valor):
        if valor > 0:
            return "▲ {:.1f}%".format(valor)
        elif valor == 0:
            return "{:.1f}%".format(valor)
        else:
            return "▼ {:.1f}%".format(valor)

    if len(selector) == 0:
        selecionado = 'Paraíba'
    else:
        selecionado = selector[0]

    # Preparando dados
    #ativos
    ativos_inicial = (city_data[selecionado]['confirmados'][-2] - city_data[selecionado]['recuperados'][-2] -
            city_data[selecionado]['obitos'][-2])

    if ativos_inicial <= 0:
        ativos_inicial = 1

    #confirmados
    confirmados_inicial = city_data[selecionado]['confirmados'][-2]

    if confirmados_inicial <= 0:
        confirmados_inicial = 1

    #recuperados
    recuperados_inicial = city_data[selecionado]['recuperados'][-2]

    if recuperados_inicial <= 0:
        recuperados_inicial = 1

    #obitos
    obitos_inicial = city_data[selecionado]['obitos'][-2]

    if obitos_inicial <= 0:
        obitos_inicial = 1

    # Mortalidade e Recuperacao
    confirmados_final = city_data[selecionado]['confirmados'][-1]
    confirmados_passado = city_data[selecionado]['confirmados'][-2]

    if confirmados_final == 0:
        confirmados_final = 1

    if confirmados_passado == 0:
        confirmados_passado = 1

    mortalidade_atual = ( city_data[selecionado]['obitos'][-1]/confirmados_final ) * 100
    mortalidade_passado = (city_data[selecionado]['obitos'][-2]/confirmados_passado) * 100

    variacao_mortalidade = ( ( mortalidade_atual - mortalidade_passado)* 100 )/ mortalidade_passado

    # Dados de sáida

    ativos = (city_data[selecionado]['confirmados'][-1] - city_data[selecionado]['recuperados'][-1] -
            city_data[selecionado]['obitos'][-1])

    novos_ativos = ( (city_data[selecionado]['confirmados'][-1] - city_data[selecionado]['recuperados'][-1] -
            city_data[selecionado]['obitos'][-1]) - (city_data[selecionado]['confirmados'][-2] - city_data[selecionado]['recuperados'][-2] -
            city_data[selecionado]['obitos'][-2]) ) * 100/ ativos_inicial


    novos_confirmados = ( city_data[selecionado]['confirmados'][-1] - city_data[selecionado]['confirmados'][-2] ) * 100 / confirmados_inicial

    novos_recuperados = ( city_data[selecionado]['recuperados'][-1] - city_data[selecionado]['recuperados'][-2] ) * 100 / recuperados_inicial

    novos_obitos = ( city_data[selecionado]['obitos'][-1] - city_data[selecionado]['obitos'][-2] ) * 100 / obitos_inicial



    return "{}".format(ativos), \
           formata_saida(novos_ativos), \
           "{}".format(city_data[selecionado]['confirmados'][-1]), \
           formata_saida(novos_confirmados), \
           "{}".format(city_data[selecionado]['recuperados'][-1]), \
           formata_saida(novos_recuperados), \
           "{}".format(city_data[selecionado]['obitos'][-1]), \
           formata_saida(novos_obitos), \
           "{:.1f}%".format(mortalidade_atual), \
           formata_saida(variacao_mortalidade),


@app.callback(
    [
        Output('well_perc', 'style'),
        Output('gas_perc', 'style'),
        Output('oil_perc', 'style'),
        Output('water_perc', 'style'),
        Output('mortalidade_perc', 'style'),
    ],
    [
        Input("well_perc", "children"),
        Input("gas_perc", "children"),
        Input("oil_perc", "children"),
        Input("water_perc", "children"),
        Input("mortalidade_perc", "children"),
    ])
def atualiza_style(valor_well, valor_gas, valor_oil, valor_water, valor_mortalidade):
    lista_styles=[]
    for valores in [valor_well,valor_gas,valor_oil,valor_water, valor_mortalidade]:
        if "▲" in valores:
            lista_styles.append([{'text-align': 'center', 'color':'green'}])
        elif "▼" in valores:
            lista_styles.append([{'text-align': 'center', 'color':'red'}])
        else:
            lista_styles.append([{'text-align': 'center', 'color':'black'}])

    return lista_styles[0][0], lista_styles[1][0], lista_styles[2][0], lista_styles[3][0], lista_styles[4][0]
  
if __name__ == '__main__':
    app.run_server()
