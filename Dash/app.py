import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Mangos", "Watermelons", "Grapes"],
    "Cost": [4, 1, 2, 2, 4, 50],
})
#Gamestop dataframe
gme_df = pd.read_csv('../Data/gme_data.csv')

#TMDB 5000 movie dataset
m_df = pd.read_csv('../Data/tmdb_5000_movies.csv')

def get_value(row):
    return row[1]
    
# Date 01/01/2000
m_df['Date_dt'] = pd.to_datetime(m_df['release_date'], format='%Y/%m/%d')
# Movies by month
m_df['Month'] = m_df['Date_dt'].dt.month
m_df['Year'] = m_df['Date_dt'].dt.year



gme_df['Date_dt'] = pd.to_datetime(gme_df['Date'], format='%m/%d/%Y')
gme_df['Close_num'] = pd.to_numeric(gme_df['Close/Last'].str.split("$").apply(get_value))

print(m_df['Month'].value_counts(sort=True))
print(m_df['Year'].value_counts(sort=True, ascending=True))
print(m_df['Month'].value_counts(sort=True)[10])

ma_df = pd.DataFrame({
    "Month": ["January", "Feburary", "March", "April", " May", "June", "July", "August", "September", "October", "November", "December"],
    "Frequency": [m_df['Month'].value_counts(sort=True)[1], m_df['Month'].value_counts(sort=True)[2], m_df['Month'].value_counts(sort=True)[3], m_df['Month'].value_counts(sort=True)[4], m_df['Month'].value_counts(sort=True)[5], m_df['Month'].value_counts(sort=True)[6], m_df['Month'].value_counts(sort=True)[7], m_df['Month'].value_counts(sort=True)[8], m_df['Month'].value_counts(sort=True)[9], m_df['Month'].value_counts(sort=True)[10], m_df['Month'].value_counts(sort=True)[11], m_df['Month'].value_counts(sort=True)[12]]
                     })

# Create Bar graph
fig = px.bar(df, x='Fruit',y='Cost')

fig2 = px.line(gme_df, x='Date_dt', y='Close_num', labels={'Date_dt': 'Date', 'Close_num': "Closing Cost ($)"})

fig3 = px.line(gme_df, x = 'Date', y='Close_num')

movie_fig = px.bar(ma_df, x='Month', y= 'Frequency', color= 'Month', color_discrete_sequence=px.colors.qualitative.Set3,   title="Movie Releases by Month")

''' ***** Layout ****** '''
app.layout = html.Div(children = [
    html.H1(children='Hello World'),
    html.Div(children = 'Dash is cool!'),
    dcc.Graph(id = 'Fruit Cost', figure = fig),
    dcc.Graph(id = 'GME 5 year Data Close', figure = fig2),
    dcc.Graph(id= '5000 Movies', figure = movie_fig),
    dcc.Graph(id= 'GME 5 year no DT', figure = fig3)
    
])

if __name__ == '__main__':
    app.run_server(debug=True)
