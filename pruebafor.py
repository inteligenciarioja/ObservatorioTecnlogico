# -*- coding: utf-8 -*-
import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import MySQLdb


dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
df = pd.read_sql("""SELECT Year, PorcaPIB, Region FROM exampledb.IDAnalisis"""
                 ,con = dbconnection)
dpie = pd.read_sql("""SELECT Year, Region, GastoIDTotalMilesEuros, GastoIDADPubMilesEuros, GastoIDEnsSupMilesEuros,
GastoIDEmpmilesEuros, GastoIDIPSFLMilesEuros FROM exampledb.IDAnalisis""",
                   con = dbconnection)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
lista = df.Region.unique()
listayear = dpie.Year.unique()


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
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

        ]),

    ]),
    dcc.Graph(id = 'graphic'),
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='Year__',
                options = [{'label': i, 'value':i} for i in listayear],
                value = '2017'
            )

        ]),
        html.Div([
            dcc.Dropdown(
                id='Region__',
                options = [{'label': i, 'value':i} for i in lista],
                value = 'Nacional'
            )

        ]),

    ]),
    dcc.Graph(id = 'pie'),
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='Year__barchart',
                options = [{'label': i, 'value':i} for i in listayear],
                value = '2017'
            )

        ])        

    ]),
    dcc.Graph(id='barchart')
        #id = 'PorInvRiojaPIB',
        #figure={
            #'data': [
                #go.Scatter(
                    #x = df[df['Region']==lista[i]]['Year'],
                    #y = df[df['Region']==lista[i]]['PorcaPIB'],
                    #text = 'PorInvPIB',
                    #name = lista[i]
                #) for i in range(0,len(lista))
                
            #],
            #'layout': go.Layout(
                #xaxis={'title':'Year'},
                #yaxis= {'title':'PorcaPib'}
            #)
        #}
    #)
    
])

@app.callback(
    Output('graphic','figure'),
    [Input('region1','value'),
     Input('region2','value')])
def update_graph(region1_name, region2_name) :
    lista2 = (region1_name, region2_name)
    return{
        'data': [
                go.Scatter(
                    x = df[df['Region']==lista2[i]]['Year'],
                    y = df[df['Region']==lista2[i]]['PorcaPIB'],
                    text = 'PorInvPIB',
                    name = lista2[i]
                ) for i in range(0,len(lista2))
                
            ],
            'layout': go.Layout(
                #xaxis={'title':'Year'},
                #yaxis= {'title':'PorcaPib'}
            )
        
    }

@app.callback(
    Output('pie','figure'),
    [Input('Year__','value'),
     Input('Region__','value')])
def update_piegrahp(Year__name, Region__name) :
    
    labels = ('Administracion Publica', 'Enseñanza Superior','Empresas','IPSFL')
    Total = dpie[(dpie['Region']== Region__name) & (dpie['Year'] == Year__name)]['GastoIDTotalMilesEuros']
    Totali = float(Total)
    Adpub = dpie[(dpie['Region']== Region__name) & (dpie['Year'] == Year__name)]['GastoIDADPubMilesEuros']
    Adpubi = float(Adpub)
    AdpubPor = (Adpubi*100)/Totali
    Enspub = dpie[(dpie['Region']== Region__name) & (dpie['Year'] == Year__name)]['GastoIDEnsSupMilesEuros']
    Enspubi = float(Enspub)
    EnspubPor = (Enspubi*100)/Totali
    Emp = dpie[(dpie['Region']== Region__name) & (dpie['Year'] == Year__name)]['GastoIDEmpmilesEuros']
    Empi = float(Emp)
    EnpiPor = (Empi*100)/Totali
    IPSFL = dpie[(dpie['Region']== Region__name) & (dpie['Year'] == Year__name)]['GastoIDIPSFLMilesEuros']
    IPSFLi = float(IPSFL)
    IPSFLPor = (IPSFLi*100)/Totali
    values = (AdpubPor,EnspubPor,EnpiPor,IPSFLPor)
    return{
         'data': [
             go.Pie(labels=labels, values = values)
        ],
        'layout': go.Layout()
        
    }
    
@app.callback(
    Output('barchart','figure'),
    [Input('Year__barchart','value')]
)
def update_bargraph(Year_barchart__) :


    yint = int(Year_barchart__) - 1
    ystr= str(yint)
    querystring = """SELECT id, Region, Year, PorcaPIB FROM exampledb.IDAnalisis WHERE Year = '""" + Year_barchart__ + """' OR Year = '"""+ ystr + """'"""
    #querystringyearmenosuno = """SELECT id, Region, Year, PorcaPIB FROM exampledb.IDAnalisis
    #WHERE Year = '"""
    #+ str(int(Year_barchart)__-1) + """'"""
    dfyear = pd.read_sql(querystring,con = dbconnection)
    #dfyearm = pd.read_sql(querystringyearmenosuno,con = dbconnection)
    xuni = dfyear.Region.unique()
    yuni = []
    print(xuni)
    for i in range(0,len(xuni)) :
            dato = dfyear[(dfyear['Year'] == Year_barchart__) & (dfyear['Region'] == xuni[i])]['PorcaPIB']
            yuni.append(float(dato))
    print(yuni)
    trace1 = go.Bar(x=xuni,y=yuni,name=Year_barchart__)
    yuni2=[]
    for i in range(0,len(xuni)) :
            dato = dfyear[(dfyear['Year'] == ystr) & (dfyear['Region'] == xuni[i])]['PorcaPIB']
            yuni2.append(float(dato))
    print(yuni2)
    trace2 = go.Bar(x=xuni,y=yuni2,name=ystr)
    
    return {
        'data': [trace2,trace1],
        'layout': go.Layout(barmode='group')
        
    }
    



    
if __name__ == '__main__':
    app.run_server(debug=False)


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
