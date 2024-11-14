from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page/<slug:slug>/', views.content_page, name='content_page'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_list2/<int:pk>/', views.post_list2, name='post_list2'),
    path('content-block/<int:pk>/', views.post_list2, name='content_block_detail'),
    path('search/', views.search_view, name='search'),
]