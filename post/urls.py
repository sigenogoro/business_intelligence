from django.urls import path
from django.conf.urls import url
from . import views

#name引数は、{% url name='引数'となる%}
#NoReverseMatchが起こる => int: numのようにするとなってしまう
urlpatterns=[
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('check', views.check, name='check'),
    path('message/', views.message, name='message'),
    path('message/<int:page>', views.message, name='message')
]