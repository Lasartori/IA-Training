import pandas as pd
#Biblioteca que serve para tratar dados nulos
import missingno as msno
import seaborn as sb
import matplotlib.pyplot as plt
dados = pd.read_excel('Recrutamento.xlsx')
dados.shape

dados.head()

#Existe um campo status que retorna se a pessoa foi contratada, usando o set, 
# é possível avaliar se existe somente um yes ou no
#Mostra todo os status dentro do campo
set(dados.status)
#Utilizado para gerar estatísticas
dados.describe()
#entrega o tipo de cada dado
dados.info()

msno.matrix(dados)
#Puxa os dados nulos e caso encontre mais de um dado nulo em uma coluna, retorna a quantidade de nulos
dados.isnull().sum()
#campo plt.close() serve para que o gráfico não seja exibido
sb.boxplot(x='status', y='salary', data=dados, palette='hls', hue='status', legend=False)
plt.close()


#pega os campos nulos do salary e troca por True para realizar a tratativa
dados['salary'].fillna(value=0,inplace=True)

sb.boxplot(x=dados['hsc_p'])
plt.close()
#Histograma pra visualizar melhor os outliers
#plt.show serve para mostrar o gráfico ao rodar o código
sb.histplot(data=dados,x='hsc_p')
plt.close()
# plt.show()

sb.histplot(data=dados,x='degree_p')
plt.close()

#O campo salário mostra que existe uma grande discrepância
sb.boxplot(x=dados['salary'])
plt.close()

sb.histplot(data=dados,x='salary')
plt.close()


