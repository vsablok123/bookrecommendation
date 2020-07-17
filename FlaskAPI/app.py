
# Importing essential libraries
from flask import Flask, render_template, request, jsonify
import pandas as pd
import sys
sys.path.append("C:/Users/sablo/original/Books Recommender System")
#from SGDRecommender import ExplicitMF
import ModelPrediction
import importlib


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():

    if request.method == 'POST':
        
        req_data = request.form
        user_id = int(req_data['user_id'])
        importlib.reload(ModelPrediction)
        ModelPrediction.set_books_ratings(user_id, ModelPrediction.pred_book_ratings)
        ModelPrediction.remove_read_books_ratings(user_id, ModelPrediction.pred_book_ratings)
        ModelPrediction.set_recommended_books(ModelPrediction.pred_book_ratings)
        return render_template('result.html', recommendations=ModelPrediction.book_recommendations)

if __name__ == '__main__':
    app.run(debug=True)





