# -*- coding: utf-8 -*-
import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import MySQLdb
from numpy import array

def extractinfo(region1_name) :
        dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
        countregionNAC = []
        countregionEUR = []
        countregionPCT = []
        if (region1_name != 'Nacional') :
            querystringNAC = ("""SELECT NPublicadas, Year FROM exampledb.SOLNAC WHERE CCAA =  '"""+region1_name+"""';""")
            querystringEUR = ("""SELECT NPublicadas, Year FROM exampledb.SOLOEPM WHERE CCAA =  '"""+region1_name+"""';""")
            querystringPCT = ("""SELECT NPublicadas, Year FROM exampledb.SOLPCT WHERE CCAA =  '"""+region1_name+"""';""")
            dfNAC = pd.read_sql(querystringNAC,con = dbconnection)
            dfNAC.NPublicadas[dfNAC.NPublicadas == 'nan'] = '0.0'
            dfNAC.NPublicadas = dfNAC.NPublicadas.astype(float)
            listayear = df.Year.unique()
            for year in listayear :
                countregionNAC.append(dfNAC[dfNAC["Year"] == year]['NPublicadas'].sum()) 
            dfEUR = pd.read_sql(querystringEUR,con = dbconnection)
            dfEUR.NPublicadas[dfEUR.NPublicadas == 'nan'] = '0.0'
            dfEUR.NPublicadas = dfEUR.NPublicadas.astype(float)
            for year in listayear :
                countregionEUR.append(dfEUR[dfEUR["Year"] == year]['NPublicadas'].sum())
            dfPCT = pd.read_sql(querystringPCT,con = dbconnection)
            dfPCT.NPublicadas[dfPCT.NPublicadas == 'nan'] = '0.0'
            dfPCT.NPublicadas = dfPCT.NPublicadas.astype(float)
            for year in listayear :
                countregionPCT.append(dfPCT[dfPCT["Year"] == year]['NPublicadas'].sum())
            df1 = array(countregionNAC)
            df2 = array(countregionEUR)
            df3 = array(countregionPCT)
            #print(df1)
            #print(df2)
            #print(df3)
            dffinal1 = df1 + df2 + df3
        else :
            querystringNAC = ("""SELECT NPublicadas, Year FROM exampledb.SOLNAC WHERE CCAA = 'nan'""")
            querystringEUR = ("""SELECT NPublicadas, Year FROM exampledb.SOLOEPM WHERE CCAA = 'nan'""")
            querystringPCT = ("""SELECT NPublicadas, Year FROM exampledb.SOLPCT WHERE CCAA = 'nan'""")
            dfNAC = pd.read_sql(querystringNAC,con = dbconnection)
            dfNAC.NPublicadas[dfNAC.NPublicadas == 'nan'] = '0.0'
            for i in range (0,len(dfNAC.NPublicadas)) :
                if (dfNAC.NPublicadas[i].find('.') == 1) :
                    dfNAC.NPublicadas [i] = round(float(dfNAC.NPublicadas[i])*1000)
            dfNAC.NPublicadas = dfNAC.NPublicadas.astype(float)
            listayear = df.Year.unique()
            for year in listayear :
                countregionNAC.append(dfNAC[dfNAC["Year"] == year]['NPublicadas'].sum())
            print("CounterRegionNAC")
            print(countregionNAC)
            dfEUR = pd.read_sql(querystringEUR,con = dbconnection)
            dfEUR.NPublicadas[dfEUR.NPublicadas == 'nan'] = '0.0'
            for i in range (0,len(dfEUR.NPublicadas)) :
                if (dfEUR.NPublicadas[i].find('.') == 1) :
                    dfEUR.NPublicadas[i] = round(float(dfEUR.NPublicadas[i])*1000)
            dfEUR.NPublicadas = dfEUR.NPublicadas.astype(float)
            #print(dfEUR.NPublicadas)
            for year in listayear :
                countregionEUR.append(dfEUR[dfEUR["Year"] == year]['NPublicadas'].sum())
            print("CounterRegionEUR")
            print(countregionEUR)
            dfPCT = pd.read_sql(querystringPCT,con = dbconnection)
            dfPCT.NPublicadas[dfPCT.NPublicadas == 'nan'] = '0.0'
            for i in range (0,len(dfPCT.NPublicadas)) :
                if (dfPCT.NPublicadas[i].find('.') == 1) :
                    dfPCT.NPublicadas[i] = round(float(dfPCT.NPublicadas[i])*1000)
            dfPCT.NPublicadas = dfPCT.NPublicadas.astype(float)
            for year in listayear :
                countregionPCT.append(dfPCT[dfPCT["Year"] == year]['NPublicadas'].sum())
            print("CounterRegionPCT")
            print(countregionPCT)
            df1 = array(countregionNAC)
            df2 = array(countregionEUR)
            df3 = array(countregionPCT)
            #print(df1)
            #print(df2)
            #print(df3)
            dffinal1 = df1 + df2 + df3
        dbconnection.close()
        return dffinal1

