from django.contrib import admin
from django.urls import path, include
from app_bort import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('room_detail/<int:room_id>/', views.room_detail, name='room_detail'),
    path('create_booking/<int:room_id>/', views.create_booking, name='create_booking'),
    path('cancel_booking/<int:booking_id>', views.cancel_booking, name='cancel_booking'),
    path('delete_room/<int:room_id>/', views.delete_room, name='delete_room'),
    path('create_booking_room/', views.create_booking_room, name='create_booking_room'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('logout/', views.user_logout, name='logout')
]