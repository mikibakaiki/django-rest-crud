from django.urls.conf import path, re_path
from tutorials import views

urlpatterns = [
    path('api/tutorials', views.tutorial_list),
    re_path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    re_path(r'^api/tutorials/published$', views.tutorial_list_published)
]
