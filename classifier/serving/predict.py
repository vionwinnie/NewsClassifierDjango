import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import os 
import joblib

## Serving Machine Learning Model
def predict(text):
    category_dict = {0:'sport',1:'business',2:'tech', \
        3:'entertainment',4:'politics',5:'food'}

    curr_cwd = os.getcwd()
    ## Recovering vectorizer and model
    #vectorizer_path = './classifier/serving/model/tfidf.pb'
    #model_path = './classifier/serving/model/logistic_model.pb'
    model_path = './classifier/serving/model/model.joblib'

    model = joblib.load(model_path)

    #with open(vectorizer_path,'rb') as fid:
    #    tfidf = pickle.load(fid)

    #with open(model_path,'rb') as feed:
    #    model = pickle.load(feed)

    #vectorized_question = tfidf.transform([text])
    category_pred = model.predict([text])
    score_pred = model.predict_proba([text])

    category_str  = [category_dict.get(pred) for pred in category_pred]
    scores = np.max(score_pred)
    return category_str[0],scores,score_pred
