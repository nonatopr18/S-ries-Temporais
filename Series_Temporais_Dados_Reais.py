# Gerando o Randon Walk
from statsmodels.tsa.stattools import adfuller
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.seasonal import seasonal_decompose, STL
import yfinance as yf
import matplotlib.ticker as mtciker
from datetime import datetime
import gc
#gc.collect()
# # BAixar os dados: Definir o ticket
#ticker = 'GOOG'
# Gerando as datas de inicio e fim da série temporal
#data_inicio='2020-01-01'
#data_fim='2021-07-01'
# Baixar os dados
#dados_mensais = yf.download(ticker, start=data_inicio, end=data_fim,interval='1mo') # baixar os dados
# Verificar se os mesmos foram baixados
#print("\n---Mostrando a 5 primeiras linhas dos dadosdados_mensais(GOOG): ---")
#print(dados_mensais.tail())
#print(dados_mensais.info())
# Salvando o arquivo no diretorio onde o python esta sendo executado
#dados_csv = f'{ticker}_historico.csv'
#dados_mensais.to_csv(dados_csv, index=True)
dados1 = pd.read_csv(
     'C:/Users/nonat/OneDrive\Desktop/Instituto Inteligência de Dados/Ciencia de Dados/DataScience/Desafio_Tecnico/Séries_Temporais/GOOG_historico.csv')
dados1['Price'] = pd.to_datetime(dados1['Price'], errors='coerce')
dados1['Close'] = pd.to_numeric(dados1['Close'], errors='coerce')
dados1=dados1.drop([0,1])
print(dados1)
#print(dados1[['Price','Close']].dtypes)
# Plotando a série temporal
fig,ax=plt.subplots()
ax.plot(dados1['Price'],dados1['Close'])
ax.set_xlabel('Data')
ax.set_ylabel('Valor Observado')
ax.set_title('Valor Observado da Ação')
#plt.xticks([4, 24, 46, 68, 89, 110, 132, 152, 174, 193, 212, 235],
#['May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 2021, 'Feb',
#'Mar', 'April'])
fig.autofmt_xdate()
plt.tight_layout()
plt.show()
# Verifica-se que o processo não é estacionário. 
# Será verificado a autocorrelação serial, ou seja, existência de raiz unitária
acao_ADF_resultado=adfuller(dados1['Close'])
print(f'ADF Estatística: {acao_ADF_resultado[0]}')
print(f'ADF Estatística: {acao_ADF_resultado[1]}')
# Pelo as sáidas nota-se que existe raiz unitária
dif_Fecha=np.diff(dados1['Close'],n=1)
acao_ADF_resultado_dif=adfuller(dif_Fecha)
print(f'ADF Estatística: {acao_ADF_resultado_dif[0]}')
print(f'ADF Estatística: {acao_ADF_resultado_dif[1]}')
# Verificando graficamente a autocorrelação serial
plot_acf(dif_Fecha,lags=10)
plt.show()
