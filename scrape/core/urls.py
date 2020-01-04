from django.urls import path

from . import views
from .utils import get_patterns

settings = [
    {
        'name': 'movie',
        'routes': [
            {
                'path': '',
            }, {
                'path': '/<int:page>'
            }
        ]
    }
]

urlpatterns = get_patterns(settings)

urlpatterns += [
    path('mv/', views.MovieListCreateViewSet.as_view()),
    path('mv/<pk>/', views.MovieRetrieveUpdateDestroyViewSet.as_view()),
]
