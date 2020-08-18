import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from lime import lime_text

## Serving Machine Learning Model
def predict(text):

    """
    Input: text
    -------------------------------
    Output: 
    - category_str: predicted category 
    - scores: probability score for the predicted category
    - score_pred: prob scores for all class in array of size [6,1]
    - viz: lime generated html for visualization
    """

    category_dict = {0:'sport',1:'business',2:'tech', \
        3:'entertainment',4:'politics',5:'food'}
    category_names = ['sport','business','tech','entertainment','politics','food']

    ## Recovering vectorizer and model
    model_path = './classifier/serving/model/model_v2.joblib'
    model = joblib.load(model_path)
    
    ## Predict Category and Probability Score
    category_pred = model.predict([text])
    score_pred = model.predict_proba([text])
    category_str  = [category_dict.get(pred) for pred in category_pred][0]
    scores = np.max(score_pred)

    ## Create Lime Explanation HTML
    explainer = lime_text.LimeTextExplainer(class_names=category_names)
    explained = explainer.explain_instance(text,
             model.predict_proba,top_labels=3, num_features=10) 

    viz = explained.as_html(text=False,predict_proba=True)

    return category_str,scores,score_pred,viz
