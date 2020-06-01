#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
df=pd.read_excel('https://administracionelectronica.navarra.es/GN.InstitutoEstadistica.Web/DescargaFichero.aspx?Fichero=%5C%5Cweb%5C%5Cagregados%5C%5C4_cuentas_economicas%5C%5C42_cuentas_trimestral%5C%5Ccuentas_trimestral_cuadro_macroec_corrientes.xls', sheet_name='1.1', skiprows=2, skipfooter=1)


# In[84]:


df
#df['VAB pb AGRICULTURA'].astype(float).values


# In[85]:


#En este caso estamos viendo que los indicadores que nos interesan son:
# VAB pb AGRICULTURA
# VAB pb INDUSTRIA
# -Industria manufacturera 
# VAB pb CONSTRUCCIÓN
# VAB pb SERVICIOS
# VAB TOTAL (miles €)

df_agricultura = df['VAB pb AGRICULTURA'].astype(float).values
df_industria = df['VAB pb INDUSTRIA'].astype(float).values
#df_manufacturera = df[df.componente=='-Industria manufacturera']
df_construccion = df['VAB pb CONSTRUCCIÓN'].astype(float).values
df_servicios = df['VAB pb SERVICIOS'].astype(float).values
df_vabTotal = (df_agricultura + df_industria + df_construccion + df_servicios).astype(float)
df_pib = df['PIB pm'].astype(float).values


# In[86]:


df_vabTotal


# In[87]:


# Me falta poner el valor de los valores de los trimestres y de los años

#Años
year = df['Unnamed: 0'][0:df.shape[0]:4].repeat(4)

# Trimestre
t1 = df['Unnamed: 1'].str.replace('I','1')
t2 = m1.str.replace('11','2')
t3 = m2.str.replace('21','3')
t4 = m3.str.replace('1V','4')


# In[90]:


bbdd = pd.DataFrame(
    {
        'year':year.astype(int).values,
        'trimestre':t4.values,
        'region':pd.DataFrame(['Navarra']*df_pib.shape[0]).values.tolist(), #Poner todo Euskadi
        'PIB':df_pib,
        'VABAgricultura':df_agricultura,
        '%VABAgricultura':(df_agricultura/df_vabTotal)*100,
        'VABIndustria':df_industria,
        '%VABIndustria':(df_industria/df_vabTotal)*100,
        'VABConstruccion':df_construccion,
        '%VABConstruccion':(df_construccion/df_vabTotal)*100,
        'VABServicios':df_servicios,
        '%VABServicios':(df_servicios/df_vabTotal)*100,
        'VABTotal':df_vabTotal,
    }
)


# In[92]:


bbdd


# In[93]:


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




