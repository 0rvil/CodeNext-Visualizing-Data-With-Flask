import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

def get_value(row):
    return row[1]

def init_dashboard(server):
    dash_app = dash.Dash(server= server, url_base_pathname="/dashapp/")

    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Mangos", "Watermelons", "Grapes"],
        "Cost": [4, 1, 2, 2, 4, 50],
    })

    gme_df = pd.read_csv('../Data/gme_data.csv')

    gme_df['Date_dt'] = pd.to_datetime(gme_df['Date'], format='%m/%d/%Y')
    gme_df['Close_num'] = pd.to_numeric(gme_df['Close/Last'].str.split("$").apply(get_value))



    fig = px.bar(df, x='Fruit',y='Cost')

    fig2 = px.line(gme_df, x='Date_dt', y='Close_num', labels={'Date_dt': 'Date', 'Close_num': "Closing Cost ($)"})

    dash_app.layout = html.Div(children = [html.H1(children='Hello World'),
    dcc.Graph(id = 'Fruit Cost', figure = fig),
    dcc.Graph(id = 'GME 5 year Data Close', figure = fig2),])

    return dash_app.server
