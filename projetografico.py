# -*- coding: utf-8 -*-
"""projetografico.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18FnuyoCVJT8jZMq_gFKApYP22VRQ02BZ

**VIZUALIZAÇÃO DA INFORMAÇÃO**
O projeto da disciplina visa apresentar ium implementação, em Python, da visualição d informação presente em dataset usando ao menso três técnicas estudadas na disciplina.

Os dados retirados do site: https://brasil.io/dataset/covid19/caso_full/?page=3 usando a tabela "covid19-0ec79f3d33c549b79486907a397bef47" referente ao Estado da Bahia.

**1. IMPORTAÇÃO DE DADOS COM IMPRESSÃO DE TELA**
"""

import matplotlib.pyplot as plt; plt.rcdefaults() 
import numpy as np 
import pandas as pd 
import seaborn as sns
import plotly.graph_objects as go
import geopandas as gpd

from pandas import read_csv

covid = pd.read_csv("/content/drive/MyDrive/covid19-ba.csv")

ba = pd.DataFrame()

print(covid)

"""**DADOS DISTRIBUIDOS POR CIDADES DA BAHIA**"""

covid.groupby('city').describe()

"""**AGRUPAMENTO CIDADES DA BAHIA COM MENOR NÚMERO DE MORTOS**"""

covid.groupby('deaths').min()

covid.groupby('death_rate').min()
plt.plot(covid['confirmed'], covid['deaths'], 'oy')
plt.xticks(rotation=0)
ax.invert_xaxis()
plt.rcParams['figure.figsize'] = (5,5)
plt.title('MORTOS NA BAHIA POR COVID-19', loc='center', fontsize=22, fontweight=30)
plt.xlabel('Casos confirmados', {'color': 'blue', 'fontsize': 20})
plt.ylabel('Mortos', {'color': 'red', 'fontsize': 20}) 
plt.show()

"""**PORCENTAGEM A CADA 100 MIL HABITANTES**"""

covid.plot.scatter('death_rate', 'confirmed_per_100k_inhabitants', figsize=(5,5))

plt.title('PORCENTAGEM CADA 100 MIL HABITANTES', loc='center', fontsize=22, fontweight=30)
plt.xlabel('Mortos em %',  {'color': 'brown', 'fontsize': 20})
plt.ylabel('Casos por 100 mil hab', {'color': 'green', 'fontsize': 20})

!pip install git+git://github.com/geopandas/geopandas.git