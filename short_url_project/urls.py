from django.urls import include, path

urlpatterns = [
    path('', include('short_url_app.urls')),
]
