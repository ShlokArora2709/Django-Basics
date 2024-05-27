from django.urls import path
from . import views

urlpatterns=[
    path('HelloWorld/',views.HelloWorld ,name='HelloWorld')
    ,path('Members/',views.Members,name='Members')
    ,path('Members/details/<int:id>',views.details,name='details')
    ,path('',views.main,name='main'),
    path('testing/', views.testing, name='testing'),
]