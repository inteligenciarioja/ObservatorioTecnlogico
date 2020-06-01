#!/usr/bin/env python
# coding: utf-8

# In[1]:


# La Rioja Trimestral
#!pip install pyaxis
#pc-axis-url: https://ias1.larioja.org/jaxiweb/fileDownload.do?filePath=/2/201/20102/l0/20102004.px&contentType=text/plain

from pyaxis import pyaxis
import pandas as pd
url = "https://ias1.larioja.org/jaxiweb/fileDownload.do?filePath=/2/201/20102/l0/20102004.px&contentType=text/plain"
px = pyaxis.parse(uri = url , encoding = 'ISO-8859-2')
data_df = px['DATA']
meta_dict = px['METADATA']


# In[2]:


data_df


# In[3]:


df = data_df[data_df['Tipo de medida']=='PRECIOS CORRIENTES']


# In[4]:


df


# In[5]:


meta_dict


# In[6]:


# En este caso estamos viendo que los indicadores que nos interesan son:
# PRODUCTO INTERIOR BRUTO A PRECIOS DE MERCADO (PIB pm)
# Agricultura, ganadería, silvicultura y pesca (A)
# Industria (B_E)
# - Industria manufacturera (C)
# Construcción (F)
# Servicios (G_T)
# VALOR AŃADIDO BRUTO (VAB)

df_agricultura = df[df['Agrupación de actividad']=='Agricultura, ganadería, silvicultura y pesca (A)']
df_industria = df[df['Agrupación de actividad']=='Industria (B_E)']
df_manufacturera = df[df['Agrupación de actividad']=='- Industria manufacturera (C)']
df_construccion = df[df['Agrupación de actividad']=='Construcción (F)']
df_servicios = df[df['Agrupación de actividad']=='Servicios (G_T)']
df_vabTotal = df[df['Agrupación de actividad']=='VALOR AŃADIDO BRUTO (VAB)']
df_pib = df[df['Agrupación de actividad']=='PRODUCTO INTERIOR BRUTO A PRECIOS DE MERCADO (PIB pm)']


# In[11]:


bbdd = pd.DataFrame(
    {
        'year':df_pib.Periodo.str.split('T ').str[1].values,
        'trimestre':df_pib.Periodo.str.split('T ').str[0].values,
        'region':pd.DataFrame(['La Rioja']*df_pib.shape[0]).values.tolist(), #Poner todo Euskadi
        'PIB':df_pib['DATA'].astype(float).values,
        'VABAgricultura':df_agricultura['DATA'].astype(float).values,
        '%VABAgricultura':(df_agricultura['DATA'].astype(float).values/df_vabTotal['DATA'].astype(float).values)*100,
        'VABIndustria':df_industria['DATA'].astype(float).values,
        '%VABIndustria':(df_industria['DATA'].astype(float).values/df_vabTotal['DATA'].astype(float).values)*100,
        'VABManufacturera':df_manufacturera['DATA'].astype(float).values,
        '%VABManufacturera':(df_manufacturera['DATA'].astype(float).values/df_vabTotal['DATA'].astype(float).values)*100,
        'VABConstruccion':df_construccion['DATA'].astype(float).values,
        '%VABConstruccion':(df_construccion['DATA'].astype(float).values/df_vabTotal['DATA'].astype(float).values)*100,
        'VABServicios':df_servicios['DATA'].astype(float).values,
        '%VABServicios':(df_servicios['DATA'].astype(float).values/df_vabTotal['DATA'].astype(float).values)*100,
        'VABTotal':df_vabTotal['DATA'].astype(float).values,
    }
)


# In[12]:


bbdd


# In[14]:


# Ahora faltaría integrarlo en una BBDD. Igual lo monto en mongodb para que hagan una prueba
# Incicializamos la conexión con mongodb localhost
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client['Contabilidad_trimestral']
collection_region = db['regions']
bbdd.reset_index(inplace=True) 
bbdd_dict = bbdd.to_dict("records") # Convert to dictionary
x = collection_region.insert_many(bbdd_dict)


# In[ ]:




