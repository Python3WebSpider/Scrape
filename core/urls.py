from django.urls import path
from . import views

settings = [
    {
        'name': 'movie',
        'routes': [
            path('movie', views.movie, name='movie'),
            path('movie/<pk>', views.movie, name='movie'),
            path('api/movie/', views.MovieListCreateViewSet.as_view()),
            path('api/movie/<pk>/', views.MovieRetrieveUpdateDestroyViewSet.as_view()),
        ]
    },
    {
        'name': 'login1',
        'routes': [
            path('login1', views.login1, name='login1'),
        ]
    }
]

urlpatterns = []
urlpatterns += [
    path('', views.index, name='index')
]

for setting in settings:
    urlpatterns += setting['routes']
