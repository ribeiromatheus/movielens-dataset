import pandas as pd

# Top 5 highest average and rating movies

movie_rating = pd.read_csv('https://raw.githubusercontent.com/ribeiromatheus/movielens-data/master/ratings.csv')
movie_rating.columns = ['User_ID', 'Movie_ID', 'Rating', 'Moment']

# total rating per movie
total_movies_rating = movie_rating.groupby('Movie_ID')['Rating'].count()
total_movies_rating.head()

# mean and votes
movies_mean_and_rating = mean_movies.join(total_movies_rating, on='Movie_ID')
movies_mean_and_rating = movies_mean_and_rating.rename(columns={'Rating': 'Total_Rating'})
movies_mean_and_rating['Average'] = movies_mean_and_rating['Average'].round(2)
movies_mean_and_rating.head()
