from django.urls import path
from . import views

urlpatterns=[
    path('',views.entry_list),
    path('Add/',views.AddUser),
    path('Edit/<id>',views.EditUser),
    path('View/<id>',views.ViewUser),
    path('Delete/<id>',views.DeleteUser),
]