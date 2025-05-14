import statsmodels.api as sm
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np


#Criar uma dataframa com dados fictícios
data = {'Vendas_Sorvetes': [200,300,400,350,500],
        'Temperatura': [28,30,32,29,33],
        'Promocao_Marketing': [1000,1200,800,900,1100]
}

df = pd.DataFrame(data)

#Adicionar uma constante para o termo de intercepto
df['Intercepto'] = 1

#Definir as variáveis independentes (X)
X = df[['Intercepto', 'Temperatura', 'Promocao_Marketing']]

#Definir a variavel dependente (Y)
Y = df['Vendas_Sorvetes']

#criar e ajustar o modelo de regressão linear múltipla
modelo = sm.OLS(Y,X).fit()

#realizar as previsões
y_pred = modelo.predict(X)

#Calcular MAE, RMSE e MSE
mae = mean_absolute_error (Y,y_pred)
mse = mean_absolute_error(Y,y_pred)
rmse = np.sqrt(mse)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'RMSE: {rmse}')