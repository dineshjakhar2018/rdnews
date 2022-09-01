from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('contact/', views.contact, name = 'contact'),
    path('photo/', views.photo, name = 'photo'),
    path('video/', views.video, name = 'video'),
    path('magazine/', views.magazine, name = 'magazine'),
    path('national/',views.national, name='national'),
    path('international/',views.international, name='international'),
    path('rajasthan/',views.rajasthan, name='rajasthan'),
    path('politics/',views.politics, name='politics'),
    path('sports/',views.sports, name='sports'),
    path('entertainment/',views.entertainment, name='entertainment'),
    path('carrier/',views.carrier, name='carrier'),

    path('national/news/<news_des>', views.news_description,name='news-description'),
    path('international/news/<news_des>', views.news_description,name='news-description'),
    path('rajasthan/news/<news_des>', views.news_description,name='news-description'),
    path('politics/news/<news_des>', views.news_description,name='news-description'),
    path('sports/news/<news_des>', views.news_description,name='news-description'),
    path('entertainment/news/<news_des>', views.news_description,name='news-description'),
    path('carrier/news/<news_des>', views.news_description,name='news-description'),
    path('news/news/<news_des>', views.news_description,name='news-description'),
    path('news/<news_des>', views.news_description,name='news-description'),
]
