"""
Urls for shortener app urlshortener/urls.py
"""

from django.urls import path
from short_url_app import views
# from .views import redirect_url_view, create_short_url, SHORT_URL_PATH

appname = "short_url_app"

urlpatterns = [
    # path('create', views.create_short_url),
    path('create', views.ShortenerDetail.as_view()),
    path(f's/<str:short_url>', views.ShortenerDetail.as_view()),
]
