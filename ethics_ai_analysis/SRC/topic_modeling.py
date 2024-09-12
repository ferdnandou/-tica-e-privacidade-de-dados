import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Carregar o conjunto de dados
df = pd.read_csv('Dataset/kaggleaiethics_papers.csv')

# Vetorização dos textos
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['narrative'])

# Modelagem de tópicos
lda = LatentDirichletAllocation(n_components=5, random_state=0)
lda.fit(X)

# Exibir os tópicos
for index, topic in enumerate(lda.components_):
    print(f"Topic #{index + 1}:")
    print([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]])
