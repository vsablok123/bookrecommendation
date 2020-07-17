import sys
sys.path.append("C:/Users/sablo/original/Books Recommender System")
from SGDRecommender import ExplicitMF

from app import app as application

if __name__ == "__main__":
    application.run()