"""
Urls for url shortener app
"""

from django.urls import path
from url_shortener import views

appname = "url_shortener"

urlpatterns = [
    path('create', views.ShortenerDetail.as_view()),
    path(f's/<str:short_url>', views.ShortenerDetail.as_view()),
]
