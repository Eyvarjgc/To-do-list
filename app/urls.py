from django.urls import path
from . import views
urlpatterns = [

    # VIEWS
    path('',views.Home,name='home'),
    path('tareas/<int:pk>',views.TaskView,name='tareas'),
    
    # CRUD
    path('addtask/',views.addtask,name="addtask"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('coments/<int:id>',views.coments,name="coments"),
    path('edit/<int:id>', views.edit,name="edit"),


    # USER
    path('register/',views.Register,name='register'),
    path('logoutUser/',views.logoutUser,name="logoutUser"),
]