def extractinfo2(region1_name) :
        dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
        countregionNAC = []
        countregionEUR = []
        countregionPCT = []
        if (region1_name != 'Nacional') :
            querystringNAC = ("""SELECT NPublicadas, Year FROM exampledb.SOLNAC WHERE CCAA =  '"""+region1_name+"""';""")
            #querystringEUR = ("""SELECT NPublicadas, Year FROM exampledb.SOLOEPM WHERE CCAA =  '"""+region1_name+"""';""")
            #querystringPCT = ("""SELECT NPublicadas, Year FROM exampledb.SOLPCT WHERE CCAA =  '"""+region1_name+"""';""")
            dfNAC = pd.read_sql(querystringNAC,con = dbconnection)
            dfNAC.NPublicadas[dfNAC.NPublicadas == 'nan'] = '0.0'
            dfNAC.NPublicadas = dfNAC.NPublicadas.astype(float)
            listayear = df.Year.unique()
            for year in listayear :
                countregionNAC.append(dfNAC[dfNAC["Year"] == year]['NPublicadas'].sum()) 
            df1 = array(countregionNAC)
            dffinal1 = df1
        else :
            querystringNAC = ("""SELECT NPublicadas, Year FROM exampledb.SOLNAC WHERE CCAA = 'nan'""")
            #querystringEUR = ("""SELECT NPublicadas, Year FROM exampledb.SOLOEPM WHERE CCAA = 'nan'""")
            #querystringPCT = ("""SELECT NPublicadas, Year FROM exampledb.SOLPCT WHERE CCAA = 'nan'""")
            dfNAC = pd.read_sql(querystringNAC,con = dbconnection)
            dfNAC.NPublicadas[dfNAC.NPublicadas == 'nan'] = '0.0'
            for i in range (0,len(dfNAC.NPublicadas)) :
                if (dfNAC.NPublicadas[i].find('.') == 1) :
                    dfNAC.NPublicadas [i] = round(float(dfNAC.NPublicadas[i])*1000)
            dfNAC.NPublicadas = dfNAC.NPublicadas.astype(float)
            listayear = df.Year.unique()
            for year in listayear :
                countregionNAC.append(dfNAC[dfNAC["Year"] == year]['NPublicadas'].sum())
            df1 = array(countregionNAC)
            dffinal1 = df1
        dbconnection.close()
        return dffinal1

