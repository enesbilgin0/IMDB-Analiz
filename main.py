import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

source_file = "movies_initial.csv"

initial_df = pd.read_csv(source_file)
valid_scores_df = initial_df.dropna(subset=["metacritic"])


sorted_movies = valid_scores_df.sort_values(by="metacritic", ascending=False)
top_films = sorted_movies.head(50).copy()
director_freq = top_films["director"].value_counts()

if top_films["runtime"].dtype == 'object':
    top_films.loc[:, "runtime"] = top_films["runtime"].str.replace(" min", "").astype(float)

# --- Görselleştirme Bölümü ---
plt.subplot(1, 2, 2)
sns.histplot(data=top_films, x="runtime", bins=10, kde=True, color='purple') 
plt.title('Top 50 Film Süre Dağılımı')
plt.xlabel('Süre (Dakika)')
plt.ylabel('Film Adedi')

plt.show()

plt.bar(director_freq.index, director_freq.values)
plt.title('Top 50 Listesindeki Yönetmenler')
plt.ylabel('Film Sayısı')
plt.xticks(rotation=90) 

plt.show()
