from django.conf.urls import include, url
from . import views

"""
camada feita na inclusao do post_list
"""

urlpatterns = [ 
    url(r'^$', views.post_list),
]
