from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:number>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('create_post/', views.create_post, name='create_post'),
    path('<int:pk>/<slug:sl>/delete/', views.delete_post, name='delete'),
    path('<int:pk>/<slug:sl>/edit/', views.edit_post, name='edit'),

    path('search', views.search, name='search'),
]
