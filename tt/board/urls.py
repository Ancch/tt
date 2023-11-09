from django.urls import path
from .views import index, tt, new, all, comment

urlpatterns = [
    path('', index, name='index'),
    path('all/', all, name='all'),
    path('new/', new, name='new'),
    path('comment/<slug:slug>/', comment, name='comment'),
    path('tt/<slug:slug>/', tt, name='tt'),
]
