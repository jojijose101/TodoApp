
from django.urls import path

from todoapp import views
app_name = 'todoapp'
urlpatterns = [
    path('', views.index,name='index'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('cbvlist', views.Task.as_view(),name='cbvlist'),
    path('cbvdetail/<int:pk>/', views.TodoDetails.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TodoUpdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TodoDelete.as_view(), name='cbvdelete'),


]