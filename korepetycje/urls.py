from django.urls import path
from . import views
app_name = 'korepetycje'

urlpatterns= [
    path('', views.new),
    # path('tomek', views.base),
    # path('list',views.CreateListProfile.as_view()),
    # path('<str:pk>',views.Count.as_view()),
    # path('profile/<pk>', views.ProfileDetailView.as_view(),name = 'detail'),




]