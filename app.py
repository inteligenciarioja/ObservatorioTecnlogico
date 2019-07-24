# -*- coding: utf-8 -*-
import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import MySQLdb

dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
df = pd.read_sql("""SELECT Year, PorcaPIB, Region FROM exampledb.IDAnalisis"""
                 ,con = dbconnection)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
lista = df.Region.unique()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Graph(
        id = 'PorInvRiojaPIB',
        figure={
            'data': [
                go.Scatter(
                    x = df[df['Region']==lista[i]]['Year'],
                    y = df[df['Region']==lista[i]]['PorcaPIB'],
                    text = 'PorInvRiojaPIB',
                    name = 'i'
                ) for i in range(0,len(lista))
                
            ],
            'layout': go.Layout(
                xaxis={'title':'Year'},
                yaxis= {'title':'PorcaPib'}
            )
        }
    )
    
])
if __name__ == '__main__':
    app.run_server(debug=True)


#querystring = """SELECT id, Region, Year, PorcaPIB FROM exampledb.IDAnalisis WHERE Year = '""" + str(yearint) + """'"""
#dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
#                              user='exampleuser', passwd='pimylifeup')
#c = dbconnection.cursor()
#c.execute(querystring)
#result = c.fetchall()
#Group = []
#values = []
#for row in result :
#    #print(row)
#    Group.append(str(row [1]))
#    values.append(float(row [3]))