def extractinfo3(region1_name) :
        dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
        countregionNAC = []
        countregionEUR = []
        countregionPCT = []
        if (region1_name != 'Nacional') :
            #querystringNAC = ("""SELECT NPublicadas, Year FROM exampledb.SOLNAC WHERE CCAA =  '"""+region1_name+"""';""")
            querystringEUR = ("""SELECT NPublicadas, Year FROM exampledb.SOLOEPM WHERE CCAA =  '"""+region1_name+"""';""")
            #querystringPCT = ("""SELECT NPublicadas, Year FROM exampledb.SOLPCT WHERE CCAA =  '"""+region1_name+"""';""")
            listayear = df.Year.unique()
            dfEUR = pd.read_sql(querystringEUR,con = dbconnection)
            dfEUR.NPublicadas[dfEUR.NPublicadas == 'nan'] = '0.0'
            dfEUR.NPublicadas = dfEUR.NPublicadas.astype(float)
            for year in listayear :
                countregionEUR.append(dfEUR[dfEUR["Year"] == year]['NPublicadas'].sum())
            
            #df1 = array(countregionNAC)
            df2 = array(countregionEUR)
            #df3 = array(countregionPCT)

            dffinal1 = df2
        else :
            #querystringNAC = ("""SELECT NPublicadas, Year FROM exampledb.SOLNAC WHERE CCAA = 'nan'""")
            querystringEUR = ("""SELECT NPublicadas, Year FROM exampledb.SOLOEPM WHERE CCAA = 'nan'""")
            #querystringPCT = ("""SELECT NPublicadas, Year FROM exampledb.SOLPCT WHERE CCAA = 'nan'""")
            
            listayear = df.Year.unique()
            dfEUR = pd.read_sql(querystringEUR,con = dbconnection)
            dfEUR.NPublicadas[dfEUR.NPublicadas == 'nan'] = '0.0'
            for i in range (0,len(dfEUR.NPublicadas)) :
                if (dfEUR.NPublicadas[i].find('.') == 1) :
                    dfEUR.NPublicadas[i] = round(float(dfEUR.NPublicadas[i])*1000)
            dfEUR.NPublicadas = dfEUR.NPublicadas.astype(float)
            
            for year in listayear :
                countregionEUR.append(dfEUR[dfEUR["Year"] == year]['NPublicadas'].sum())
            
            #df1 = array(countregionNAC)
            df2 = array(countregionEUR)
            #df3 = array(countregionPCT)
            #print(df1)
            #print(df2)
            #print(df3)
            dffinal1 = df2
        dbconnection.close()
        return dffinal1

def extractinfo4(region1_name) :
        dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
        countregionNAC = []
        countregionEUR = []
        countregionPCT = []
        if (region1_name != 'Nacional') :
            #querystringNAC = ("""SELECT NPublicadas, Year FROM exampledb.SOLNAC WHERE CCAA =  '"""+region1_name+"""';""")
            #querystringEUR = ("""SELECT NPublicadas, Year FROM exampledb.SOLOEPM WHERE CCAA =  '"""+region1_name+"""';""")
            querystringPCT = ("""SELECT NPublicadas, Year FROM exampledb.SOLPCT WHERE CCAA =  '"""+region1_name+"""';""")
            
            listayear = df.Year.unique()
            
            dfPCT = pd.read_sql(querystringPCT,con = dbconnection)
            dfPCT.NPublicadas[dfPCT.NPublicadas == 'nan'] = '0.0'
            dfPCT.NPublicadas = dfPCT.NPublicadas.astype(float)
            for year in listayear :
                countregionPCT.append(dfPCT[dfPCT["Year"] == year]['NPublicadas'].sum())
            
            df3 = array(countregionPCT)
            
            dffinal1 = df3
        else :
            
            querystringPCT = ("""SELECT NPublicadas, Year FROM exampledb.SOLPCT WHERE CCAA = 'nan'""")
            
            listayear = df.Year.unique()
            
            dfPCT = pd.read_sql(querystringPCT,con = dbconnection)
            dfPCT.NPublicadas[dfPCT.NPublicadas == 'nan'] = '0.0'
            for i in range (0,len(dfPCT.NPublicadas)) :
                if (dfPCT.NPublicadas[i].find('.') == 1) :
                    dfPCT.NPublicadas[i] = round(float(dfPCT.NPublicadas[i])*1000)
            dfPCT.NPublicadas = dfPCT.NPublicadas.astype(float)
            for year in listayear :
                countregionPCT.append(dfPCT[dfPCT["Year"] == year]['NPublicadas'].sum())
            
            df3 = array(countregionPCT)
            #print(df1)
            #print(df2)
            #print(df3)
            dffinal1 =  df3
        dbconnection.close()
        return dffinal1


