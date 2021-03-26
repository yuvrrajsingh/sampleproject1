from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('submit', views.submit, name = 'submit'),
    path('delete/<int:i>', views.delete, name='delete'),
    path('todolist', views.todolist, name = 'todolist'),
    path('main', views.main, name='main'),
    path('sortdata', views.sortdata, name='sortdata'),
    path('searchtodo', views.searchtodo, name='searchtodo'),
    path('edit/<int:i>', views.edit, name='edit'),
    path('update/<int:i>', views.update, name = 'update')

]
