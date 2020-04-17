from django.urls import path

from core.views import URLList, redirect_view


app_name = 'core'

urlpatterns = [
    path('api/short-url', URLList.as_view(), name='list'),
    path('<slug:slug>', redirect_view, name='redirect')
]