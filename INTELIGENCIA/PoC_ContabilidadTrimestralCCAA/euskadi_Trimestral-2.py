#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install pyaxis


# In[36]:


from pyaxis import pyaxis
import pandas as pd
url = "https://www.eustat.eus/bankupx/Resources/PX/Databases/spanish/PX_3422_cet01tb.px"
px = pyaxis.parse(uri = url , encoding = 'ISO-8859-2')
data_df = px['DATA']
meta_dict = px['METADATA']


# In[3]:


data_df


# In[4]:


meta_dict


# In[5]:


data_df['periodo']


# In[17]:


df = data_df[(data_df['tipo de dato']=='Nivel') & (data_df['tipo de serie']=='Datos brutos') & (data_df['tipo de medida']=='Precios corrientes (miles euros)')]


# In[18]:


df


# In[28]:


# En este caso estamos viendo que los indicadores que nos interesan son:
# AGRICULTURA, GANADERÍA Y PESCA
# INDUSTRIA Y ENERGÍA
# -Industria manufacturera
# CONSTRUCCIÓN
# SERVICIOS
# VAB TOTAL (miles €)

df_agricultura = df[df.componente=='AGRICULTURA, GANADERÍA Y PESCA']
df_industria = df[df.componente=='INDUSTRIA Y ENERGÍA']
df_manufacturera = df[df.componente=='-Industria manufacturera']
df_construccion = df[df.componente=='CONSTRUCCIÓN']
df_servicios = df[df.componente=='SERVICIOS']
df_vabTotal = df[df.componente=='VALOR AŃADIDO BRUTO a precios básicos']
df_pib = df[df.componente=='PRODUCTO INTERIOR BRUTO a precios de mercado']


# In[20]:


df_agricultura


# In[22]:


df_industria


# In[23]:


df_manufacturera


# In[24]:


df_construccion


# In[25]:


df_servicios


# In[26]:


df_vabTotal


# In[29]:


df_pib


# In[82]:


#df_agricultura = df[df.componente=='AGRICULTURA, GANADERÍA Y PESCA']
#df_industria = df[df.componente=='INDUSTRIA Y ENERGÍA']
#df_manufacturera = df[df.componente=='-Industria manufacturera']
#df_construccion = df[df.componente=='CONSTRUCCIÓN']
#df_servicios = df[df.componente=='SERVICIOS']
#df_vabTotal = df[df.componente=='VALOR AŃADIDO BRUTO a precios básicos']
#df_pib = df[df.componente=='PRODUCTO INTERIOR BRUTO a precios de mercado']


bbdd = pd.DataFrame(
    {
        'year':df_pib.periodo.str.split('-').str[0].values,
        'trimestre':df_pib.periodo.str.split('-').str[1].values,
        'region':pd.DataFrame(['Euskadi']*df_pib.shape[0]).values.tolist(), #Poner todo Euskadi
        'PIB':df_pib['DATA'].astype(float).astype(float).values,
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


# In[83]:


bbdd


# In[84]:


# Una vez montadas las rows faltaría introducirlas en una BBDD MySQL o MongodB
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




