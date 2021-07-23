import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_daq as daq
import plotly
import dash_auth
import csv
from dash.dependencies import Input, Output
import smtp_alert

#аутентификация
with open('login.txt', 'r') as f:
    for line in f:
        line = line.strip()
        login, password = line.split(' ')
VALID_USERNAME_PASSWORD_PAIRS = {
    login: password
}

# стиль
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
    ]

# приложение
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
app.title = "Управление промышленными помещениями"
app.layout = html.Div([
        html.Div(
            children=[
                html.H1(
                    children="Помещение 1", className="header-title"),
                html.P(
                    children="Просмотр актуальных данных с датчиков.\n"
                    " Управление установленными устройствами.",
                    className="header-description",
                ),
            ],
            className="header",
            style={"margin-bottom": "25px"},
        ),
        html.Div([
                html.Div([
                        html.H4(
                            "Показатели:",
                            className="control_label",
                        ),
                        html.Div([
                                html.Div(
                                    [html.H6(id="temp_text"), html.P("Температура по Цельсию: "),
                                     html.Div([
                                         html.Div(id='live-update-text1'),
                                         dcc.Interval(
                                             id='interval-component1',
                                             interval=2*1000, # in milliseconds
                                             n_intervals=0
                                             )
                                         ]),
                                     html.P("Норма: 19-28 "),
                                     html.P("Файл статистики: C:\ nucleo_klient \ temp.csv ")],
                                    id="temp",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="hum_text"), html.P("Влажность в %: "),
                                     html.Div([
                                         html.Div(id='live-update-text2'),
                                         dcc.Interval(
                                             id='interval-component2',
                                             interval=2*1000, # in milliseconds
                                             n_intervals=0
                                             )
                                         ]),
                                    html.P("Норма: 30-55 "),
                                    html.P("Файл статистики: C:\ nucleo_klient \ hum.csv ")],
                                    id="hum",
                                    className="mini_container",
                                ),
                            ],)
                    ],
                    className="pretty_container four columns",
                    id="left-column",
                ),
                html.Div([                    
                        html.H4(
                            "Управление устройствами:",
                            style={
                                "margin-bottom": "15px",
                                },
                            className="control_label",
                        ),
                        html.Div(
                            children=[
                            html.Div([
                                    html.Div([
                                            daq.BooleanSwitch(
                                            id='switch1',
                                            color="#ff9900",
                                            label="Кондиционер",
                                            labelPosition="top"
                                        ),                                        
                                        html.Div(id='boolean-switch1-output')
                                        ],),
                                ],
                                    id="ref1",
                                    className="mini_container",
                                ),
                            html.Div([
                                    html.Div([
                                            daq.BooleanSwitch(
                                            id='switch2',
                                            color="#ff9900",
                                            label="Основное свещение",
                                            labelPosition="top"
                                        ),
                                        html.Div(id='boolean-switch2-output')
                                        ],),
                                ],
                                    id="ref2",
                                    className="mini_container",
                                ),
                            html.Div([
                                    html.Div([
                                            daq.BooleanSwitch(
                                            id='switch3',
                                            color="#ff9900",
                                            label="Вентиляция",
                                            labelPosition="top"
                                        ),
                                        html.Div(id='boolean-switch3-output')
                                        ],),
                                ],
                                    id="ref3",
                                    className="mini_container",
                                ),
                            html.Div([
                                    html.Div([
                                            daq.BooleanSwitch(
                                            id='switch4',
                                            color="#ff9900",
                                            label="Дополнительное освещение",
                                            labelPosition="top"
                                        ),
                                        html.Div(id='boolean-switch4-output')
                                        ],),
                                ],
                                    id="ref4",
                                    className="mini_container",
                                ),
                            ],),
                    ],
                    id="right-column",
                    className="pretty_container four columns"
                ),
            ],
            className="row flex-display",
        ),                
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)

@app.callback(Output('live-update-text1', 'children'),
              Input('interval-component1', 'n_intervals'))
def update_metrics(n):
    with open("temp.csv","r") as file:
        data = file.readlines()
        lastRow = data[-1]
        temp = lastRow[27]+lastRow[28]
        t = int(temp)
        indicator = "ТЕМПЕРАТУРА"
        if t < 19:
            smtp_alert.send_alert(indicator)
        elif t > 28:
            smtp_alert.send_alert(indicator)
    style = {'padding': '5px', 'fontSize': '24px', 'font-weight' : 'bold',"color":"#ff7700",}
    return [
        html.Span(temp, style=style)
    ]

@app.callback(Output('live-update-text2', 'children'),
              Input('interval-component2', 'n_intervals'))
def update_metrics(n):
    with open("hum.csv","r") as file:
        data = file.readlines()
        lastRow = data[-1]
        hum = lastRow[27]+lastRow[28]
        h = int(hum)
        indicator = "ВЛАЖНОСТЬ"
        if h < 30:
            smtp_alert.send_alert(indicator)
        elif h > 55:
            smtp_alert.send_alert(indicator)
    style = {'padding': '5px', 'fontSize': '24px', 'font-weight' : 'bold',"color":"#ff7700",}
    return [
        html.Span(hum, style=style)
    ]


if __name__ == "__main__":
    app.run_server(debug=True,
                   host = '127.0.0.1')
