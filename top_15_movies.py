import pandas as pd

# Top 15 highest average movies

movies = pd.read_csv('https://raw.githubusercontent.com/ribeiromatheus/movielens-data/master/movies.csv')
movies.columns = ['Movie_ID', 'Title', 'Genre']

movie_rating = pd.read_csv('https://raw.githubusercontent.com/ribeiromatheus/movielens-data/master/ratings.csv')
movie_rating.columns = ['User_ID', 'Movie_ID', 'Rating', 'Moment']

mean_rating_by_movie = movie_rating.groupby('Movie_ID')['Rating'].mean()

mean_movies = movies.join(mean_rating_by_movie, on='Movie_ID')
mean_movies = mean_movies.rename(columns={'Rating': 'Average'})
mean_movies.sort_values('Average', ascending=False).head(15)
