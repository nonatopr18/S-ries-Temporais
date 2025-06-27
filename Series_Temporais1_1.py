# Preprando os dados
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.seasonal import seasonal_decompose, STL
df= pd.read_csv('https://raw.githubusercontent.com/marcopeix/AppliedTimeSeriesAnalysisWithPython/main/data/jj.csv')
#print(df.head())
# Gerando o conjunto de treino e teste
treino=df[:-4]
teste=df[-4:]
# Gerar o erro absoluto percentual médio
def mape(y_obs,y_pred):
    print(np.mean(abs((y_obs-y_pred)/y_obs))*100) 
# Treinando o modelo
media_histo=np.mean(treino['data']).round(2)
print(media_histo)
# Fazendo a previsão pela média 
teste.loc[:,'media_predita']=media_histo # Previsão ingenua
# # Gerando as previsões pela média móvel
media_movel=np.mean(treino.data[-4:])
teste.loc[:,'Predito_Media_Movel']=media_movel # Previsão média móvel
# # Estimando Sazonalidade pelo último periodo
media_fim=treino.data.iloc[-1]
# # Estimando Sazonalidade pelo último periodo
teste.loc[:,'Predito Fim']=media_fim
# # Estimando Sazonalidade pelo método ingênuo
sazonalidade=treino['data'][-4:].values
teste.loc[:,'Predito Sazonalidade']=sazonalidade
print(teste)
# # Avaliando o desempenho
mape(teste['data'],teste['media_predita'])
mape(teste['data'],teste['Predito_Media_Movel'])
mape(teste['data'],teste['Predito Fim'])
mape(teste['data'],teste['Predito Sazonalidade'])
# # Visualizando a Série Temporal
fig,ax=plt.subplots()
ax.plot(treino['date'],treino['data'],'g-.',label='Treino')
ax.plot(teste['date'],teste['data'],'b-.',label='Teste')
ax.plot(teste['date'],teste['Predito Fim'],'r--.',label='Prditos')
ax.plot(teste['date'],teste['Predito_Media_Movel'],'r-.',label='Prditos Média Móvel')
ax.set_xlabel('Período')
ax.set_ylabel('Lucro por Ação (R$)')
ax.axvspan(80, 83, color= '#808080', alpha=0.2)
plt.xticks(np.arange(0, 85, 8), [1960, 1962, 1964, 1966, 1968, 1970, 1972,
1974, 1976, 1978, 1980])
fig.autofmt_xdate()
plt.tight_layout()
plt.show()
# # Comparando os esimadores
esimativas=[69.99,15.59,30.46,11.56]
medidas=['media_predita','Predito_Media_Movel','Predito Fim','Predito Sazonalidade']
# Cria a figura 
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(medidas, esimativas, color='skyblue') # armazenar os valores das barras
ax.bar_label(bars, fmt='%.1f') # Ajsutando as casas decimais
# Cria a figura e os eixos
plt.title(" Comparação dos indicadores")
plt.xlabel('Métodos de Estimar')
plt.ylabel('Erro Médio Absoluto (%)')
plt.tight_layout() # Ajusta o layout para evitar sobreposição
plt.show()