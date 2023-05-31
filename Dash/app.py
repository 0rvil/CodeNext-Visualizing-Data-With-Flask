import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Mangos", "Watermelons", "Grapes"],
    "Cost": [4, 1, 25, 2, 4, 50],
})
#Gamestop dataframe
gme_df = pd.read_csv('../Data/gme_data.csv')

def get_value(row):
    return row[1]

gme_df['Date_dt'] = pd.to_datetime(gme_df['Date'], format='%m/%d/%Y')
gme_df['Close_num'] = pd.to_numeric(gme_df['Close/Last'].str.split("$").apply(get_value))

# Create Bar graph
fig = px.bar(df, x='Fruit',y='Cost')

fig2 = px.line(gme_df, x='Date_dt', y='Close_num', labels={'Date_dt': 'Date', 'Close_num': "Closing Cost ($)"})

fig3 = px.line(gme_df, x = 'Date', y='Close_num')

''' ***** Layout ****** '''
app.layout = html.Div(children = [
    #Navigation Bar linking to the three graphs
    html.Header(
        html.Nav(
            html.Ul(
                html.Li(children=[
                html.A("Fruit Cost", href="#Fruit Cost"),
                html.A("GME 5 YR", href="#GME 5 year Data Close"),
                html.A("GME No Datastamps", href="#GME 5 year no DT") ])
            )
        )
    ),
    html.H1(children='Hello World', className="title"),
    html.Div(children = 'Dash is cool!', className="title"),
    dcc.Graph(id = 'Fruit Cost', figure = fig),
    dcc.Graph(id = 'GME 5 year Data Close', figure = fig2),
    dcc.Graph(id= 'GME 5 year no DT', figure = fig3)
    
])

if __name__ == '__main__':
    app.run_server(debug=True)
