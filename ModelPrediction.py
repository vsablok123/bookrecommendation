# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:06:23 2020

@author: sablo
"""

#import sys
#sys.path.append("C:/Users/sablo/original/Books Recommender System")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

    # Load the Recommender SGD model
filename = 'C:/Users/sablo/original/Books Recommender System/book-recommender-sgd-model.pkl'
sgdd = pickle.load(open(filename, 'rb'))



ratings = pd.read_csv("C:/Users/sablo/original/Books Recommender System/final_model_ratings")
userindex = pd.DataFrame(data = ratings['user_id'].unique())
bookindex = pd.DataFrame(data = ratings['book_id'].unique())
books = pd.read_csv("C:/Users/sablo/original/Books Recommender System/final_books_list")


#Example Prediction to check the Validity of the model
uindex = 1

user5ratings = ratings[(ratings["user_id"] == userindex.iloc[uindex][0]) & (ratings['rating'] == 5)]
booknames = books[books['id'].apply(lambda x: x in user5ratings['book_id'])]['title']

#26      Harry Potter and the Half-Blood Prince (Harry ...
#108                                        Les Misérables
#158     The Battle of the Labyrinth (Percy Jackson and...
#174     The Last Olympian (Percy Jackson and the Olymp...
#230                                           Sarah's Key
#240                                      Number the Stars
#323                                               Fangirl
#656                                       The White Tiger
#672                                            Americanah
#899                                      The Selfish Gene
#977               Shadow of Night (All Souls Trilogy, #2)
#1119                                       Aesop's Fables
#1349                                Lirael (Abhorsen, #2)
#1823                   Flawless (Pretty Little Liars, #2)
#2254       An Unquiet Mind: A Memoir of Moods and Madness
#3912                                          Immortality

prediction = {}
for bindex in range(0,2987):
    prediction[bindex] = sgdd.predict(uindex, bindex)
    
top10books = sorted(prediction.items(), key = 
             lambda kv:(kv[1], kv[0]))[-10:]
topbooknames = books[books['id'].apply(lambda x: x in list(zip(*top10books))[0])][['title', 'average_rating']]

#average_rating
#39                                      Eat, Pray, Love            3.51
#248                 Extremely Loud and Incredibly Close            3.97
#268                                     P.S. I Love You            4.01
#287   The Hunt for Red October (Jack Ryan Universe, #4)            4.01
#487                                      The Green Mile            4.42
#826   To All the Boys I've Loved Before (To All the ...            4.11
#1238                      Chronicle of a Death Foretold            3.95
#2354                                       Silas Marner            3.60
#2362  Beautiful Boy: A Father's Journey Through His ...            4.03
#2862                The Kill Artist (Gabriel Allon, #1)            4.00

pred_book_ratings = {}
book_recommendations = {}

def set_books_ratings(user_id, pred_book_ratings):
    uindex = userindex[userindex[0] == user_id].index[0]
    for bindex in range(0,2987):
        pred_book_ratings[bindex] = sgdd.predict(uindex, bindex)

def remove_read_books_ratings(user_id, pred_book_ratings):
    readbook_ids = ratings[ratings['user_id'] == user_id]['book_id']
    readbook_index = getbookindexfromidlist(readbook_ids)
    for item in readbook_index:
        if item in pred_book_ratings.keys():
            del pred_book_ratings[item]

def getbookindexfromidlist(book_ids):
    return book_ids.values

def getuserindexfromuserid(user_id):
    return userindex[userindex[0] == user_id].index[0]

def getbookidfromindexlist(bindexlist):
    return bookindex.loc[bindexlist][0]

def set_recommended_books(pred_book_ratings):
    genres = ["Auto/Biography","Classics","Fantasy", "Fiction", "Humor and Comedy", "Nonfiction", "Romance", "Science Fiction",
          "Suspense", "Thriller","Non-Fiction"]
    top100bookindex = sorted(pred_book_ratings.items(), key = 
             lambda kv:(kv[1], kv[0]))[-100:]
    
    top100books = books[books['id'].apply(lambda x: x in getbookidfromindexlist(list(list(zip(*top100bookindex))[0])))]
    
    #top100books = top100books.sort_values('Avg_Rating', ascending = False)

    for index, row in top100books.iterrows():
        for genre in genres:
            if (row[genre] == 1):
                if (genre in book_recommendations.keys()):
                    book_recommendations[genre] = book_recommendations[genre].append(row, ignore_index = True)
                else: 
                    book_recommendations[genre] = pd.DataFrame(data = row.values.reshape(1,36), columns = row.index)
                
                if len(book_recommendations[genre]) == 6:
                    genres.remove(genre)
                break
        if (len(genres) <= 4):
            break
        