def extractinfo5(region1_pie, year_pie)  :
    dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
    countregionNAC = []
    countregionEUR = []
    countregionPCT = []
    if (region1_pie != 'Nacional') :
        querystringNAC = ("""SELECT TipoSolicitante, NPublicadas, Year FROM exampledb.SOLNAC """
                              """WHERE CCAA='"""+region1_pie+"""'AND Year = '""" + year_pie+"""'ORDER BY TipoSolicitante;""")
        querystringEUR = ("""SELECT TipoSolicitante, NPublicadas, Year FROM exampledb.SOLOEPM """
                              """WHERE CCAA='"""+region1_pie+"""'AND Year = '""" + year_pie+"""'ORDER BY TipoSolicitante;""")
        querystringPCT = ("""SELECT TipoSolicitante, NPublicadas, Year FROM exampledb.SOLPCT """
                              """WHERE CCAA='"""+region1_pie+"""'AND Year = '""" + year_pie+"""'ORDER BY TipoSolicitante;""")
        dfNAC = pd.read_sql(querystringNAC,con = dbconnection)
        dfNAC.NPublicadas[dfNAC.NPublicadas == 'nan'] = '0.0'
        dfNAC.NPublicadas = dfNAC.NPublicadas.astype(float)
        listasol = dfNAC.TipoSolicitante.unique()
        for sol in listasol :
            countregionNAC.append(dfNAC[dfNAC["TipoSolicitante"] == sol].NPublicadas.item()) 
        dfEUR = pd.read_sql(querystringEUR,con = dbconnection)
        dfEUR.NPublicadas[dfEUR.NPublicadas == 'nan'] = '0.0'
        dfEUR.NPublicadas = dfEUR.NPublicadas.astype(float)
        for sol in listasol :
            countregionEUR.append(dfEUR[dfEUR["TipoSolicitante"] == sol].NPublicadas.item())
        dfPCT = pd.read_sql(querystringPCT,con = dbconnection)
        dfPCT.NPublicadas[dfPCT.NPublicadas == 'nan'] = '0.0'
        dfPCT.NPublicadas = dfPCT.NPublicadas.astype(float)
        for sol in listasol :
            countregionPCT.append(dfPCT[dfPCT["TipoSolicitante"] == sol].NPublicadas.item())
        #print(countregionNAC)
        print("Revision")
        print(countregionPCT)
        df1 = array(countregionNAC)
        df2 = array(countregionEUR)
        df3 = array(countregionPCT)
            #print(df1)
            #print(df2)
            #print(df3)
        values = df1 + df2 + df3
        labels = dfNAC.TipoSolicitante.unique()
        values.astype(float)
        total = float(values.sum())
        for i in range (0,len(values)) :
            values[i] = (values[i]/total)*100
    dbconnection.close()
    return [labels, values]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
df = pd.read_sql("""SELECT CCAA, Year FROM exampledb.SOLNAC"""
                 ,con = dbconnection)
listaf = df.CCAA.unique()
listapie = listaf.tolist()
lista = listaf.tolist()
lista.append('Nacional')
listayear = df.Year.unique()

app.layout = html.Div([

    html.Div([

        html.Div([
            dcc.Dropdown(
                id='region1',
                options = [{'label': i, 'value':i} for i in lista],
                value = 'Nacional'
            )

        ]),
        html.Div([
            dcc.Dropdown(
                id='region2',
                options = [{'label': i, 'value':i} for i in lista],
                value = 'Nacional'
            )

        ])
        

    ]),
    dcc.Graph(id = 'graphic'),
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='region1_nac',
                options = [{'label': i, 'value':i} for i in lista],
                value = 'Nacional'
            )

        ]),
        html.Div([
            dcc.Dropdown(
                id='region2_nac',
                options = [{'label': i, 'value':i} for i in lista],
                value = 'Nacional'
            )

        ])
        

    ]),
    dcc.Graph(id = 'graphic2'),
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='region1_eur',
                options = [{'label': i, 'value':i} for i in lista],
                value = 'Nacional'
            )

        ]),
        html.Div([
            dcc.Dropdown(
                id='region2_eur',
                options = [{'label': i, 'value':i} for i in lista],
                value = 'Nacional'
            )

        ])
        

    ]),
    dcc.Graph(id = 'graphic3'),
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='region1_pct',
                options = [{'label': i, 'value':i} for i in lista],
                value = 'Nacional'
            )

        ]),
        html.Div([
            dcc.Dropdown(
                id='region2_pct',
                options = [{'label': i, 'value':i} for i in lista],
                value = 'Nacional'
            )

        ])
        

    ]),
    dcc.Graph(id = 'graphic4'),
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='region1_pie',
                options = [{'label': i, 'value':i} for i in listapie],
                value = 'ANDALUCIA'
            )

        ]),
        html.Div([
            dcc.Dropdown(
                id='year_pie',
                options = [{'label': i, 'value':i} for i in listayear],
                value = '2017.0'
            )

        ])
        

    ]),
    dcc.Graph(id = 'graphic5')
])


