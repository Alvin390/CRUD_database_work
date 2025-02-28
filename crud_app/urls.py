from django.urls import path
from . import views

urlpatterns=[
    path('',views.entry_list),
    path('Add/',views.AddUser),
]