import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Movies by genre

movies = pd.read_csv('https://raw.githubusercontent.com/ribeiromatheus/movielens-data/master/movies.csv')
movies.columns = ['Movie_ID', 'Title', 'Genre']

sns.set_style('whitegrid')

movies_by_genre = movies['Genre'].str.get_dummies('|').sum().sort_values(ascending=False)

plt.figure(figsize=(16,8))

sns.barplot(x=movies_by_genre.index,
            y=movies_by_genre.values,
            palette=sns.color_palette('BuGn_r', n_colors=len(movies_by_genre) + 4))
plt.xticks(rotation=45)
plt.show()
