from textblob import TextBlob
import pandas as pd

# Carregar o conjunto de dados
df = pd.read_csv('Dataset/kaggleaiethics_papers.csv')

# Função para calcular o sentimento
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Aplicar análise de sentimento
df['sentiment'] = df['narrative'].apply(get_sentiment)

# Exibir a média do sentimento
print(df['sentiment'].mean())
