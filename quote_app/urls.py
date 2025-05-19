# parcelhero/urls.py
from django.contrib import admin
from django.urls import path
from quote_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.quote_me, name='quote-me'),
    path('api/quotes/', views.get_parcel_quotes, name='api-quotes'),
]
