#  Modelos de Séries Temporais
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Gerando uma série Temporal Artificial
tempo=np.arange(200)
obser=np.random.randn(200)*100 # Gerando 200 observaçoes de uma Gaussiana(0,1)
# Analisando Granficamente a Série Temporal
# Função Para Gerar as Análises Gráficas das Séries Temporais
def plot_serie_temporal(tempo,obser,title="Serie Temporal Observada"):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=tempo, y=obser)
    plt.title(title)
    plt.xlabel("Tempo")
    plt.ylabel("Valor observado")
    plt.grid(True)
    plt.show() 
#plot_serie_temporal(tempo,obser,title="Serie Temporal Observada")
# Gerar uma séries sem ser ruído branco
r=0.4
valores=np.zeros(200)
for i,x in enumerate(obser):
    if i==0:
       valores[i]=x
    else:
       valores[i]= r*valores[i-1] + np.sqrt((1-np.power(r,2)))*x
p1=plot_serie_temporal(tempo,obser,title="Serie Temporal Observada")
p2=plot_serie_temporal(tempo,valores,title="Serie Temporal Observada")


