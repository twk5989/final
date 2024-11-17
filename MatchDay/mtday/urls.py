from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home_html'),
    path('login/', views.login_view, name='login'),
    path('sign_up/', views.sign_up_view, name='sign_up'),
    path('logout/', views.logout_view, name='logout'),
    path('mypage/', views.mypage_view, name='mypage'),  # 개인정보 페이지
    path('edit_mypage/', views.edit_mypage_view, name='edit_mypage'),  # 개인정보 수정 페이지
    path('local_club_list/', views.local_club_list_view, name='lcl'),
    path('sports/', views.sports_view, name='sports'),
    path('board/', views.board_view, name='board'),
    
]
