import pandas as pd

# Carregar o conjunto de dados
df = pd.read_csv('Dataset/kaggleaiethics_papers.csv')

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Resumo estatístico e estrutura dos dados
print(df.info())
print(df.describe())

# Verificação de valores ausentes
print(df.isnull().sum())
