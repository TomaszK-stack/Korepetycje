from django.urls import path
from . import views


urlpatterns= [
    path('', views.CreateListProfile.as_view()),
    # path('',include('django.contrib.auth.urls'))
   path('tomek', views.new),
    # path('register'include,)



]