@app.callback(
    Output('graphic','figure'),
    [Input('region1','value'),
     Input('region2','value')])
def update_graph(region1_name, region2_name) :
    
    dffinal1 = extractinfo(region1_name)
    dffinal2 = extractinfo(region2_name)
    x = listayear
    print(dffinal1)
    print(dffinal2)
    print(x)
    trace1 = go.Scatter(x = x, y = dffinal1, name = region1_name)
    trace2 = go.Scatter(x = x, y = dffinal2, name = region2_name) 
    return{
        'data': [trace1, trace2],
        'layout': go.Layout(
                title = 'Solicitudes de Patentes Nacionales, Europeas y PCT',
                xaxis={'title':'Year'},
                yaxis= {'title':'NPat'}
        )
        
    }

@app.callback(
    Output('graphic2','figure'),
    [Input('region1_nac','value'),
     Input('region2_nac','value')])
def update_graph2(region1_name, region2_name) :
    
    dffinal1 = extractinfo2(region1_name)
    dffinal2 = extractinfo2(region2_name)
    x = listayear
    print(dffinal1)
    print(dffinal2)
    print(x)
    trace1 = go.Scatter(x = x, y = dffinal1, name = region1_name)
    trace2 = go.Scatter(x = x, y = dffinal2, name = region2_name) 
    return{
        'data': [trace1, trace2],
        'layout': go.Layout(
                title = 'Solicitudes de Patentes Nacionales',
                xaxis={'title':'Year'},
                yaxis= {'title':'NPat'}
        )
        
    }

@app.callback(
    Output('graphic3','figure'),
    [Input('region1_eur','value'),
     Input('region2_eur','value')])
def update_graph3(region1_name, region2_name) :
    
    dffinal1 = extractinfo3(region1_name)
    dffinal2 = extractinfo3(region2_name)
    x = listayear
    print(dffinal1)
    print(dffinal2)
    print(x)
    trace1 = go.Scatter(x = x, y = dffinal1, name = region1_name)
    trace2 = go.Scatter(x = x, y = dffinal2, name = region2_name) 
    return{
        'data': [trace1, trace2],
        'layout': go.Layout(
                title = 'Solicitudes de Patentes Europeas',
                xaxis={'title':'Year'},
                yaxis= {'title':'NPat'}
        )
        
    }

@app.callback(
    Output('graphic4','figure'),
    [Input('region1_pct','value'),
     Input('region2_pct','value')])
def update_graph4(region1_name, region2_name) :
    
    dffinal1 = extractinfo4(region1_name)
    dffinal2 = extractinfo4(region2_name)
    x = listayear
    print(dffinal1)
    print(dffinal2)
    print(x)
    trace1 = go.Scatter(x = x, y = dffinal1, name = region1_name)
    trace2 = go.Scatter(x = x, y = dffinal2, name = region2_name) 
    return{
        'data': [trace1, trace2],
        'layout': go.Layout(
                title = 'Solicitudes de Patentes PCT',
                xaxis={'title':'Year'},
                yaxis= {'title':'NPat'}
        )
        
    }
@app.callback(
    Output('graphic5','figure'),
    [Input('region1_pie','value'),
     Input('year_pie','value')])
def update_graph5(region1_pie, year_pie) :
    dffinal1 = extractinfo5(region1_pie, year_pie)
    print('@marcos')
    print(dffinal1[0])
    print(dffinal1[1])
    values = dffinal1[1]
    trace1 = go.Pie(labels = dffinal1[0], values = values)

    return{
        'data': [trace1],
        'layout': go.Layout(
                #title = 'Solicitudes de Patentes PCT',
                #xaxis={'title':'Year'},
                #yaxis= {'title':'NPat'}
        )
        
    }

if __name__ == '__main__':
    app.run_server(debug=False, port = 8051)



