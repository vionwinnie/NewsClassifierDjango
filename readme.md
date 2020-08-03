# Project Name: News Classifier Portal
## Purpose: 
 - Portal for user to enter news article and show news category classification
 - Using local surrogate model to display which words in the text triggers such prediction using LIME algorithm
## Tech Stack:
 - Language: Python 3.7
 - Web Application Framework: Django
 - Database: sqlite
 - Deployment: GCP App Engine

## Roadmap:
 - Add Lime Explainer
 - Migrate to Firebase db

## Create local testing environment
 - `conda create -n newsApp_env python=3.7 pip`
 - `conda activate newsApp_env`
 - `pip install -r requirements.txt`

## To Start the application:
 - `python manage.py runserver`

## News Categories:
 - Food
 - Sport
 - Politics
 - Entertainment
 - Tech
 - Business

