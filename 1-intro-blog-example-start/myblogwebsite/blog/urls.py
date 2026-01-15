from django.urls import path
from . import views

urlpatterns = [
    # Note: the empty string '' means the root of this app
    path('', views.post_list, name='post_list'),
]