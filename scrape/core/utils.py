from . import views
from django.urls import path


def get_patterns(settings):
    """
    get patterns using settings
    :return: list
    """
    patterns = []
    for item in settings:
        name = item['name']
        routes = item['routes']
        for route in routes:
            pattern = path(name + route['path'],
                           getattr(views, name) if not hasattr(route, 'func') else getattr(views, route['func']),
                           name=name if not hasattr(route, name) else route['name'])
            patterns.append(pattern)
    return patterns
