# Gerando o Randon Walk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.seasonal import seasonal_decompose, STL
# Puxando os dados
np.random.seed(42)
passos=np.random.standard_normal(1000)
passos[0]=0
randon_walk=np.cumsum(passos)
# Plotando o Passeio Aleatório
fig,ax=plt.subplots()
ax.plot(randon_walk)
ax.set_xlabel('Tempo dos Saltos')
ax.set_ylabel('valor observado')
plt.tight_layout()
#plt.show()
# Função de Autocorrelação: Testando a estacionariedade
from statsmodels.tsa.stattools import adfuller
ADF_resultado=adfuller(randon_walk)
print(f'ADF Estatísticas: {ADF_resultado[0]}')
print(f'p-valor: {ADF_resultado[1]}')
# verificando a funçao de autocorrelação
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(randon_walk,lags=20)
# Tornando a serie estariconario
dif_random_walk=np.diff(randon_walk,n=1)
ADF_resultado1=adfuller(dif_random_walk)
print(f'ADF Estatísticas: {ADF_resultado1[0]}')
print(f'p-valor: {ADF_resultado1[1]}')
# Plotando as defasagens
passos=np.random.standard_normal(1000)
passos[0]=0
randon_walk=np.cumsum(passos)
# Plotando o Passeio Aleatório
fig,ax=plt.subplots()
ax.plot(dif_random_walk)
ax.set_xlabel('Tempo dos Saltos')
ax.set_ylabel('valor observado')
plt.tight_layout()
# Analisando as correlações defasadas
plot_acf(dif_random_walk,lags=20)
plt.show()