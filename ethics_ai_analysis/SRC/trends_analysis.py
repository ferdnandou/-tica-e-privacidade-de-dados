import pandas as pd
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
df = pd.read_csv('Dataset/kaggleaiethics_papers.csv')

# Agrupar por ano e contar o número de artigos
df['year'] = pd.to_datetime(df['date']).dt.year
trends = df.groupby('year').size()

# Plotar tendências
plt.figure(figsize=(10, 6))
trends.plot(kind='line')
plt.title('Número de Artigos por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Artigos')
plt.grid(True)
plt.savefig('trends_over_time.png')
plt.show()
