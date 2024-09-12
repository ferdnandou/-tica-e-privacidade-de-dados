import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
df = pd.read_csv('Dataset/kaggleaiethics_papers.csv')

# Visualização de palavras mais frequentes
from wordcloud import WordCloud

text = ' '.join(df['narrative'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Nuvem de Palavras dos Artigos')
plt.savefig('wordcloud.png')
plt.show()
