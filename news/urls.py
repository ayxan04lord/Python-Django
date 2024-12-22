from django.urls import path, re_path
from news.views import *

urlpatterns = [

    path('', index),
    path('about/', about),
    path('contact/', contact),
    path('category/', category),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('category/<int:catID>', category),
    # path('category/<str:catID>', category),
    # path('category/<uuid:catID>', category),
    # path('category/<path:catID>', category),
]
