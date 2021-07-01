from django.urls import path
from . import views


urlpatterns= [
    path('', views.new),
    path('tomek', views.base),
    path('lista', views.CreateListProfile.as_view())


]