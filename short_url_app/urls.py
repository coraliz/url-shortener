"""
Urls for shortener app urlshortener/urls.py
"""

from django.urls import path
from .views import redirect_url_view, create_short_url, SHORT_URL_PATH

appname = "short_url_app"


urlpatterns = [
    path('create', create_short_url, name='create'),
    #todo : decide what to do about the path
    path(f'{SHORT_URL_PATH}/<str:shortened_part>', redirect_url_view, name='redirect'),
]
