# Book Recommendation System

## Overview
Recommender Systems are a novel way to find out relations between two groups of OBJECTS/SUBJECTS. We often have one component as the end user to whom we want to recommend new items. There are interesting patterns to be studied within item-user interactions because the similarities between users and similarity between items. Here I have tried to create a usable and fast recommendation for books. The purpose is to recommend books to users in all genres even if the user is not familiar with those genres. This comes with the idea that people often want to explore different kinds of books but are often only recommended their favorite genres. 

## Data
The Data has been taken from Kaggle Goodbooks data set from GoodReads. This contains a list of 10,000 book and 50,000 users creating a vast expanse. I tried to use the whole data but due to system limitations, I had to limit to 2000 books and 5000 users. 

## Feature Extraction 
Feature extraction was done to find the appropriate three major genres for each book from hundreds of tags. This involved two things. First I cleaned up the tags so that a phrase/sentence can be represented by one word. Then I used nltk tokenize and frequency functions to find the most appearing tags for each book. The top three tags were selected to represent the genre. 

## Model 1 - Similarity based Collaborative Filtering
I used the similarity between user-user and book-book to find what a particular user might end up liking. 
Step 1 was to try the basic approach where we find simiarity with all users/books.
Secondly, I tried to use top K similar users/books to find recommendations.
Third step was to vary K and see if we get better performance for some K.
Final step was to reduce bias by estimating the difference of rating with mean rather than absolute rating.

## Model 2 - SVDS
I tried to use a simple svds(Single Vaue Decomposition) Factorization which works well with sparse data but our data was very sparse so it did not perform well. The performance was similar to Model 1.

## Model 3 - SGD
I tried a new approach which I had read about in a blog post(https://www.ethanrosenthal.com/2016/01/09/explicit-matrix-factorization-sgd-als/). He explained how we can use stochastic descent with cost functions to estimate the ratings accurately and fast. 
I developed the model ground up (since it does not exist) using the steps given in the blog. The model was very flexible with varying parameters like number of iterations, learning rate, regularization param, no of factors. Also a custom GridSearch was created to get the best params. 
This model performed the best of all giving a MSE of 0.83. 

## Model Deployment
The model was deployed on a local server using Flask. I created an attactive webpage to show all the recommendation results in neat tiles. The function was basic, taking in an existing user's name and recommending books to him in all major genres.

## Conclusion/Future Steps
The recommendations given were quite similar to the books a user had already read. I checked for myself as well. The results were actually the books which I want to read at some point(some of them!). This shows that the purpose of this project was achieved. It was also a great learning experience because I developed a model ground up with all the necessary functions/parameters/gridSearch. And deploying a custom model was a challenge as well because we had to take care of refreshing the necessary variables on each new test run. 

Future steps will be to get recommendations for a new user based on how he rates certain popular books. Another idea it to create an interface where a user can enter a book he really loved and the algorithm will recommend books very similar to that one.
