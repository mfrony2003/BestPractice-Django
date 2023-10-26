from django.urls import path
from apps.polls import views


urlpatterns = [    
      path('',views.Home, name='Home'), 
]