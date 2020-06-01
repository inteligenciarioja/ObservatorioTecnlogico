#!/usr/bin/env python
# coding: utf-8

# In[58]:


# Nacional Trimestral
# Url pcaxis base: https://www.ine.es/jaxiT3/files/t/es/px/30678.px?nocab=1

from pyaxis import pyaxis
from pymongo import MongoClient
import pandas as pd
url = "https://www.ine.es/jaxiT3/files/t/es/px/30678.px?nocab=1"
px = pyaxis.parse(uri = url , encoding = 'ISO-8859-2')
data_df = px['DATA']
meta_dict = px['METADATA']


#meta_dict


# In[3]:


#data_df


# In[6]:


df = data_df[(data_df['Tipo de dato']=='Datos ajustados de estacionalidad y calendario')& (data_df['Niveles y tasas']=='Dato base')]
df


# In[53]:


# En este caso estamos viendo que los indicadores que nos interesan son:
# Producto interior bruto a precios de mercado
# VABpb Agricultura, ganadería, silvicultura y pesca (A, CNAE 2009)
# VABpb Industria (B-E, CNAE 2009)
# VABpb Industria. Industria manufacturera (C, CNAE 2009)
# VABpb Construcción (F, CNAE 2009)
# VABpb Servicios (G-T, CNAE 2009)
# VALOR AŃADIDO BRUTO (VAB)

df_agricultura = df[df['Agregados macroeconómicos']=='VABpb Agricultura, ganadería, silvicultura y pesca (A, CNAE 2009)']
df_industria = df[df['Agregados macroeconómicos']=='VABpb Industria (B-E, CNAE 2009)']
df_manufacturera = df[df['Agregados macroeconómicos']=='VABpb Industria. Industria manufacturera (C, CNAE 2009)']
df_construccion = df[df['Agregados macroeconómicos']=='VABpb Construcción (F, CNAE 2009)']
df_servicios = df[df['Agregados macroeconómicos']=='VABpb Servicios (G-T, CNAE 2009)']
df_vabTotal = df_agricultura['DATA'].astype(float).values + df_industria['DATA'].astype(float).values + df_construccion['DATA'].astype(float).values +df_servicios['DATA'].astype(float).values 
df_pib = df[df['Agregados macroeconómicos']=='Producto interior bruto a precios de mercado']


# In[78]:


# Los valores se dan en millones de euros y el resto de regiones lo da en miles
bbdd = pd.DataFrame(
    {
        'year':df_pib.Periodo.str.split('T').str[0].values,
        'trimestre':df_pib.Periodo.str.split('T').str[1].values,
        'region':pd.DataFrame(['España']*df_pib.shape[0]).values.tolist(), #Poner todo Euskadi
        'PIB':df_pib['DATA'].astype(float).values*1000,
        'VABAgricultura':df_agricultura['DATA'].astype(float).values*1000,
        '%VABAgricultura':(df_agricultura['DATA'].astype(float).values/df_vabTotal)*100,
        'VABIndustria':df_industria['DATA'].astype(float).values*1000,
        '%VABIndustria':(df_industria['DATA'].astype(float).values/df_vabTotal)*100,
        'VABManufacturera':df_manufacturera['DATA'].astype(float).values*1000,
        '%VABManufacturera':(df_manufacturera['DATA'].astype(float).values/df_vabTotal)*100,
        'VABConstruccion':df_construccion['DATA'].astype(float).values*1000,
        '%VABConstruccion':(df_construccion['DATA'].astype(float).values/df_vabTotal)*100,
        'VABServicios':df_servicios['DATA'].astype(float).values*1000,
        '%VABServicios':(df_servicios['DATA'].astype(float).values/df_vabTotal)*100,
        'VABTotal':df_vabTotal*1000,
    }
)


# In[79]:


bbdd


# In[23]:


# Ahora habría que integrarlo en un BBDD - Voy a hacerlo con mongo que te deja desacargarlo luego en csv y si quiero modifico node.js para completar la API


# In[80]:


# Incicializamos la conexión con mongodb localhost
client = MongoClient('localhost',27017)
db = client['Contabilidad_trimestral']
collection_region = db['regions']
bbdd.reset_index(inplace=True) 
bbdd_dict = bbdd.to_dict("records") # Convert to dictionary
x = collection_region.insert_many(bbdd_dict)


# In[ ]:




