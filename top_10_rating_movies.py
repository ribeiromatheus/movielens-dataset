import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Top 10 movies

movies = pd.read_csv('https://raw.githubusercontent.com/ribeiromatheus/movielens-data/master/movies.csv')
movies.columns = ['Movie_ID', 'Title', 'Genre']

movies = pd.read_csv('https://raw.githubusercontent.com/ribeiromatheus/movielens-data/master/movies.csv')
movies.columns = ['Movie_ID', 'Title', 'Genre']

# total votes per movie
total_movies_rating = movie_rating.groupby('Movie_ID')['Rating'].count()
total_movies_rating.head()

# mean and votes
movies_mean_and_rating = mean_movies.join(total_movies_rating, on='Movie_ID')
movies_mean_and_rating = movies_mean_and_rating.rename(columns={'Rating': 'Total_Rating'})
movies_mean_and_rating['Average'] = movies_mean_and_rating['Average'].round(2)
movies_mean_and_rating.head()

top_10_rating_movies = movies_mean_and_rating.sort_values(by='Total_Rating', ascending=False).head(10)
top_10_rating_movies_titles = top_10_rating_movies['Title'].to_list()
top_10_rating_movies_ids = top_10_rating_movies['Movie_ID'].to_list()

plt.figure(figsize=(18,8))

ax = sns.boxplot(x='Movie_ID', y='Rating', data=movie_rating.query(f'Movie_ID in {top_10_rating_movies_ids}'))
ax.set_xticklabels(top_10_rating_movies_titles, fontSize=12)
ax.set_xlabel('Movie', fontSize=16)
ax.set_ylabel('Rating', fontSize=16)

plt.xticks(rotation=45)
plt.show()
