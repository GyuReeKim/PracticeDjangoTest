from django.urls import path
from . import views

app_name = "musics"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/update/', views.update, name="update"),
    path('<int:id>/delete/', views.delete, name="delete"),
    path('<int:id>/create/', views.favor_create, name="favor_create"),
    path('<int:music_id>/delete/<int:favor_id>/', views.favor_delete, name="favor_delete"),
]
