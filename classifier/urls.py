from django.urls import path

from . import views

urlpatterns = [
    # ex: /classifier/
    path('', views.index, name='index'),
    # ex: /classifier/5/results/
    path('<int:news_id>/results/', views.results, name='results'),
    # ex: /classifier/enter_text/
    path('enter_text/', views.enter_text, name='enter_text'),
]
