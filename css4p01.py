# -*- coding: utf-8 -*-
"""
Project on data manipulation, cleaning and analysis.

Created on Sat Oct 26 22:01:25 2024

@author: edemk
"""

import pandas as pd
df=pd.read_csv("movie_dataset.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df)
#%%Cleaning data
df.columns=df.columns.str.replace(' ','')#Removing spaces from column names
print(df.isnull().sum())#shows the number of missing rows of values per column
'''
128 in Revenue and 64 in metascore
'''
print(df.duplicated(subset=['Title', 'Year']).sum())#shows the number of duplicates of both the title and year simultaneously

'''
0 duplicates found
'''
#replacing missing values with thier mean values
df['Revenue(Millions)']=df['Revenue(Millions)'].fillna(df['Revenue(Millions)'].mean())
df['Metascore']=df['Metascore'].fillna(df['Metascore'].mean())



print(df.isnull().sum())#checking again for null values
'''
No missing values recorded
'''
#%%
#Question 1 What is the highest rated movie in the dataset?

highest_movie=df[df['Rating']==df["Rating"].max()]#checking the max nmber in ratings column
print(highest_movie)
'''
The highest rated movie is the Dark Knight
'''
#%%
#Question 2 What is the average revenue of all movies in the dataset? 

avgRevenue=df['Revenue(Millions)'].mean()#caclulates the average value of the Revenue
print(avgRevenue)
'''
The average Revenue in Millions is 82.96
'''
#%%
#Question 3 What is the average revenue of movies from 2015 to 2017 in the dataset?

movies_btn_2015_2017=df[(df['Year']>=2015)&(df['Year']<=2017)]#filtering movies between 2015 and 2017
avgRevenue2=movies_btn_2015_2017['Revenue(Millions)'].mean()#caclulates the average value of the Revenue
print(avgRevenue2)
'''
The average Revenue between 2015 and 2017 in Millions is 68.06
'''
#%%
#Question 4 How many movies were released in the year 2016?

Movies_2016=df[df['Year']==2016]#Table of movies released in 2016
numMovies_2016=len(Movies_2016)# number of released movies in 2016
print(numMovies_2016)
'''
The number of movies in 2016 was 297
'''
#%%
#Question 5 How many movies were directed by Christopher Nolan?

nolan_movies=df[df['Director']=='Christopher Nolan']#Table of movies released by Christopher Nolan
print(nolan_movies)
num_nolan_movies=len(nolan_movies)
print(num_nolan_movies)
'''
The number of movies directed by Christopher Nolan was 5
'''
#%%
#Question 6 How many movies in the dataset have a rating of at least 8.0?

ratings=df[(df['Rating']>=8.0)]#Table of movies with a rating of 8 and above
print(len(ratings))
'''
The number of movies with a rating of at least 8 was 78
'''
#%%
#Question 7 What is the median rating of movies directed by Christopher Nolan?
nolan_median_ratings=nolan_movies['Rating'].median()#Table of movies with a rating of 8 and above
print(nolan_median_ratings)
'''
The median of Christopher Nolan movies is 8.6
'''
#%%
#Question 8 Find the year with the highest average rating?
avgRating_by_year=df.groupby('Year')['Rating'].mean()#finds the average rating per year
print(avgRating_by_year)
highest_avg_rating_year = avgRating_by_year.idxmax()#returns the year with the highest average rating
print(highest_avg_rating_year)
'''
2007 had the highest average rating
'''

#%%
#Question 9 What is the percentage increase in number of movies made between 2006 and 2016?
Movies_2006=df[df['Year']==2006]#Table of movies released in 2006
numMovies_2006=len(Movies_2006)#Returns the number of movies released in 2006

Movies_2016=df[df['Year']==2016]#Table of movies released in 2016
numMovies_2016=len(Movies_2016)#returns the number of movies released in 2016

percentage_increase=((numMovies_2016-numMovies_2006)/numMovies_2006)*100#calculates percentage increase
print(percentage_increase)

'''
The percentage increase in the number of movies
between 2006 and 2016 is 575.0 percent
'''


#%%
#Question 10 Find the most common actor in all the movies?
split_actors=df['Actors'].str.split(', ').explode()#splits the actors in the actor column
count_actors=split_actors.value_counts()#counts the occurence of each actor
most_common_actors=count_actors.head(10)#returns the top 10 most common actors

print(most_common_actors)
'''
The most common actor is Mark Wahlberg
'''
#%%
#Question 11 How many unique genres are there in the dataset?
split_genre=df['Genre'].str.split(', ').explode().unique()#splits the genres in the actor column
total_genre=len(split_genre)#returns the number of genres
print(total_genre)

'''
The total number of genres is 207
'''


#%%
#Question 12
'''

Do a correlation of the numerical features, what insights can you deduce? Mention at least 5 insights.

And what advice can you give directors to produce better movies?

1. Most of the missing values took place in the Metascore and Revenue(Milions) column.
2. The year of 2007 arguably had high performing movies relative to other years in terms of Ratings.
3. Movies grew by 5.75 times from 2006 to 2016 meaning the market for movies has grown greatly throughout the years.
4. The most common actor in Movies is Mark Whalberg meaning he is most likely to do more movies relative to other actors.
5. Out of all the 1000 movies only 78 recieved a movie rating of 8 and above meaning it is very rare for movies to recieve a rating of at least 8.
6. Most of the common actors are men meaning there is a low representation of reoccuring female actors.

To produce better movies directors can watch and analyse movies that recieved high ratings 
such as the movies that recieved an 8 and above. They can watch and analyse movies directed
by high performing directs such as Christopher Nolan who has a median rating of movies of 8.6.
Additionally they can employ most of the common actors in their movies as viewers may enjoy seeing
them star in movies.
'''