from django.urls import path
from . import views


urlpatterns= [
    path('', views.new),
    path('tomek', views.base),
    # path('<str:pk>', views.CreateListProfile.as_view()),
    path('<str:pk>',views.Count.as_view()),


]